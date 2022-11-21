<!DOCTYPE html>
<html>

<head>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous" />
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
</head>

<body>
    <div class="bg-container text-center d-flex flex-column justify-content-center">
        <h1 class="counter-heading">Counter</h1>
        <p id="countervalue" class="counter-value">0</p>
        <div>
            <button onclick="onDc()" class="button">DECREASE</button>
            <button onclick="onRs()" class="button">RESET</button>
            <button onclick="onInc()" class="button">INCREASE</button>
        </div>
    </div>
</body>
</html>


css...........................................

@import url("https://fonts.googleapis.com/css2?family=Bree+Serif&family=Caveat:wght@400;700&family=Lobster&family=Monoton&family=Open+Sans:ital,wght@0,400;0,700;1,400;1,700&family=Playfair+Display+SC:ital,wght@0,400;0,700;1,700&family=Playfair+Display:ital,wght@0,400;0,700;1,700&family=Roboto:ital,wght@0,400;0,700;1,400;1,700&family=Source+Sans+Pro:ital,wght@0,400;0,700;1,700&family=Work+Sans:ital,wght@0,400;0,700;1,700&display=swap");

.bg-container {
    height: 100vh;
    background-color: #f1f5f8;
}

.counter-heading {
    font-size: 50px;
    font-family: "Roboto";
    font-weight: 800;
}

.counter-value {
    font-size: 75px;
    font-weight: 900;
}

.button {
    margin: 8px;
    border-radius: 8px;
    padding: 5px;
    border-width: 2px;
    border-color: black;
    background-color: #f1f5f8;
}


js.......................................................


let c = document.getElementById("countervalue");

function onDc() {
    let a = c.textContent;
    let b = parseInt(a) - 1;
    c.textContent = b;
    if (b < 0) {
        c.style.color = "red"
    } 
    else if (b > 0) {
        c.style.color = "green"
    } 
    else {
        c.style.color = "black"
    }


}

function onRs() {
    let a = 0;
    let b = parseInt(a);
    c.textContent = b;
    if (b < 0) {
        c.style.color = "red"
    } 
    else if (b > 0) {
        c.style.color = "green"
    } 
    else {
        c.style.color = "black"
    }
}

function onInc() {
    let a = c.textContent;
    let b = parseInt(a) + 1;
    c.textContent = b;
    if (b < 0) {
        c.style.color = "red"
    } 
    else if (b > 0) {
        c.style.color = "green"
    } 
    else {
        c.style.color = "black"
    }
}
