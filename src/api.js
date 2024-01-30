export function fetchDataFromFastAPI() {
// Make a GET request to the FastAPI endpoint
    return fetch('http://localhost:8000/')
        .then(response => {
            // Check if the request was successful (status code 200)
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }

            // Parse the response as JSON
            return response.json().then(data => data.message);
        })
        .catch(error => {
            // Handle errors
            console.error('Error:', error);
            return null; // Return null or any default value in case of an error
        });
}


export function genereateOdds(h1c1, h1c2, h2c1, h2c2) {
    const hand_1 = [h1c1, h1c2]
    const hand_2 = [h2c1, h2c2]

    const hands_payload = {
        hand_1: hand_1,
        hand_2: hand_2
    }

    return fetch('http://localhost:8000/evaluate_hands' ,{
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(hands_payload)
    })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json().then(data => data.data)
        })
}