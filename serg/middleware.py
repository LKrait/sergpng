# middleware.py
from .models import SiteVisit

class VisitCounterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response  # Store the next middleware or view function

    def __call__(self, request):
        # List of URLs to track
        tracked_urls = ['/', '/login/']  # Example URLs to track

        # Check if the current request path matches one of the tracked URLs
        if request.path in tracked_urls:
            try:
                # Increment the visit count only for these URLs
                visit, created = SiteVisit.objects.get_or_create(id=1)  # Ensure a single row exists
                visit.update_visit()
            except Exception as e:
                print(f"Error in VisitCounterMiddleware: {e}")
                raise e  # Raise exception again for Django to handle it
        
        # Proceed with the normal request-response cycle
        response = self.get_response(request)
        return response
