// This function toggles the visibility of the search icon on mobile devices.
const toggleSearchIcon = () => {
  const searchIcon = document.querySelector('.search-icon-container');
  if (searchIcon.classList.contains('d-none')) {
    searchIcon.classList.remove('d-none');
  } else {
    searchIcon.classList.add('d-none');
  }
}


// This function toggles the visibility of the search box on mobile devices.
const toggleSearchBox = () => {
  const searchBox = document.querySelector('.mobile-search-input');
  if (searchBox.classList.contains('d-none')) {
    searchBox.classList.remove('d-none');
  } else {
    searchBox.classList.add('d-none');
  }
} 


// This function toggles the visibility of the user settings dropdown on mobile devices.
const toggleUserSetting = () => {
  const container = document.querySelector('.dropdown');
  if (container.classList.contains('d-none')) {
    container.classList.remove('d-none')
  } else {
    container.classList.add('d-none');
  }
}



// add click event listeners to the task content container
document.addEventListener("DOMContentLoaded", function() {
  const containers = document.querySelectorAll(".tasks-wrapper");
  containers.forEach(container => {
    container.addEventListener("click", function() {
      const url = this.getAttribute("data-href");
      if (url) {
        window.location.href = url;
      }
    });
  });
});


// task tabs
const tabs = document.querySelectorAll('.task-tab');
  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
    });
  });