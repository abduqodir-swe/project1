console.log("Django Static Js dan salom!");

const button = document.querySelector("#hello-button");

if (button) {
    button.addEventListener("click", () => {
        alert("Django Static JS Button!");
    });
}
