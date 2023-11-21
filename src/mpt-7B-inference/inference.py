import sys
import os
from dataclasses import dataclass, asdict
from transformers import AutoConfig, AutoModelForCausalLM, AutoTokenizer

@dataclass
class GenerationConfig:
    temperature: float
    top_k: int
    top_p: float
    repetition_penalty: float
    max_new_tokens: int

def format_prompt(system_prompt: str, user_prompt: str):
    system_prompt = f"system\n{system_prompt}\n"
    user_prompt = f"user\n{user_prompt}\n"
    assistant_prompt = f"assistant\n"
    return f"{system_prompt}{user_prompt}{assistant_prompt}"

def generate(llm: AutoModelForCausalLM, tokenizer: AutoTokenizer, generation_config: GenerationConfig, prompt: str):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = llm.generate(
        **inputs,
        temperature=generation_config.temperature,
        top_k=generation_config.top_k,
        top_p=generation_config.top_p,
        repetition_penalty=generation_config.repetition_penalty,
        max_new_tokens=generation_config.max_new_tokens
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def load_model_and_tokenizer(model_name: str, trust_remote_code: bool = True):
    config = AutoConfig.from_pretrained(model_name, trust_remote_code=trust_remote_code)
    llm = AutoModelForCausalLM.from_pretrained(model_name, config=config, trust_remote_code=trust_remote_code)
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=trust_remote_code, use_fast=True)
    return llm, tokenizer

if __name__ == "__main__":
    model_name = "mosaicml/mpt-7b-chat"
    llm, tokenizer = load_model_and_tokenizer(model_name, trust_remote_code=True)

    system_prompt = "A conversation between a user and an LLM-based AI assistant named Local Assistant. Local Assistant gives helpful and honest answers."

    generation_config = GenerationConfig(
        temperature=0.2,
        top_k=0,
        top_p=0.9,
        repetition_penalty=1.0,
        max_new_tokens=512,
    )

    assistant_prefix = "[assistant]:"

    # Hardcoded user prompt
    hardcoded_user_prompt = "What is the weather like today?"

    prompt = format_prompt(system_prompt, hardcoded_user_prompt)
    response = generate(llm, tokenizer, generation_config, prompt)
    print(assistant_prefix, response)
