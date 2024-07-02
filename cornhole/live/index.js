let redScore = 0;
let blueScore = 0;
const MAX_SCORE = 21;
const RESET_SCORE = 15;

function incrementScore(team) {
    if (team === 'red') {
        redScore++;
        if (redScore > MAX_SCORE) {
            redScore = RESET_SCORE;
        }
        document.getElementById('redScore').textContent = redScore;
    } else if (team === 'blue') {
        blueScore++;
        if (blueScore > MAX_SCORE) {
            blueScore = RESET_SCORE;
        }
        document.getElementById('blueScore').textContent = blueScore;
    }
}
