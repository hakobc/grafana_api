# set_env_vars.ps1

Write-Host "Setting environment variables based on the selected branch/environment"

$sourceBranch = "$(Build.SourceBranch)"

if ($sourceBranch -eq 'refs/heads/main') {
    [Environment]::SetEnvironmentVariable("API_URL", "$(PROD_API_URL)", "Process")
    [Environment]::SetEnvironmentVariable("API_USERNAME", "$(PROD_API_USERNAME)", "Process")
    [Environment]::SetEnvironmentVariable("API_PASSWORD", "$(PROD_API_PASSWORD)", "Process")
    [Environment]::SetEnvironmentVariable("INSTANCE_NAME", "$(PROD_INSTANCE_NAME)", "Process")
}
elseif ($sourceBranch -eq 'refs/heads/dev') {
    [Environment]::SetEnvironmentVariable("API_URL", "$(DEV_API_URL)", "Process")
    [Environment]::SetEnvironmentVariable("API_USERNAME", "$(DEV_API_USERNAME)", "Process")
    [Environment]::SetEnvironmentVariable("API_PASSWORD", "$(DEV_API_PASSWORD)", "Process")
    [Environment]::SetEnvironmentVariable("INSTANCE_NAME", "$(DEV_INSTANCE_NAME)", "Process")
}
else {
    Write-Host "Branch not mapped to a specific environment"
    # Handle other cases if needed
}

[Environment]::SetEnvironmentVariable("ENDPOINT", "$(Endpoint)", "Process")
[Environment]::SetEnvironmentVariable("SELECTED_OPERATION", "$(Operation)", "Process")

python api_call.py
