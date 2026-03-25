from django.contrib import admin
from django.utils.html import format_html
from django.db.models import Count, Avg
from django.utils import timezone
from .models import Category, Professional, Review, Inquiry, SiteStats


# ── Category Admin ────────────────────────────────────────────────────────────

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('icon', 'name', 'slug', 'professional_count', 'color_preview')
    list_display_links = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

    def professional_count(self, obj):
        count = obj.professionals.count()
        return format_html('<strong>{}</strong> professionals', count)
    professional_count.short_description = 'Professionals'

    def color_preview(self, obj):
        return format_html(
            '<span style="display:inline-block;width:24px;height:24px;'
            'background:{};border-radius:4px;border:1px solid #ddd;"></span>',
            obj.color
        )
    color_preview.short_description = 'Color'


# ── Review Inline ─────────────────────────────────────────────────────────────

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0
    fields = ('client_name', 'rating', 'comment', 'is_approved', 'created_at')
    readonly_fields = ('created_at',)
    show_change_link = True


# ── Professional Admin ────────────────────────────────────────────────────────

@admin.register(Professional)
class ProfessionalAdmin(admin.ModelAdmin):
    list_display = (
        'avatar_display', 'name', 'category', 'location',
        'availability_badge', 'is_verified', 'is_featured',
        'avg_rating', 'projects_completed', 'created_at'
    )
    list_display_links = ('name',)
    list_filter = ('category', 'availability', 'is_verified', 'is_featured', 'location')
    search_fields = ('name', 'specialty', 'email', 'phone', 'location')
    list_editable = ('is_verified', 'is_featured')
    readonly_fields = ('created_at', 'updated_at', 'initials_display', 'avg_rating', 'review_count_display')
    inlines = [ReviewInline]
    date_hierarchy = 'created_at'

    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'photo', 'initials_display', 'email', 'phone', 'website')
        }),
        ('Professional Details', {
            'fields': ('category', 'specialty', 'location', 'bio', 'experience_years', 'price_per_hour', 'projects_completed')
        }),
        ('Status', {
            'fields': ('availability', 'is_verified', 'is_featured'),
            'classes': ('wide',)
        }),
        ('Statistics', {
            'fields': ('avg_rating', 'review_count_display', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def avatar_display(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="width:36px;height:36px;border-radius:50%;object-fit:cover;">', obj.photo.url)
        return format_html(
            '<div style="width:36px;height:36px;border-radius:50%;background:#C8860A;'
            'color:#0F1410;display:flex;align-items:center;justify-content:center;'
            'font-weight:900;font-size:12px;font-family:serif;">{}</div>',
            obj.initials
        )
    avatar_display.short_description = ''

    def availability_badge(self, obj):
        colors = {'available': '#10B981', 'busy': '#F59E0B', 'unavailable': '#EF4444'}
        color = colors.get(obj.availability, '#6B7280')
        return format_html(
            '<span style="background:{};color:white;padding:2px 8px;'
            'border-radius:12px;font-size:11px;font-weight:600;">{}</span>',
            color, obj.get_availability_display()
        )
    availability_badge.short_description = 'Status'

    def verified_badge(self, obj):
        if obj.is_verified:
            return format_html('<span style="color:#10B981;font-size:16px;" title="Verified">✓</span>')
        return format_html('<span style="color:#D1D5DB;font-size:16px;" title="Not verified">○</span>')
    verified_badge.short_description = '✓'

    def featured_badge(self, obj):
        if obj.is_featured:
            return format_html('<span style="color:#F59E0B;font-size:16px;" title="Featured">★</span>')
        return format_html('<span style="color:#D1D5DB;font-size:16px;" title="Not featured">☆</span>')
    featured_badge.short_description = '★'

    def avg_rating(self, obj):
        rating = obj.average_rating
        if rating:
            stars = '★' * int(rating) + '☆' * (5 - int(rating))
            return format_html('<span style="color:#F59E0B;">{}</span> <strong>{}</strong>', stars, rating)
        return '—'
    avg_rating.short_description = 'Rating'

    def review_count_display(self, obj):
        return obj.review_count
    review_count_display.short_description = 'Reviews'

    def initials_display(self, obj):
        return format_html(
            '<div style="width:60px;height:60px;border-radius:50%;background:#C8860A;'
            'color:#0F1410;display:flex;align-items:center;justify-content:center;'
            'font-weight:900;font-size:18px;font-family:serif;">{}</div>',
            obj.initials
        )
    initials_display.short_description = 'Avatar'

    actions = ['mark_verified', 'mark_featured', 'mark_available']

    def mark_verified(self, request, queryset):
        updated = queryset.update(is_verified=True)
        self.message_user(request, f'{updated} professional(s) marked as verified.')
    mark_verified.short_description = '✓ Mark selected as Verified'

    def mark_featured(self, request, queryset):
        updated = queryset.update(is_featured=True)
        self.message_user(request, f'{updated} professional(s) marked as featured.')
    mark_featured.short_description = '★ Mark selected as Featured'

    def mark_available(self, request, queryset):
        updated = queryset.update(availability='available')
        self.message_user(request, f'{updated} professional(s) marked as available.')
    mark_available.short_description = '✅ Set availability to Available'


# ── Review Admin ──────────────────────────────────────────────────────────────

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'professional', 'star_rating', 'is_approved', 'created_at')
    list_filter = ('rating', 'is_approved', 'professional__category')
    search_fields = ('client_name', 'comment', 'professional__name')
    list_editable = ('is_approved',)
    date_hierarchy = 'created_at'

    def star_rating(self, obj):
        stars = '★' * obj.rating + '☆' * (5 - obj.rating)
        colors = {1: '#EF4444', 2: '#F97316', 3: '#F59E0B', 4: '#84CC16', 5: '#10B981'}
        return format_html('<span style="color:{};">{}</span>', colors.get(obj.rating, '#F59E0B'), stars)
    star_rating.short_description = 'Rating'

    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        updated = queryset.update(is_approved=True)
        self.message_user(request, f'{updated} review(s) approved.')
    approve_reviews.short_description = '✓ Approve selected reviews'


# ── Inquiry Admin ─────────────────────────────────────────────────────────────

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'email', 'phone', 'service_category',
        'status', 'assigned_to', 'created_at'
    )
    list_filter = ('status', 'service_category', 'created_at')
    search_fields = ('name', 'email', 'phone', 'message')
    list_editable = ('status', 'assigned_to')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'created_at'

    fieldsets = (
        ('Client Information', {
            'fields': ('name', 'email', 'phone', 'location')
        }),
        ('Inquiry Details', {
            'fields': ('service_category', 'message', 'created_at', 'updated_at')
        }),
        ('Management', {
            'fields': ('status', 'assigned_to', 'admin_notes'),
            'classes': ('wide',)
        }),
    )

    def status_badge(self, obj):
        colors = {
            'new': '#3B82F6',
            'contacted': '#8B5CF6',
            'in_progress': '#F59E0B',
            'resolved': '#10B981',
            'closed': '#6B7280',
        }
        color = colors.get(obj.status, '#6B7280')
        return format_html(
            '<span style="background:{};color:white;padding:3px 10px;'
            'border-radius:12px;font-size:11px;font-weight:600;">{}</span>',
            color, obj.get_status_display()
        )
    status_badge.short_description = 'Status'

    actions = ['mark_contacted', 'mark_resolved']

    def mark_contacted(self, request, queryset):
        queryset.update(status='contacted')
        self.message_user(request, f'Inquiries marked as Contacted.')
    mark_contacted.short_description = 'Mark as Contacted'

    def mark_resolved(self, request, queryset):
        queryset.update(status='resolved')
        self.message_user(request, f'Inquiries marked as Resolved.')
    mark_resolved.short_description = '✓ Mark as Resolved'


# ── Site Settings Admin ───────────────────────────────────────────────────────

@admin.register(SiteStats)
class SiteStatsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SiteStats.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
