from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from polls.models import Question, Choice
from django.views import generic  # Import Generic Views


class IndexView(generic.ListView):
    # Template name to use . By default used the "<app_name>/<model_name>_list.html"
    template_name = "polls/index.html"
    # The name of the object passed to the view*
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """ Return the last five published questions. """
        return Question.objects.order_by('-pub_date')[:5]  # *This object


class DetailView(generic.DetailView):
    # Model used in the view
    model = Question
    # Template name to use . By default used the "<app_name>/<model_name>_detail.html"
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    # Model used in the view
    model = Question
    # Template name to use . By default used the "<app_name>/<model_name>_detail.html"
    template_name = "polls/results.html"


def vote(request, question_id):
    print(f"Posted value : {request.POST['choice']}")
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
