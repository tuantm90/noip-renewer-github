import os

# Number of scripts to generate
num_scripts = 100
lines_per_script = 1

# Directory to save scripts
output_dir = 'scripts'
os.makedirs(output_dir, exist_ok=True)

for chunk in range(1, num_scripts + 1):
    start = (chunk - 1) * lines_per_script + 1
    end = start + lines_per_script - 1
    
    # Initialize a variable to store the script content
    script_content = "#!/bin/bash\n"
    
    for i in range(start, end + 1):
        username_var = f"NO_IP_USERNAME_{i}"
        password_var = f"NO_IP_PASSWORD_{i}"
        totp_key_var = f"NO_IP_TOTP_KEY_{i}"

        script_content += 'username' + str(i) + '="${{ secrets.' + username_var + ' }}"\n'
        script_content += 'password' + str(i) + '="${{ secrets.' + password_var + ' }}"\n'
        script_content += 'totp_key' + str(i) + '="${{ secrets.' + totp_key_var + ' }}"\n\n'

        script_content += 'if [ -n "$username' + str(i) + '" ] && [ -n "$password' + str(i) + '" ] && [ -n "$totp_key' + str(i) + '" ]; then\n'
        script_content += '  echo "Processing account ' + str(i) + ': $username' + str(i) + '"\n'
        script_content += '  docker run --rm \\\n'
        script_content += '    --env NO_IP_USERNAME="$username' + str(i) + '" \\\n'
        script_content += '    --env NO_IP_PASSWORD="$password' + str(i) + '" \\\n'
        script_content += '    --env NO_IP_TOTP_KEY="$totp_key' + str(i) + '" \\\n'
        script_content += '    simaofsilva/noip-renewer:latest\n'
        script_content += 'fi\n\n'
    
    # Write the accumulated content to the script file
    script_file = os.path.join(output_dir, f'script_chunk_{chunk}.sh')
    with open(script_file, 'w') as f:
        f.write(script_content)
