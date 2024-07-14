document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('predictionForm');

    // Function to populate datalist based on entered values
    function populateDatalist(id, value) {
        const datalist = document.getElementById(id);
        const option = document.createElement('option');
        option.value = value;
        datalist.appendChild(option);
    }

    // Listen for form submission to update datalists
    form.addEventListener('submit', function(event) {
        const phValue = parseFloat(document.getElementById('id_ph').value);
        const hardnessValue = parseFloat(document.getElementById('id_hardness').value);
        const solidsValue = parseFloat(document.getElementById('id_solids').value);
        const chloraminesValue = parseFloat(document.getElementById('id_chloramines').value);
        const sulfateValue = parseFloat(document.getElementById('id_sulfate').value);
        const conductivityValue = parseFloat(document.getElementById('id_conductivity').value);
        const organicCarbonValue = parseFloat(document.getElementById('id_organic_carbon').value);
        const trihalomethanesValue = parseFloat(document.getElementById('id_trihalomethanes').value);
        const turbidityValue = parseFloat(document.getElementById('id_turbidity').value);

        // Update datalists with new values
        populateDatalist('ph-list', phValue);
        populateDatalist('hardness-list', hardnessValue);
        populateDatalist('solids-list', solidsValue);
        populateDatalist('chloramines-list', chloraminesValue);
        populateDatalist('sulfate-list', sulfateValue);
        populateDatalist('conductivity-list', conductivityValue);
        populateDatalist('organic-carbon-list', organicCarbonValue);
        populateDatalist('trihalomethanes-list', trihalomethanesValue);
        populateDatalist('turbidity-list', turbidityValue);
    });
});
