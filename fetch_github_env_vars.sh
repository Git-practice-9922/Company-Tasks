#!/bin/bash

# GitHub Personal Access Token
GITHUB_TOKEN="${{ secrets.GH_GITHUB_PAT }}"

# Input file containing org/repo
INPUT_FILE="${GITHUB_WORKSPACE}/repositories.txt"

# Output file for JSON data
OUTPUT_JSON="${GITHUB_WORKSPACE}/env_vars.json"

# Initialize the JSON output file
echo "[]" > $OUTPUT_JSON

# Function to fetch environments and variables for a given repo
fetch_env_vars() {
    local org_repo=$1

    echo "Fetching environments for $org_repo..."

    # Fetch environments
    environments=$(curl -s -H "Authorization: token $GITHUB_TOKEN" \
        "https://api.github.com/repos/$org_repo/environments" | jq -r '.environments[].name')

    for env in $environments; do
        echo "Fetching variables for environment $env in $org_repo..."

        # Fetch variables for each environment
        variables=$(curl -s -H "Authorization: token $GITHUB_TOKEN" \
            "https://api.github.com/repos/$org_repo/environments/$env/variables" | jq '.variables')

        # Create a JSON object for the current repo, environment, and variables
        json_obj=$(jq -n --arg org_repo "$org_repo" --arg env "$env" --argjson vars "$variables" \
            '{repository: $org_repo, environment: $env, variables: $vars}')

        # Append the JSON object to the output file
        jq --argjson new_obj "$json_obj" '. += [$new_obj]' $OUTPUT_JSON > tmp.json && mv tmp.json $OUTPUT_JSON
    done
}

# Read the input file and fetch environment variables for each repo
while IFS= read -r repo; do
    fetch_env_vars "$repo"
done < $INPUT_FILE
