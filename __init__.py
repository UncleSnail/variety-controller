# A Mycroft skill for controlling the desktop through Variety
# Copyright (C) 2018  Uncle Snail

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.



# Import statements: the list of outside modules you'll be using in your
# skills, whether from other files in mycroft-core or from external libraries
from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
import subprocess

__author__ = 'UncleSnail'

# Logger: used for debug lines, like "LOGGER.debug(xyz)". These
# statements will show up in the command line when running Mycroft.
LOGGER = getLogger(__name__)

# The logic of each skill is contained within its own class, which inherits
# base methods from the MycroftSkill class with the syntax you can see below:
# "class ____Skill(MycroftSkill)"
class VarietyController(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(VarietyController, self).__init__(name="Variety Controller")

    # This method loads the files needed for the skill's functioning, and
    # creates and registers each intent that the skill uses
    def initialize(self):
        self.load_data_files(dirname(__file__))

        #IntentBuilders
        #For background images

        next_intent = IntentBuilder("NextIntent").\
            require("WallpaperKeyword").require("NextKeyword").build()
        self.register_intent(next_intent, self.handle_next_intent)

        previous_intent = IntentBuilder("PreviousIntent").\
            require("WallpaperKeyword").require("PreviousKeyword").build()
        self.register_intent(previous_intent,
                             self.handle_previous_intent)

        pause_intent = IntentBuilder("PauseIntent").\
            require("WallpaperKeyword").require("PauseKeyword").build()
        self.register_intent(pause_intent,
                             self.handle_pause_intent)

        resume_intent = IntentBuilder("ResumeIntent").\
            require("WallpaperKeyword").require("ResumeKeyword").build()
        self.register_intent(resume_intent,
                             self.handle_resume_intent)

        toggle_intent = IntentBuilder("ToggleIntent").\
            require("WallpaperKeyword").require("ToggleKeyword").build()
        self.register_intent(toggle_intent,
                             self.handle_toggle_intent)

        fast_intent = IntentBuilder("FastIntent").\
            require("WallpaperKeyword").require("FastKeyword").build()
        self.register_intent(fast_intent,
                             self.handle_fast_intent)

        favorite_intent = IntentBuilder("FavoriteIntent").\
            require("WallpaperKeyword").require("FavoriteKeyword").build()
        self.register_intent(favorite_intent,
                             self.handle_favorite_intent)

        trash_intent = IntentBuilder("TrashIntent").\
             require("WallpaperKeyword").require("TrashKeyword").build()
        self.register_intent(trash_intent,
                             self.handle_trash_intent)

        #For background quotes

        next_quote_intent = IntentBuilder("NextQuoteIntent").\
            require("QuoteKeyword").require("NextKeyword").build()
        self.register_intent(next_quote_intent, self.handle_next_quote_intent)

        previous_quote_intent = IntentBuilder("PreviousQuoteIntent").\
            require("QuoteKeyword").require("PreviousKeyword").build()
        self.register_intent(previous_quote_intent,
                             self.handle_previous_quote_intent)

        toggle_quote_intent = IntentBuilder("ToggleQuoteIntent").\
            require("QuoteKeyword").require("ToggleKeyword").build()
        self.register_intent(toggle_quote_intent,
                             self.handle_toggle_quote_intent)

        fast_quote_intent = IntentBuilder("FastQuoteIntent").\
            require("QuoteKeyword").require("FastKeyword").build()
        self.register_intent(fast_quote_intent,
                             self.handle_fast_quote_intent)

        favorite_quote_intent = IntentBuilder("FavoriteQuoteIntent").\
            require("QuoteKeyword").require("FavoriteKeyword").build()
        self.register_intent(favorite_quote_intent,
                             self.handle_favorite_quote_intent)

        #For Variety interface

        version_intent = IntentBuilder("VersionIntent").\
            require("VarietyKeyword").require("VersionKeyword").build()
        self.register_intent(version_intent,
                             self.handle_version_intent)

        preferences_intent = IntentBuilder("PreferencesIntent").\
            require("VarietyKeyword").require("PreferencesKeyword").build()
        self.register_intent(preferences_intent,
                             self.handle_preferences_intent)

        quit_intent = IntentBuilder("QuitIntent").\
            require("VarietyKeyword").require("QuitKeyword").build()
        self.register_intent(quit_intent,
                             self.handle_quit_intent)

        history_intent = IntentBuilder("HistoryIntent").\
            require("WallpaperKeyword").require("HistoryKeyword").build()
        self.register_intent(history_intent,
                             self.handle_history_intent)

        downloads_intent = IntentBuilder("DownloadsIntent").\
            require("VarietyKeyword").require("DownloadsKeyword").build()
        self.register_intent(downloads_intent,
                             self.handle_downloads_intent)

        selector_intent = IntentBuilder("SelectorIntent").\
            require("VarietyKeyword").require("SelectorKeyword").build()
        self.register_intent(selector_intent,
                             self.handle_selector_intent)


    # The "handle_xxxx_intent" functions define Mycroft's behavior when
    # each of the skill's intents is triggered: in this case, he simply
    # speaks a response. Note that the "speak_dialog" method doesn't
    # actually speak the text it's passed--instead, that text is the filename
    # of a file in the dialog folder, and Mycroft speaks its contents when
    # the method is called.

    #Background images
    def handle_next_intent(self, message):
        subprocess.call(["variety","-n"])

    def handle_previous_intent(self, message):
        subprocess.call(["variety","-p"])

    def handle_pause_intent(self, message):
        subprocess.call(["variety","--pause"])
        self.speak_dialog("pause")

    def handle_resume_intent(self, message):
        subprocess.call(["variety","--resume"])
        self.speak_dialog("resume")

    def handle_toggle_intent(self, message):
        subprocess.call(["variety","--toggle-pause"])

    def handle_fast_intent(self, message):
        subprocess.call(["variety","--fast-forward"])

    def handle_favorite_intent(self, message):
        subprocess.call(["variety","-f"])
        self.speak_dialog("image.favorite")

    def handle_trash_intent(self, message):
        subprocess.call(["variety","-t"])
        self.speak_dialog("trash")

    #Background quotes
    def handle_next_quote_intent(self, message):
        subprocess.call(["variety","--quotes-next"])

    def handle_previous_quote_intent(self, message):
        subprocess.call(["variety","--quotes-previous"])

    def handle_toggle_quote_intent(self, message):
        subprocess.call(["variety","--quotes-toggle-pause"])

    def handle_fast_quote_intent(self, message):
        subprocess.call(["variety","--quotes-fast-forward"])

    def handle_favorite_quote_intent(self, message):
        subprocess.call(["variety","--quotes-save-favorite"])
        self.speak_dialog("quote.favorite")

    #Variety interface

    def handle_version_intent(self, message):
        self.speak(subprocess.check_output(["variety","--version"]))

    def handle_preferences_intent(self, message):
        subprocess.call(["variety","--preferences"])
        self.speak_dialog("preferences")

    def handle_quit_intent(self, message):
        subprocess.call(["variety","-q"])
        self.speak_dialog("quit")

    def handle_history_intent(self, message):
        subprocess.call(["variety","--history"])
        self.speak_dialog("history")

    def handle_downloads_intent(self, message):
        subprocess.call(["variety","--downloads"])
        self.speak_dialog("downloads")

    #TODO: Find a way to make the "variety --selector" command work.
    def handle_selector_intent(self, message):
        subprocess.call(["variety","--selector"])
        self.speak_dialog("selector")

    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, the method just contains the keyword "pass", which
    # does nothing.
    def stop(self):
        pass

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return VarietyController()
