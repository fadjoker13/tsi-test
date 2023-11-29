// function getPlayersList() {
//     fetch('http://localhost:8000')
//         .then(response => response.json())
//         .then(data => {
//             console.log("Données de l'API :", data);
//             var celluleNom = document.querySelector('.nameplayer');
//             if (celluleNom && data.length > 0) {
//                 var nameFirstPlayer = data[0].name;
//                 celluleNom.textContent = nameFirstPlayer;
//                 console.log("Name of Player:", nameFirstPlayer);
//             } else {
//                 console.error("Player not found");
//             }
//         })
//         .catch(error => {
//             console.error("Erreur lors de la récupération des joueurs:", error);
//         });   
// }
// getPlayersList();

function getNomsDesJoueurs() {
    fetch('http://127.0.0.1:8000/api/players/')
    .then(response => response.json())
    .then(data => {
    console.log("Fonction called");
    var NamePlayer = document.querySelectorAll(".nameplayer");
    if (NamePlayer.length > 0) {
        NamePlayer.forEach(function (element) {
            var nomDuJoueur = element.textContent;
            console.log('Nom du joueur :', nomDuJoueur);
        });
    } else {
        console.error('Classe non trouvée.');
    }})
    .catch(error => {
            console.error("Erreur lors de la récupération des joueurs:", error);
        });   
}
getNomsDesJoueurs();

function getPlayersList() {
    console.log("Fonction called");
    var NamePlayer = document.querySelectorAll(".nameplayer");
    if (NamePlayer.length > 0) {
        NamePlayer.forEach(function (element) {
            var nomDuJoueur = element.textContent;
            console.log('Name of Player:', nomDuJoueur);
        });
    } else {
        console.error('Player Not Found');
    }
}
getPlayersList();