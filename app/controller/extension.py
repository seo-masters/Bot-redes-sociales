import os
import zipfile

def create_proxy_extension(proxy_host, proxy_port, username, password, output_directory):
    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 3,
        "name": "Chrome Proxy",
        "permissions": [
            "webRequest",
            "webRequestBlocking"
        ],
        "host_permissions": ["<all_urls>"],
        "background": {
            "service_worker": "background.js"
        }
    }
    """

    background_js = f"""
    chrome.webRequest.onAuthRequired.addListener(
        function(details) {{
            return new Promise((resolve) => {{
                resolve({{
                    authCredentials: {{
                        username: "{username}",
                        password: "{password}"
                    }}
                }});
            }});
        }},
        {{ urls: ["*://*/*"] }},
        ['blocking']
    );
    """

    os.makedirs(output_directory, exist_ok=True)
    with open(os.path.join(output_directory, "manifest.json"), "w") as manifest_file:
        manifest_file.write(manifest_json)
    with open(os.path.join(output_directory, "background.js"), "w") as background_file:
        background_file.write(background_js)

    with zipfile.ZipFile(os.path.join(output_directory, "proxy_auth_extension.zip"), "w") as zipped:
        zipped.write(os.path.join(output_directory, "manifest.json"), "manifest.json")
        zipped.write(os.path.join(output_directory, "background.js"), "background.js")

