let xhr = new XMLHttpRequest();
let Name = document.querySelector(".text_button");
let Size = document.querySelector(".size");
let bar = document.querySelector("#progressBar");
bar.value;
let inptAddImg = document
  .querySelector("#add_image")
  .addEventListener("change", () => {
    let preview = document.querySelector("#img_file");
    let file = document.querySelector("#add_image").files[0];
    let reader = new FileReader();

    xhr.upload.addEventListener("progress", function (event) {
      var percent = (event.loaded / event.total) * 100;

      bar.value = percent;
    });

    xhr.upload.addEventListener("loadend", function () {
      Name.style.color = "#3CA255";
      Size.style.color = "#3CA255";
      document.querySelector(".button_add path").style.fill = "#3CA255";
    });

    reader.onloadend = function () {
      preview.src = reader.result;
    };

    if (file) {
      reader.readAsDataURL(file);
      Name.textContent = file.name;
      Size.textContent = Math.round(file.size / 1024) + "[KB]";
    } else {
      preview.src = "";
    }

    xhr.open("POST", "https://isidea.ru/rgups_file.php", true);
    xhr.send(file);
  });
