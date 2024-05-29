from social_core.pipeline.user import get_username
from social_core.pipeline.social_auth import social_user


def get_vk_avatar(strategy, details, response, social, user, *args, **kwargs):
    url = None
    if social.provider == 'vk-oauth2' and response.get('photo_max_orig'):
        url = response['photo_max_orig']
    if url and user and not user.avatar:
        user.avatar = url
        user.save()


SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'your_project_name.social_pipeline.get_vk_avatar',  # Replace 'your_project_name' with your Django project name
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)
