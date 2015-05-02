from django.shortcuts import render
from comments.forms import AddCommentForm


def add(request):
    valid = ""
    if request.method == 'POST':
        form = AddCommentForm(request.POST)

        if form.is_valid():
            form.save()
            valid = "ok"
        else:
            valid = "ko"
    else:
        form = AddCommentForm()

    return render(request, 'recipe/show.html', {'form': form, 'validation': valid})


