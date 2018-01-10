from django import template
register = template.Library()

@register.inclusion_tag('friends/_feed.html')
def recipe_feed(following):
    """takes a user someone is following  and returns the last 5 recipes added"""
    recipes = following.recipe_set.filter(shared=0).order_by('-pub_date')[0:5]
    return {'recipes':recipes, 'following':following}

@register.inclusion_tag('friends/_feed.html')
def rate_feed(following):
    """returns the last five recipes a friend has voted on"""
    rated = following.votes.order_by('-date_changed')
    return{'rated':rated, 'following':following}

