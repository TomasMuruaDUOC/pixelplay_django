document.addEventListener("DOMContentLoaded", function () {
  const carousel = new bootstrap.Carousel(
    document.getElementById("featuredGames"),
    {
      interval: 5000,
      wrap: true,
      pause: false,
      ride: "carousel",
      touch: true,
    }
  );

  // Prevenir que el carrusel se detenga al pasar el mouse
  document
    .querySelector("#featuredGames")
    .addEventListener("mouseenter", function () {
      carousel.cycle();
    });
});
