import os

exit_code = os.system("python manage.py test")

if exit_code != 0:
    os.system("git bisect start HEAD e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c")
    os.system("git bisect run python manage.py test")
