document.getElementById('signupForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    const firstName = formData.get('firstName');
    const lastName = formData.get('lastName');
    const email = formData.get('email');
    const password = formData.get('password');
    const confirmPassword = formData.get('confirmPassword');
    
    if (password !== confirmPassword) {
        document.getElementById('error-msg').textContent = 'Passwords do not match';
        return;
    }
    
    try {
        const response = await fetch('/signup', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ firstName, lastName, email, password })
        });
        
        if (response.ok) {
            window.location.href = '/login';
        } else {
            const errorMsg = await response.text();
            document.getElementById('error-msg').textContent = errorMsg;
        }
    } catch (error) {
        console.error('Error:', error);
    }
});
