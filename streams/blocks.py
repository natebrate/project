"""Add your blocks here"""
from wagtail.core import blocks
from wagtail.core.templatetags.wagtailcore_tags import richtext
from wagtail.images.blocks import ImageChooserBlock


class TitleAndTextBlocks(blocks.StructBlock):
    title = blocks.CharBlock(required=True, help_text="Add Your Title")

    stuff = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
            ]
        )
    )

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title and Text"


class CardBlock(blocks.StructBlock):
    """Card with image, text and buttons"""
    title = blocks.CharBlock(required=True, help_text="Add Your Title")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )

    class Meta:  # noqa
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Product Cards"


class RichtextBlock(blocks.RichTextBlock):
    """Richtext with all the features."""

    def get_api_representation(self, value, context=None):
        return richtext(value.source)

    class Meta:  # noqa
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"


class SimpleRichtextBlock(blocks.RichTextBlock):
    """Richtext without (limited) all the features."""

    def __init__(
            self, required=True, help_text=None, editor="default", features=None, **kwargs
    ):  # noqa
        super().__init__(**kwargs)
        self.features = ["bold", "italic", "link"]

    class Meta:  # noqa
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Simple RichText"


class CTABlock(blocks.StructBlock):
    """A simple call to action section."""

    title = blocks.CharBlock(required=True, max_length=60)
    text = blocks.RichTextBlock(required=True, features=["bold", "italic"])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=True, default='Learn More', max_length=40)

    class Meta:  # noqa
        template = "streams/cta_block.html"
        icon = "placeholder"
        label = "Call to Action"


class LinkStructValue(blocks.StructValue):
    """Add more logic for urls"""

    def url(self):
        button_page = self.get('button_page')
        button_url = self.get('button_url')
        if button_page:
            return button_page.url
        elif button_url:
            return button_url
        return None


class ButtonBlock(blocks.StructBlock):
    """Link to external page"""
    button_page = blocks.PageChooserBlock(required=False, help_text="If selected, this url will be used first")
    button_url = blocks.URLBlock(required=False, help_text="If selected, this url will be used secondarily")

    class Meta:  # noqa
        template = "streams/button_block.html"
        icon = "placeholder"
        label = "Button Chooser"
        value_class = LinkStructValue


class IntroBlock(blocks.StructBlock):
    banner_title = blocks.CharBlock(max_length=200, default="Welcome to the store")
    intro = blocks.TextBlock(blank=True, max_length=500)

    class Meta:
        template = "streams/intro_block.html"
        icon = "Edit Body"
        label = "Introduction Body"


class BodyBlock(blocks.StructBlock):
    heading = blocks.RichTextBlock(required=True, help_text="Add Your Heading")
    image = ImageChooserBlock(required=False, help_text="Add Your Image")
    paragraph = blocks.RichTextBlock(required=True, max_length=40, help_text="Add Your Paragraph")

    class Meta:
        template = "streams/body_block.html"
        icon = "Edit Body"
        label = "Store Body"


class FoodBlocks(blocks.StructBlock):
    """Card with image, text and buttons"""
    title = blocks.CharBlock(required=True, help_text="Add Your Title")

    foodCard = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=False)),
                ("title", blocks.TextBlock(required=True, max_length=200)),
                ("text", blocks.RichTextBlock(required=True, max_length=200)),
                ("Price", blocks.FloatBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                (
                    "button_url",
                    blocks.URLBlock(
                        required=False,
                        help_text="If the button page above is selected, that will be used first.",  # noqa
                    ),
                ),
            ]
        )
    )

    class Meta:  # noqa
        template = "streams/food_block.html"
        icon = "placeholder"
        label = "Product Cards"
