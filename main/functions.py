from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



def generate_form_errors(form):
    message = ""
    for field in form:
        if field.errors:
                message += field.errors
    for error in form.non_field_errors():
         message += str(error)

    return message
    

def paginate_instances(request, instances, per_page=9):
    instances = Paginator(instances, per_page)
    page = request.GET.get('page', 1)

    try:
        instances = instances.page(page)
    except PageNotAnInteger:
        instances = instances.page(1)
    except EmptyPage:
        instances = instances.page(instances.num_pages)

    return instances
