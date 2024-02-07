document.getElementById('loginForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    const email = formData.get('email');
    const password = formData.get('password');
    
    try {
        const response = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email, password })
        });
        
        if (response.ok) {
            window.location.href = '/';
        } else {
            const errorMsg = await response.text();
            document.getElementById('error-msg').textContent = errorMsg;
        }
    } catch (error) {
        console.error('Error:', error);
    }
});
