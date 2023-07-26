const loader = document.querySelector(".loader-con");
// const loadercon = document.querySelector(".loader-con");
window.addEventListener("load", () => {
    this.setTimeout(myload, 1000)
})
function myload() {
    loader.style.display = "none";
    // loadercon.style.display = "none" 
    document.body.style.overflow = "auto";
}