//const vehicleModelInfo = document.querySelectorAll(".vehicleModelInfo");
//const engineModelInfo = document.querySelectorAll(".engineModelInfo");
//const transmissionModelInfo = document.querySelectorAll(".transmissionModelInfo");


const closeInfoPanelButton = document.querySelector("#closeInfoPanel");
closeInfoPanelButton.addEventListener("click", function() {
    document.querySelector('.showInfo').style.display = "none";
});

function Info(id, nameInfo, urlInfo, tableName) {
    document.querySelector('#tableName').textContent = `'${tableName}'`;
    document.querySelector('.showInfo').style.display = "block";

    const url = `http://127.0.0.1:8000/api/catalog/${urlInfo}/${id}/`

    fetch(url)
    .then((response) => {
        const result = response.json()
        return result;
    })
    .then((result) => {

        let results_id = new Map(Object.entries(result));
        let results_name = new Map(Object.entries(result));
        let results_description = new Map(Object.entries(result));

        document.querySelector(".id").textContent = results_id.get('id');
        document.querySelector(".name").textContent = results_name.get('name');
        document.querySelector(".description").textContent = results_description.get('description');
    })
}

