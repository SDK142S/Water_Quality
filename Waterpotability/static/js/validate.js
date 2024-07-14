document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('predictionForm');
    form.addEventListener('submit', function(event) {
        const limits = {
            'ph': [0.00, 14.00],
            'hardness': [47.43, 323.12],
            'solids': [320.94, 61227.20],
            'chloramines': [0.35, 13.13],
            'sulfate': [129.00, 481.03],
            'conductivity': [181.48, 753.34],
            'organic_carbon': [2.20, 28.30],
            'trihalomethanes': [0.74, 124.00],
            'turbidity': [1.45, 6.74]
        };

        let valid = true;

        // Check each input field
        Object.keys(limits).forEach(key => {
            const input = document.getElementById('id_' + key);
            const value = parseFloat(input.value);

            // Check if value is empty or exceeds limits
            if (isNaN(value) || value < limits[key][0] || value > limits[key][1]) {
                valid = false;
                input.classList.add('error-input');
                document.getElementById(key + '-error').innerText = `Please enter a valid value (${limits[key][0]} - ${limits[key][1]})`;
            } else {
                input.classList.remove('error-input');
                document.getElementById(key + '-error').innerText = '';
            }
        });

        if (!valid) {
            event.preventDefault();
            alert('Please correct the errors before submitting.');
        }
    });
});
