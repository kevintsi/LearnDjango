from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from polls.models import Question, Choice
from django.views import generic  # Import Generic Views
from django.utils import timezone


class IndexView(generic.ListView):
    # Nom du template à utiler . Par default utilise : "<app_name>/<model_name>_list.html"
    template_name = "polls/index.html"
    # Le nom de l'objet passé à la vue*
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]  # *Cet objet retourné


class DetailView(generic.DetailView):
    # Model utilisé dans la vue
    model = Question
    # Nom du template à utiler . Par default utilise : "<app_name>/<model_name>_detail.html"
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())  # __lte = less the equal to (inférieur ou égal)


class ResultsView(generic.DetailView):
    # Model utilisé dans la vue
    model = Question
    # Nom du template à utiler . Par default utilise : "<app_name>/<model_name>_detail.html"
    template_name = "polls/results.html"


def vote(request, question_id):
    print(f"Posted value : {request.POST['choice']}")
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Réaffiche le formulaire de vote
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Toujours retourne un HttpResponseRedirect après avoir réussi à traiter avec succès une donnée POST.
        # Cela empêche à la donnée d'être postée 2 fois si un utilisateur appuie sur le bouton de retour
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
