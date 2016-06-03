#!/usr/bin/env python

import rospy, os, sys
from sound_play.msg import SoundRequest

from sound_play.libsoundplay import SoundClient

def sleep(t):
    try:
        rospy.sleep(t)
    except:
        pass

if __name__ == '__main__':
    rospy.init_node('soundplay_test', anonymous = True)
    soundhandle = SoundClient()

    rospy.sleep(1)

    soundhandle.stopAll()

    print "This script will run continuously until you hit CTRL+C, testing various sound_node sound types."

    print
    #print 'Try to play wave files that do not exist.'
    #soundhandle.playWave('17')
    #soundhandle.playWave('dummy')

    #print 'say'
    #soundhandle.say('Hello world!')
    #sleep(3)
    #

    print 'plugging'
    soundhandle.play(SoundRequest.NEEDS_PLUGGING)
    sleep(2)

    print 'unplugging'
    soundhandle.play(SoundRequest.NEEDS_UNPLUGGING)
    sleep(2)

    print 'plugging badly'
    soundhandle.play(SoundRequest.NEEDS_PLUGGING_BADLY)
    sleep(2)

    print 'unplugging badly'
    soundhandle.play(SoundRequest.NEEDS_UNPLUGGING_BADLY)
    sleep(2)

    s1 = soundhandle.builtinSound(SoundRequest.NEEDS_UNPLUGGING_BADLY)
    s3 = soundhandle.voiceSound("Testing the new A P I")

    print "New API start voice"
    s3.repeat()
    sleep(3)

    print "New API builtin"
    s1.play()
    sleep(2)

    print "New API stop"
    s3.stop()
