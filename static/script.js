document.addEventListener('DOMContentLoaded', function () {
  const pwd = document.getElementById('password');
  const toggle = document.getElementById('show-password');

  toggle.addEventListener('change', function () {
    pwd.type = this.checked ? 'text' : 'password';
  });
});

