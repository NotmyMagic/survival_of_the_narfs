function deleteNote(narfId) {
  fetch("/delete-narf", {
    method: "POST",
    body: JSON.stringify({ narfId: narfId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}
