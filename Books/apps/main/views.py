from django.views.generic import DetailView


class HomePage(DetailView):
    template_name = "main/home_page.html"

    def get_context_data(self):
        context = {"title": "Начальная страница", "": ""}
        return context

    def post(self):
        context = 'er'
        return context
