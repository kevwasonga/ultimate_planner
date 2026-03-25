from .models import Review, Inquiry

def create_review(professional, client_name, rating, comment, is_approved=False):
    """
    Service to create a professional review with optional approval logic.
    """
    review = Review.objects.create(
        professional=professional,
        client_name=client_name,
        rating=rating,
        comment=comment,
        is_approved=is_approved
    )
    return review

def process_inquiry(inquiry_id, status='contacted', admin_notes=None):
    """
    Service to update/process an inquiry.
    """
    inquiry = Inquiry.objects.get(id=inquiry_id)
    inquiry.status = status
    if admin_notes:
        inquiry.admin_notes = admin_notes
    inquiry.save()
    return inquiry
