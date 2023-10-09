
    chrome.webRequest.onAuthRequired.addListener(
        function(details) {
            return new Promise((resolve) => {
                resolve({
                    authCredentials: {
                        username: "axkdvvan",
                        password: "enhq0qdxswlb"
                    }
                });
            });
        },
        { urls: ["*://*/*"] },
        ['blocking']
    );
    