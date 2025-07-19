kernel-level programming


The Apple documentation you linked to is about using AVFoundation for media capture on macOS, which is a high-level framework for working with audio and video. While it's extremely powerful and flexible, it doesn't provide the kind of low-level access to the camera that you would need to replace the default camera feed at the kernel level.

Kernel-level programming is a specialized field that requires a deep understanding of operating systems and the specific hardware you're working with. It's also risky: mistakes can lead to system crashes or security vulnerabilities. Kernel extensions (kexts) are typically written in C or C++, not Python, and you would need to be familiar with macOS's I/O Kit framework.

If you're interested in going down this path, you would likely need to:

Gain a deep understanding of macOS's I/O Kit and driver architecture.
Learn how to write a kernel extension (kext) for macOS.
Understand the specific APIs and data structures used by macOS's camera drivers.
Write your own driver that captures video from the real camera, modifies the frames to include your ASCII art, and then sends those frames to any application that is using the camera.
This would be a large and complex project that goes well beyond what can be easily explained here. It would also require specialized knowledge and tools, including:

A Mac computer running macOS.
Xcode and the macOS SDK.
A paid Apple Developer Program membership if you want to distribute your driver.
Familiarity with C or C++.
Familiarity with macOS's security features, including code signing and entitlements.
If you're serious about pursuing this, I would recommend starting by learning about macOS driver development and the I/O Kit framework. Apple's I/O Kit Fundamentals guide would be a good starting point.

However, for most purposes, creating a virtual camera as described in my previous answer would be much simpler and safer.