function loadclip() {
  const words = document.getElementById("fileLoaderBox").innerHTML;

  const load = document.getElementById("message");

  load.innerHTML = words;
  console.log(document.getElementById("fileLoaderBox").innerText);
}
