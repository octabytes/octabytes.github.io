const toggleMenu = () => {
  document.getElementById("mobile-menu").classList.toggle("hidden");
  document.getElementById("header").classList.toggle("isolate");
};

function getQueryParam(name) {
  const params = new URLSearchParams(window.location.search);
  return params.get(name);
}

window.onload = function () {
  const referralCode = getQueryParam("ref");
  if (referralCode) {
    localStorage.setItem("referral-code", referralCode);
  }
};
