# Build the Docker image
docker build -t chatui-appi .

# Run the Docker container in detached mode
docker run -dp 8501:8501 --name contain_chatty chatui-appi

# Get the container IP address
container_ip=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' contain_chatty)
echo "Container IP Address: $container_ip"

# Open the URL in a web browser
# Note: This command may vary depending on your operating system and default web browser
# Open the URL in the default web browser based on the operating system
if [[ "$OSTYPE" == "darwin"* ]]; then
    open "http://$container_ip:8501"
elif [[ "$OSTYPE" == "linux-gnu" ]]; then
  xdg-open "http://$container_ip:8501"
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    start "http://localhost:8501"
else
    echo "Unsupported operating system"
fi

# Optionally, you can wait for a while to give the container time to start before opening the URL
sleep 10

# Display a message indicating the URL is opened
echo "Opening http://$container_ip:8501 in your default web browser..."