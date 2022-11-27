function $searchon()
{
    $(document).getElementById("search").style.display = "inline-block";
    $(document).getElementById("btnsearch").style.display = "none";
}
function $searchoff()
{
    $(document).getElementById("search").style.display = "none";
    $(document).getElementById("btnsearch").style.display = "inline-block";
}

const toggleButton = $(document).getElementsByClassName('toggle-button')[0]
const navbarLinks = $(document).getElementsByClassName('dropdown')[0]


toggleButton.addEventListener('click', () => {
    (navbarLinks).classList.toggle('active')
})