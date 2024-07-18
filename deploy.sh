#!/bin/bash

# Set the paths to your Ansible playbooks and inventory file
INFRASTRUCTURE_PLAYBOOK="./prefect_infrastructure_deploy.yml"
FLOW_PLAYBOOK="./prefect_flow_deploy.yml"
INVENTORY_PATH="./inventory.ini"

# Set the SSH key path
SSH_KEY_PATH="$HOME/.ssh/cjl_rsa"

# Function to check if a file exists
check_file() {
    if [ ! -f "$1" ]; then
        echo "File not found: $1"
        exit 1
    fi
}

# Check if Ansible is installed
if ! command -v ansible &> /dev/null; then
    echo "Ansible is not installed. Please install Ansible and try again."
    exit 1
fi

# Check if required files exist
check_file "$INFRASTRUCTURE_PLAYBOOK"
check_file "$FLOW_PLAYBOOK"
check_file "$INVENTORY_PATH"
check_file "$SSH_KEY_PATH"

# Function to run Ansible playbook
run_playbook() {
    echo "Running playbook: $1"
    ansible-playbook -i "$INVENTORY_PATH" "$1" --private-key="$SSH_KEY_PATH" -u root
    if [ $? -eq 0 ]; then
        echo "Playbook completed successfully."
    else
        echo "Playbook failed. Please check the Ansible output for errors."
        exit 1
    fi
}

# Main script logic
echo "What would you like to deploy?"
echo "1. Full Prefect Infrastructure"
echo "2. Prefect Flow Only"
echo "3. Both Infrastructure and Flow"
read -p "Enter your choice (1/2/3): " choice

case $choice in
    1)
        run_playbook "$INFRASTRUCTURE_PLAYBOOK"
        ;;
    2)
        run_playbook "$FLOW_PLAYBOOK"
        ;;
    3)
        run_playbook "$INFRASTRUCTURE_PLAYBOOK"
        run_playbook "$FLOW_PLAYBOOK"
        ;;
    *)
        echo "Invalid choice. Please enter 1, 2, or 3."
        exit 1
        ;;
esac

echo "Deployment process completed."
