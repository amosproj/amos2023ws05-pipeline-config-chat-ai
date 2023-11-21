# inference.py
import sys
print(sys.path)

import os
from dataclasses import dataclass, asdict
from transformers import AutoConfig, AutoModelForCausalLM


@dataclass
class GenerationConfig:
    temperature: float
    top_k: int
    top_p: float
    repetition_penalty: float
    max_new_tokens: int
    seed: int
    reset: bool
    stream: bool
    threads: int
    stop: list[str]

def format_prompt(system_prompt: str, user_prompt: str):
    """format prompt based on: https://huggingface.co/spaces/mosaicml/mpt-7b-chat/blob/main/app.py"""
    system_prompt = f"system\n{system_prompt}\n"
    user_prompt = f"user\n{user_prompt}\n"
    assistant_prompt = f"assistant\n"
    return f"{system_prompt}{user_prompt}{assistant_prompt}"

def generate(llm: AutoModelForCausalLM, generation_config: GenerationConfig, system_prompt: str, user_prompt: str):
    """run model inference, will return a Generator if streaming is true"""
    return llm(
        format_prompt(
            system_prompt,
            user_prompt,
        ),
        **asdict(generation_config),
    )

def load_model_from_hub(model_name: str, trust_remote_code: bool = True):
    config = AutoConfig.from_pretrained(model_name, context_length=8192, trust_remote_code=trust_remote_code)
    llm = AutoModelForCausalLM.from_pretrained(model_name, config=config, cache_dir=True)
    return llm

if __name__ == "__main__":
    model_name = "mosaicml/mpt-7b-chat"
    llm = load_model_from_hub(model_name, trust_remote_code=True)

    system_prompt = "A conversation between a user and an LLM-based AI assistant named Local Assistant. Local Assistant gives helpful and honest answers."

    generation_config = GenerationConfig(
        temperature=0.2,
        top_k=0,
        top_p=0.9,
        repetition_penalty=1.0,
        max_new_tokens=512,  # adjust as needed
        seed=42,
        reset=False,  # reset history (cache)
        stream=True,  # streaming per word/token
        threads=int(os.cpu_count() / 2),  
        stop=["", "|<"],
    )

    user_prefix = "[user]: "
    assistant_prefix = f"[assistant]:"

    while True:
        user_prompt = input(user_prefix)
        generator = generate(llm, generation_config, system_prompt, user_prompt.strip())
        print(assistant_prefix, end=" ", flush=True)
        for word in generator:
            print(word, end="", flush=True)
        print("")
