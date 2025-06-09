from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def logo_orb(content, href="#", size="medium"):
    size_classes = {
        "small": "tw-h-12 tw-w-12",
        "medium": "tw-h-24 tw-w-24",
        "large": "tw-h-32 tw-w-32",
    }

    img_size_px = {
        "small": 48,
        "medium": 96,
        "large": 144,
    }

    orb_size = size_classes.get(size, size_classes["medium"])
    img_size = img_size_px.get(size, img_size_px["medium"])
    img_w = int(img_size * 0.6)
    img_h = int(img_size * 0.6)

    # Inline style for image wrapper
    content_html = f'<div style="width: {img_w}px; height: {img_h}px;">{content}</div>'

    html = f"""
      <a href="/about-us/" class="tw-transition-transform tw-duration-300 tw-ease-in-out tw-transform tw-hover:scale-110 tw-animate-spin">
        <div class="tw-relative">
        <div class="tw-orb-before"></div>
             <div class="tw-flex {orb_size} tw-items-center tw-justify-center tw-rounded-full tw-bg-white tw-shadow-lg tw-relative tw-z-10">
                <div class="tw-absolute tw-inset-0 tw-m-[8.334%] tw-rounded-full tw-border tw-border-gray-700/5 tw-bg-gray-300/60 tw-[mask-image:linear-gradient(to_bottom,black,transparent)]"></div>
                <div class="tw-relative tw-z-10 tw-text-center">
                  {content_html}
                </div>
            </div>      
          </div>
        </div>  
      </a>
    </div>
  """

    return mark_safe(html)

#            <div class="animate-[breath_8s_ease-in-out_infinite_both]">    </div>
#                  <div class="absolute inset-0 m-[8.334%] rounded-full border border-gray-700/5 bg-gray-700/70 [mask-image:radial-gradient(black,transparent)]"></div>   
#       <a href="{href}" class="tw-relative tw-group tw-block tw-transition-transform tw-hover:scale-105">



#  {% load logo_orb %}

#  <!-- Image version -->
#                    {% load static logo_orb %}
#                    {% static 'img/shapes/logo-01.svg' as logo_path %}
#                    {% with '<img src="'|add:logo_path|add:'" alt="Logo" class="rounded-full w-8 h-8">' as logo_img %}
#                      {% logo_orb logo_img href='/about/' size='medium' %}
#                    {% endwith %}
#  <!-- Text version -->
#  {% logo_orb 'Go' href='/pricing/' size='medium' %}
#    {% logo_orb "?" href="/faq/" size="small" %}
#    {% logo_orb "🛠️" href="/tools/" size="medium" %}

#  <!-- Large image -->
#  {% logo_orb '<img src="'|add:static('images/github-icon.svg')|add:'" width="40" height="40" alt="GitHub">' href='https://github.com/' size='large' %}


