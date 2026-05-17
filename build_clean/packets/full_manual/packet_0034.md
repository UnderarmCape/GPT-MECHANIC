# Deep Research Manual Packet 0034

## Suggested Deep Research Prompt

> You are analyzing a 2016 Honda Civic LX 4D Sedan CVT service manual packet. Use only the manual excerpts in this packet as evidence. When answering, cite the relevant source_path and chunk_id. If this packet does not contain enough information, say what is missing and ask for another packet or targeted retrieval.

## Packet Metadata

- Vehicle: 2016 Honda Civic LX 4D Sedan CVT
- Packet number: 0034
- Chunk count: 429
- Chunk range: 8297-8725
- Source count: 399
- Target maximum characters: 750000

## Manual Chunks

## Chunk 8297: Scope Of This Article

- Title: Scope Of This Article
- Source path: `pages\10611.html`
- Chunk ID: `chunk_220d51b7dbd8`
- Images: none
- Duplicate sources: `pages\17787.html`

### Full Text

````text
# Scope Of This Article

This is NOT a manufacturer specific article. All different types of systems are covered here, regardless of the specific year/make/model/engine.

The reason for such broad coverage is because there are only a few basic ways to operate a solenoid-type injector. By understanding the fundamental principles, you will understand all the major points of injector patterns you encounter. Of course there are minor differences in each specific system, but that is where a waveform library helps out.

If this is confusing, consider a secondary ignition pattern. Even though there are many different implementations, each still has a primary voltage turn-on, firing line, spark line, etc.

If specific waveforms are available in On Demand for the engine and vehicle you are working on, you will find them in the Engine Performance section under the Engine Performance category.
````

## Chunk 8298: Is A Lab Scope Necessary?: Introduction

- Title: Is A Lab Scope Necessary?: Introduction
- Source path: `pages\10612.html`
- Chunk ID: `chunk_51a8574c33af`
- Images: none
- Duplicate sources: `pages\17788.html`

### Full Text

````text
# Is A Lab Scope Necessary?: Introduction

You probably have several tools at your disposal to diagnose injector circuits. But you might have questioned "Is a lab scope necessary to do a thorough job, or will a set of noid lights and a multifunction DVOM do just as well?"

In the following text, we are going to look at what noid lights and DVOMs do best, do not do very well, and when they can mislead you. As you might suspect, the lab scope, with its ability to look inside an active circuit, comes to the rescue by answering for the deficiencies of these other tools.
````

## Chunk 8299: Overview Of NOID Light: Notes

- Title: Overview Of NOID Light: Notes
- Source path: `pages\10613.html`
- Chunk ID: `chunk_c31c91afa658`
- Images: none
- Duplicate sources: `pages\17789.html`

### Full Text

````text
# Overview Of NOID Light: Notes

The noid light is an excellent "quick and dirty" tool. It can usually be hooked to a fuel injector harness fast and the flashing light is easy to understand. It is a dependable way to identify a no-pulse situation.

However, a noid light can be very deceptive in two cases:

- If the wrong one is used for the circuit being tested. Beware: Just because a connector on a noid light fits the harness does not mean it is the right one.

- If an injector driver is weak or a minor voltage drop is present.
````

## Chunk 8300: Use the Right Noid Light

- Title: Use the Right Noid Light
- Source path: `pages\10614.html`
- Chunk ID: `chunk_e77d0fdd8d0e`
- Images: none
- Duplicate sources: `pages\17790.html`

### Full Text

````text
# Use the Right Noid Light

In the following text we will look at what can happen if the wrong noid light is used, why there are different types of noid lights (besides differences with connectors), how to identify the types of noid lights, and how to know the right type to use.

First, let's discuss what can happen if the incorrect type of noid light is used. You might see:

- A dimly flashing light when it should be normal.

- A normal flashing light when it should be dim.

A noid light will flash dim if used on a lower voltage circuit than it was designed for. A normally operating circuit would appear underpowered, which could be misinterpreted as the cause of a fuel starvation problem.

Here are the two circuit types that could cause this problem:

- Circuits with external injector resistors. Used predominately on some Asian & European systems, they are used to reduce the available voltage to an injector in order to limit the current flow. This lower voltage can cause a dim flash on a noid light designed for full voltage.

- Circuits with current controlled injector drivers (e.g. "Peak and Hold"). Basically, this type of driver allows a quick burst of voltage/current to flow and then throttles it back significantly for the remainder of the pulse width duration. If a noid light was designed for the other type of driver (voltage controlled, e.g. "Saturated"), it will appear dim because it is expecting full voltage/current to flow for the entire duration of the pulse width.

Let's move to the other situation where a noid light flashes normally when it should be dim. This could occur if a more sensitive noid light is used on a higher voltage/amperage circuit that was weakened enough to cause problems (but not outright broken). A circuit with an actual problem would thus appear normal.

Let's look at why. A noid light does not come close to consuming as much amperage as an injector solenoid. If there is a partial driver failure or a minor voltage drop in the injector circuit, there can be adequate amperage to fully operate the noid light BUT NOT ENOUGH TO OPERATE THE INJECTOR.

If this is not clear, picture a battery with a lot of corrosion on the terminals. Say there is enough corrosion that the starter motor will not operate; it only clicks. Now imagine turning on the headlights (with the ignition in the RUN position). You find they light normally and are fully bright. This is the same idea as noid light: There is a problem, but enough amp flow exists to operate the headlights ("noid light"), but not the starter motor ("injector").

How do you identify and avoid all these situations? By using the correct type of noid light. This requires that you understanding the types of injector circuits that your noid lights are designed for. There are three. They are:

- Systems with a voltage controlled injector driver. Another way to say it: The noid light is designed for a circuit with a "high" resistance injector (generally 12 ohms or above).

- Systems with a current controlled injector driver. Another way to say it: The noid light is designed for a circuit with a low resistance injector (generally less than 12 ohms) without an external injector resistor.

- Systems with a voltage controlled injector driver and an external injector resistor. Another way of saying it: The noid light is designed for a circuit with a low resistance injector (generally less than 12 ohms) and an external injector resistor.

If you are not sure which type of circuit your noid light is designed for, plug it into a known good car and check out the results. If it flashes normally during cranking, determine the circuit type by finding out injector resistance and if an external injector resistor is used. You now know enough to identify the type of injector circuit. Label the noid light appropriately.

Next time you need to use a noid light for diagnosis, determine what type of injector circuit you are dealing with and select the appropriate noid light.

Of course, if you suspect a no-pulse condition you could plug in any one whose connector fit without fear of misdiagnosis. This is because it is unimportant if the flashing light is dim or bright. It is only important that it flashes.

In any cases of doubt regarding the use of a noid light, a lab scope will overcome all inherent weaknesses.
````

## Chunk 8301: Overview Of DVOM: Notes

- Title: Overview Of DVOM: Notes
- Source path: `pages\10615.html`
- Chunk ID: `chunk_2bf2f82ef2c3`
- Images: none
- Duplicate sources: `pages\17791.html`

### Full Text

````text
# Overview Of DVOM: Notes

A DVOM is typically used to check injector resistance and available voltage at the injector. Some techs also use it check injector on-time either with a built-in feature or by using the dwell/duty function.

There are situations where the DVOM performs these checks dependably, and other situations where it can deceive you. It is important to be aware of these strengths and weaknesses. We will cover the topics above in the following text.
````

## Chunk 8302: Checking Injector Resistance

- Title: Checking Injector Resistance
- Source path: `pages\10616.html`
- Chunk ID: `chunk_22b996a2fc6d`
- Images: none
- Duplicate sources: `pages\17792.html`

### Full Text

````text
# Checking Injector Resistance

If a short in an injector coil winding is constant, an ohmmeter will accurately identify the lower resistance. The same is true with an open winding. Unfortunately, an intermittent short is an exception. A faulty injector with an intermittent short will show "good" if the ohmmeter cannot force the short to occur during testing.

Alcohol in fuel typically causes an intermittent short, happening only when the injector coil is hot and loaded by a current high enough to jump the air gap between two bare windings or to break down any oxides that may have formed between them.

When you measure resistance with an ohmmeter, you are only applying a small current of a few milliamps. This is nowhere near enough to load the coil sufficiently to detect most problems. As a result, most resistance checks identify intermittently shorted injectors as being normal.

There are two methods to get around this limitation. The first is to purchase an tool that checks injector coil windings under full load. The Kent-Moore J-39021 is such a tool, though there are others. The Kent-Moore costs around $240 at the time of this writing and works on many different manufacturer's systems.

The second method is to use a lab scope. Remember, a lab scope allows you to see the regular operation of a circuit in real time. If an injector is having an short or intermittent short, the lab scope will show it.
````

## Chunk 8303: Checking Available Voltage At the Injector

- Title: Checking Available Voltage At the Injector
- Source path: `pages\10617.html`
- Chunk ID: `chunk_747d0bb43f99`
- Images: none
- Duplicate sources: `pages\17793.html`

### Full Text

````text
# Checking Available Voltage At the Injector

Verifying a fuel injector has the proper voltage to operate correctly is good diagnostic technique. Finding an open circuit on the feed circuit like a broken wire or connector is an accurate check with a DVOM. Unfortunately, finding an intermittent or excessive resistance problem with a DVOM is unreliable.

Let's explore this drawback. Remember that a voltage drop due to excessive resistance will only occur when a circuit is operating? Since the injector circuit is only operating for a few milliseconds at a time, a DVOM will only see a potential fault for a few milliseconds. The remaining 90+% of the time the unloaded injector circuit will show normal battery voltage.

Since DVOMs update their display roughly two to five times a second, all measurements in between are averaged. Because a potential voltage drop is visible for such a small amount of time, it gets "averaged out", causing you to miss it.

Only a DVOM that has a "min-max" function that checks EVERY MILLISECOND will catch this fault consistently (if used in that mode). The Fluke 87 among others has this capability.

A "min-max" DVOM with a lower frequency of checking (100 millisecond) can miss the fault because it will probably check when the injector is not on. This is especially true with current controlled driver circuits. The Fluke 88, among others fall into this category.

Outside of using a Fluke 87 (or equivalent) in the 1 mS "min-max" mode, the only way to catch a voltage drop fault is with a lab scope. You will be able to see a voltage drop as it happens.

One final note. It is important to be aware that an injector circuit with a solenoid resistor will always show a voltage drop when the circuit is energized. This is somewhat obvious and normal; it is a designed-in voltage drop. What can be unexpected is what we already covered--a voltage drop disappears when the circuit is unloaded. The unloaded injector circuit will show normal battery voltage at the injector. Remember this and do not get confused.
````

## Chunk 8304: Checking Injector On-Time With Built-In Function

- Title: Checking Injector On-Time With Built-In Function
- Source path: `pages\10618.html`
- Chunk ID: `chunk_bc79af66083c`
- Images: none
- Duplicate sources: `pages\17794.html`

### Full Text

````text
# Checking Injector On-Time With Built-In Function

Several DVOMs have a feature that allows them to measure injector on-time (mS pulse width). While they are accurate and fast to hookup, they have three limitations you should be aware of:

- They only work on voltage controlled injector drivers (e.g "Saturated Switch"), NOT on current controlled injector drivers (e.g. "Peak & Hold").

- A few unusual conditions can cause inaccurate readings.

- Varying engine speeds can result in inaccurate readings.

Regarding the first limitation, DVOMs need a well-defined injector pulse in order to determine when the injector turns ON and OFF. Voltage controlled drivers provide this because of their simple switch-like operation. They completely close the circuit for the entire duration of the pulse. This is easy for the DVOM to interpret.

The other type of driver, the current controlled type, start off well by completely closing the circuit (until the injector pintle opens), but then they throttle back the voltage/current for the duration of the pulse. The DVOM understands the beginning of the pulse but it cannot figure out the throttling action. In other words, it cannot distinguish the throttling from an open circuit (de-energized) condition.

Yet current controlled injectors will still yield a millisecond on-time reading on these DVOMs. You will find it is also always the same, regardless of the operating conditions. This is because it is only measuring the initial completely-closed circuit on-time, which always takes the same amount of time (to lift the injector pintle off its seat). So even though you get a reading, it is useless.

The second limitation is that a few erratic conditions can cause inaccurate readings. This is because of a DVOM's slow display rate; roughly two to five times a second. As we covered earlier, measurements in between display updates get averaged. So conditions like skipped injector pulses or intermittent long/short injector pulses tend to get "averaged out", which will cause you to miss important details.

The last limitation is that varying engine speeds can result in inaccurate readings. This is caused by the quickly shifting injector on-time as the engine load varies, or the RPM moves from a state of acceleration to stabilization, or similar situations. It too is caused by the averaging of all measurements in between DVOM display periods. You can avoid this by checking on-time when there are no RPM or load changes.

A lab scope allows you to overcome each one of these limitations.
````

## Chunk 8305: Checking Injector On-Time With Dwell Or Duty

- Title: Checking Injector On-Time With Dwell Or Duty
- Source path: `pages\10619.html`
- Chunk ID: `chunk_20abd2f2cea6`
- Images: none
- Duplicate sources: `pages\17795.html`

### Full Text

````text
# Checking Injector On-Time With Dwell Or Duty

If no tool is available to directly measure injector millisecond on-time measurement, some techs use a simple DVOM dwell or duty cycle functions as a replacement.

While this is an approach of last resort, it does provide benefits. We will discuss the strengths and weaknesses in a moment, but first we will look at how a duty cycle meter and dwell meter work.
````

## Chunk 8306: How A Duty Cycle Meter and Dwell Meter Work

- Title: How A Duty Cycle Meter and Dwell Meter Work
- Source path: `pages\10620.html`
- Chunk ID: `chunk_5b8394658747`
- Images: none
- Duplicate sources: `pages\17796.html`

### Full Text

````text
# How A Duty Cycle Meter and Dwell Meter Work

All readings are obtained by comparing how long something has been OFF to how long it has been ON in a fixed time period. A dwell meter and duty cycle meter actually come up with the same answers using different scales. You can convert freely between them. See RELATIONSHIP BETWEEN DWELL & DUTY CYCLE READINGS TABLE .

The DVOM display updates roughly one time a second, although some DVOMs can be a little faster or slower. All measurements during this update period are tallied inside the DVOM as ON time or OFF time, and then the total ratio is displayed as either a percentage (duty cycle) or degrees (dwell meter).

For example, let's say a DVOM had an update rate of exactly 1 second (1000 milliseconds). Let's also say that it has been measuring/tallying an injector circuit that had been ON a total of 250 mS out of the 1000 mS. That is a ratio of one-quarter, which would be displayed as 25% duty cycle or 15° dwell (six-cylinder scale). Note that most duty cycle meters can reverse the readings by selecting the positive or negative slope to trigger on. If this reading were reversed, a duty cycle meter would display 75%.
````

## Chunk 8307: Strengths of Dwell/Duty Meter

- Title: Strengths of Dwell/Duty Meter
- Source path: `pages\10621.html`
- Chunk ID: `chunk_1d6701a44371`
- Images: none
- Duplicate sources: `pages\17797.html`

### Full Text

````text
# Strengths of Dwell/Duty Meter

The obvious strength of a dwell/duty meter is that you can compare injector on-time against a known-good reading. This is the only practical way to use a dwell/duty meter, but requires you to have known-good values to compare against.

Another strength is that you can roughly convert injector mS on-time into dwell reading with some computations.

A final strength is that because the meter averages everything together it does not miss anything (though this is also a severe weakness that we will look at later). If an injector has a fault where it occasionally skips a pulse, the meter registers it and the reading changes accordingly.

Let's go back to figuring out dwell/duty readings by using injector on-time specification. This is not generally practical, but we will cover it for completeness. You NEED to know three things:

- Injector mS on-time specification.

- Engine RPM when specification is valid.

- How many times the injectors fire per crankshaft revolution.

The first two are self-explanatory. The last one may require some research into whether it is a bank-fire type that injects every 360° of crankshaft rotation, a bank-fire that injects every 720°, or an SFI that injects every 720°. Many manufacturers do not release this data so you may have to figure it out yourself with a frequency meter.

Here are the four complete steps to convert millisecond on-time:

- Determine the injector pulse width and RPM it was obtained at. Let's say the specification is for one millisecond of on-time at a hot idle of 600 RPM.

- Determine injector firing method for the complete 4 stroke cycle. Let's say this is a 360° bank-fired, meaning an injector fires each and every crankshaft revolution.

- Determine how many times the injector will fire at the specified engine speed (600 RPM) in a fixed time period. We will use 100 milliseconds because it is easy to use. Six hundred crankshaft Revolutions Per Minute (RPM) divided by 60 seconds equals 10 revolutions per second. Multiplying 10 times .100 yields one; the crankshaft turns one time in 100 milliseconds. With exactly one crankshaft rotation in 100 milliseconds, we know that the injector fires exactly one time.

- Determine the ratio of injector on-time vs. off-time in the fixed time period, then figure duty cycle and/or dwell. The injector fires one time for a total of one millisecond in any given 100 millisecond period. One hundred minus one equals 99. We have a 99% duty cycle. If we wanted to know the dwell (on 6 cylinder scale), multiple 99% times .6; this equals 59.4° dwell.
````

## Chunk 8308: Weaknesses of Dwell/Duty Meter

- Title: Weaknesses of Dwell/Duty Meter
- Source path: `pages\10622.html`
- Chunk ID: `chunk_cdcbf24192b2`
- Images: none
- Duplicate sources: `pages\17798.html`

### Full Text

````text
# Weaknesses of Dwell/Duty Meter

The weaknesses are significant. First, there is no one-to-one correspondence to actual mS on-time. No manufacturer releases dwell/duty data, and it is time-consuming to convert the mS on-time readings. Besides, there can be a large degree of error because the conversion forces you to assume that the injector(s) are always firing at the same rate for the same period of time. This can be a dangerous assumption.

Second, all level of detail is lost in the averaging process. This is the primary weakness. You cannot see the details you need to make a confident diagnosis.

Here is one example. Imagine a vehicle that has a faulty injector driver that occasionally skips an injector pulse. Every skipped pulse means that that cylinder does not fire, thus unburned O2 gets pushed into the exhaust and passes the O2 sensor. The O2 sensor indicates lean, so the computer fattens up the mixture to compensate for the supposed "lean" condition.

A connected dwell/duty meter would see the fattened pulse width but would also see the skipped pulses. It would tally both and likely come back with a reading that indicated the "pulse width" was within specification because the rich mixture and missing pulses offset each other.

This situation is not a far-fetched scenario. Some early GM 3800 engines were suffering from exactly this. The point is that a lack of detail could cause misdiagnosis.

As you might have guessed, a lab scope would not miss this.

Dwell Meter (2) | Duty Cycle Meter

1° | 1%

15° | 25%

30° | 50%

45° | 75%

60° | 100%

(1) These are just some examples for your understanding. It is okay to fill in the gaps. (2) Dwell meter on the six-cylinder scale. | (1) | These are just some examples for your understanding. It is okay to fill in the gaps. | (2) | Dwell meter on the six-cylinder scale.

(1) | These are just some examples for your understanding. It is okay to fill in the gaps.

(2) | Dwell meter on the six-cylinder scale.
````

## Chunk 8309: The Two Types Of Injector Drivers: Notes

- Title: The Two Types Of Injector Drivers: Notes
- Source path: `pages\10623.html`
- Chunk ID: `chunk_c1e1273268c7`
- Images: none
- Duplicate sources: `pages\17799.html`

### Full Text

````text
# The Two Types Of Injector Drivers: Notes
````

## Chunk 8310: The Two Types Of Injector Drivers: Overview

- Title: The Two Types Of Injector Drivers: Overview
- Source path: `pages\10624.html`
- Chunk ID: `chunk_0a06c45d679f`
- Images: none
- Duplicate sources: `pages\17800.html`

### Full Text

````text
# The Two Types Of Injector Drivers: Overview

There are two types of transistor driver circuits used to operate electric fuel injectors: voltage controlled and current controlled. The voltage controlled type is sometimes called a "saturated switch" driver, while the current controlled type is sometimes known as a "peak and hold" driver.

The basic difference between the two is the total resistance of the injector circuit. Roughly speaking, if a particular leg in an injector circuit has total resistance of 12 or more ohms, a voltage control driver is used. If less than 12 ohms, a current control driver is used.

It is a question of what is going to do the job of limiting the current flow in the injector circuit; the inherent "high" resistance in the injector circuit, or the transistor driver. Without some form of control, the current flow through the injector would cause the solenoid coil to overheat and result in a damaged injector.
````

## Chunk 8311: Voltage Controlled Circuit ("Saturated Switch")

- Title: Voltage Controlled Circuit ("Saturated Switch")
- Source path: `pages\10625.html`
- Chunk ID: `chunk_17d288c0905b`
- Images: `images\G50G15053.gif`
- Duplicate sources: `pages\17801.html`

### Full Text

````text
# Voltage Controlled Circuit ("Saturated Switch")

The voltage controlled driver inside the computer operates much like a simple switch because it does not need to worry about limiting current flow. Recall, this driver typically requires injector circuits with a total leg resistance of 12 or more ohms.

The driver is either ON, closing/completing the circuit (eliminating the voltage-drop), or OFF, opening the circuit (causing a total voltage drop).

Some manufacturers call it a "saturated switch" driver. This is because when switched ON, the driver allows the magnetic field in the injector to build to saturation. This is the same "saturation" property that you are familiar with for an ignition coil.

There are two ways "high" resistance can be built into an injector circuit to limit current flow. One method uses an external solenoid resistor and a low resistance injector, while the other uses a high resistance injector without the solenoid resistor. See the left side of Fig. Fig 1 .

In terms of injection opening time, the external resistor voltage controlled circuit is somewhat faster than the voltage controlled high resistance injector circuit. The trend, however, seems to be moving toward use of this latter type of circuit due to its lower cost and reliability. The ECU can compensate for slower opening times by increasing injector pulse width accordingly.
````

## Chunk 8312: Current Controlled Circuit ("Peak & Hold")

- Title: Current Controlled Circuit ("Peak & Hold")
- Source path: `pages\10626.html`
- Chunk ID: `chunk_f79504c11e7a`
- Images: none
- Duplicate sources: `pages\17802.html`

### Full Text

````text
# Current Controlled Circuit ("Peak & Hold")

The current controlled driver inside the computer is more complex than a voltage controlled driver because as the name implies, it has to limit current flow in addition to its ON-OFF switching function. Recall, this driver typically requires injector circuits with a total leg resistance of less than 12 ohms.

Once the driver is turned ON, it will not limit current flow until enough time has passed for the injector pintle to open. This period is preset by the particular manufacturer/system based on the amount of current flow needed to open their injector. This is typically between two and six amps. Some manufacturers refer to this as the "peak" time, referring to the fact that current flow is allowed to "peak" (to open the injector).

Once the injector pintle is open, the amp flow is considerably reduced for the rest of the pulse duration to protect the injector from overheating. This is okay because very little amperage is needed to hold the injector open, typically in the area of one amp or less. Some manufacturers refer to this as the "hold" time, meaning that just enough current is allowed through the circuit to "hold" the already-open injector open.

There are a couple methods of reducing the current. The most common trims back the available voltage for the circuit, similar to turning down a light at home with a dimmer.

The other method involves repeatedly cycling the circuit ON-OFF. It does this so fast that the magnetic field never collapses and the pintle stays open, but the current is still significantly reduced. See the right side of Fig. Figure for an illustration.

The advantage to the current controlled driver circuit is the short time period from when the driver transistor goes ON to when the injector actually opens. This is a function of the speed with which current flow reaches its peak due to the low circuit resistance. Also, the injector closes faster when the driver turns OFF because of the lower holding current.
````

## Chunk 8313: The Two Ways Injector Circuits Are Wired

- Title: The Two Ways Injector Circuits Are Wired
- Source path: `pages\10627.html`
- Chunk ID: `chunk_ad79aed56838`
- Images: none
- Duplicate sources: `pages\17803.html`

### Full Text

````text
# The Two Ways Injector Circuits Are Wired

Like other circuits, injector circuits can be wired in one of two fundamental directions. The first method is to steadily power the injectors and have the computer driver switch the ground side of the circuit. Conversely, the injectors can be steadily grounded while the driver switches the power side of the circuit.

There is no performance benefit to either method. Voltage controlled and current controlled drivers have been successfully implemented both ways.

However, 95% percent of the systems are wired so the driver controls the ground side of the circuit. Only a handful of systems use the drivers on the power side of the circuit. Some examples of the latter are the 1970's Cadillac EFI system, early Jeep 4.0 EFI (Renix system), and Chrysler 1984-87 TBI.
````

## Chunk 8314: Interpreting Injector Waveforms: Notes

- Title: Interpreting Injector Waveforms: Notes
- Source path: `pages\10628.html`
- Chunk ID: `chunk_c67aaf4d02ef`
- Images: none
- Duplicate sources: `pages\17804.html`

### Full Text

````text
# Interpreting Injector Waveforms: Notes
````

## Chunk 8315: Interpreting A Voltage Controlled Pattern

- Title: Interpreting A Voltage Controlled Pattern
- Source path: `pages\10629.html`
- Chunk ID: `chunk_59ee09d138a8`
- Images: `images\G95B23862.gif`
- Duplicate sources: `pages\17805.html`

### Full Text

````text
# Interpreting A Voltage Controlled Pattern

- See Fig 1 for pattern that the following text describes.

Point "A" is where system voltage is supplied to the injector. A good hot run voltage is usually 13.5 or more volts. This point, commonly known as open circuit voltage, is critical because the injector will not get sufficient current saturation if there is a voltage shortfall. To obtain a good look at this precise point, you will need to shift your Lab Scope to five volts per division.

You will find that some systems have slight voltage fluctuations here. This can occur if the injector feed wire is also used to power up other cycling components, like the ignition coil(s). Slight voltage fluctuations are normal and are no reason for concern. Major voltage fluctuations are a different story, however. Major voltage shifts on the injector feed line will create injector performance problems. Look for excessive resistance problems in the feed circuit if you see big shifts and repair as necessary.

Note that circuits with external injector resistors will not be any different because the resistor does not affect open circuit voltage.

Point "B" is where the driver completes the circuit to ground. This point of the waveform should be a clean square point straight down with no rounded edges. It is during this period that current saturation of the injector windings is taking place and the driver is heavily stressed. Weak drivers will distort this vertical line.

Point "C" represents the voltage drop across the injector windings. Point "C" should come very close to the ground reference point, but not quite touch. This is because the driver has a small amount of inherent resistance. Any significant offset from ground is an indication of a resistance problem on the ground circuit that needs repaired. You might miss this fault if you do not use the negative battery post for your Lab Scope hook-up, so it is HIGHLY recommended that you use the battery as your hook-up.

The points between "B" and "D" represent the time in milliseconds that the injector is being energized or held open. This line at Point "C" should remain flat. Any distortion or upward bend indicates a ground problem, short problem, or a weak driver. Alert readers will catch that this is exactly opposite of the current controlled type drivers (explained in the next section), because they bend upwards at this point.

How come the difference? Because of the total circuit resistance. Voltage controlled driver circuits have a high resistance of 12+ ohms that slows the building of the magnetic field in the injector. Hence, no counter voltage is built up and the line remains flat.

On the other hand, the current controlled driver circuit has low resistance which allows for a rapid magnetic field build-up. This causes a slight inductive rise (created by the effects of counter voltage) and hence, the upward bend. You should not see that here with voltage controlled circuits.

Point "D" represents the electrical condition of the injector windings. The height of this voltage spike (inductive kick) is proportional to the number of windings and the current flow through them. The more current flow and greater number of windings, the more potential for a greater inductive kick. The opposite is also true. The less current flow or fewer windings means less inductive kick. Typically you should see a minimum 35 volts at the top of Point "D".

If you do see approximately 35 volts, it is because a zener diode is used with the driver to clamp the voltage. Make sure the beginning top of the spike is squared off, indicating the zener dumped the remainder of the spike. If it is not squared, that indicates the spike is not strong enough to make the zener fully dump, meaning the injector has a weak winding.

If a zener diode is not used in the computer, the spike from a good injector will be 60 or more volts.

Point "E" brings us to a very interesting section. As you can see, the voltage dissipates back to supply value after the peak of the inductive kick. Notice the slight hump? This is actually the mechanical injector pintle closing. Recall that moving an iron core through a magnetic field will create a voltage surge. The pintle is the iron core here.

This pintle hump at Point "E" should occur near the end of the downward slope, and not afterwards.
````

## Chunk 8316: Interpreting A Voltage Controlled Pattern

- Title: Interpreting A Voltage Controlled Pattern
- Source path: `pages\10629.html`
- Chunk ID: `chunk_1a9ffd6f73c1`
- Images: `images\G95B23862.gif`
- Duplicate sources: `pages\17805.html`

### Full Text

````text
ure the beginning top of the spike is squared off, indicating the zener dumped the remainder of the spike. If it is not squared, that indicates the spike is not strong enough to make the zener fully dump, meaning the injector has a weak winding.

If a zener diode is not used in the computer, the spike from a good injector will be 60 or more volts.

Point "E" brings us to a very interesting section. As you can see, the voltage dissipates back to supply value after the peak of the inductive kick. Notice the slight hump? This is actually the mechanical injector pintle closing. Recall that moving an iron core through a magnetic field will create a voltage surge. The pintle is the iron core here.

This pintle hump at Point "E" should occur near the end of the downward slope, and not afterwards. If it does occur after the slope has ended and the voltage has stabilized, it is because the pintle is slightly sticking because of a faulty injector

If you see more than one hump it is because of a distorted pintle or seat. This faulty condition is known as "pintle float".

It is important to realize that it takes a good digital storage oscilloscope or analog lab scope to see this pintle hump clearly. Unfortunately, it cannot always be seen.
````

## Chunk 8317: Interpreting A Current Controlled Pattern

- Title: Interpreting A Current Controlled Pattern
- Source path: `pages\10630.html`
- Chunk ID: `chunk_2fdec839d566`
- Images: `images\G95C23863.gif`
- Duplicate sources: `pages\17806.html`

### Full Text

````text
# Interpreting A Current Controlled Pattern

- See Fig 1 for pattern that the following text describes.

Point "A" is where system voltage is supplied to the injector. A good hot run voltage is usually 13.5 or more volts. This point, commonly known as open circuit voltage, is critical because the injector will not get sufficient current saturation if there is a voltage shortfall. To obtain a good look at this precise point, you will need to shift your Lab Scope to five volts per division.

You will find that some systems have slight voltage fluctuations here. This could occur if the injector feed wire is also used to power up other cycling components, like the ignition coil(s). Slight voltage fluctuations are normal and are no reason for concern. Major voltage fluctuations are a different story, however. Major voltage shifts on the injector feed line will create injector performance problems. Look for excessive resistance problems in the feed circuit if you see big shifts and repair as necessary.

Point "B" is where the driver completes the circuit to ground. This point of the waveform should be a clean square point straight down with no rounded edges. It is during this period that current saturation of the injector windings is taking place and the driver is heavily stressed. Weak drivers will distort this vertical line.

Point "C" represents the voltage drop across the injector windings. Point "C" should come very close to the ground reference point, but not quite touch. This is because the driver has a small amount of inherent resistance. Any significant offset from ground is an indication of a resistance problem on the ground circuit that needs repaired. You might miss this fault if you do not use the negative battery post for your Lab Scope hook-up, so it is HIGHLY recommended that you use the battery as your hook-up.

Right after Point "C", something interesting happens. Notice the trace starts a normal upward bend. This slight inductive rise is created by the effects of counter voltage and is normal. This is because the low circuit resistance allowed a fast build-up of the magnetic field, which in turn created the counter voltage.

Point "D" is the start of the current limiting, also known as the "Hold" time. Before this point, the driver had allowed the current to free-flow ("Peak") just to get the injector pintle open. By the time point "D" occurs, the injector pintle has already opened and the computer has just significantly throttled the current back. It does this by only allowing a few volts through to maintain the minimum current required to keep the pintle open.

The height of the voltage spike seen at the top of Point "D" represents the electrical condition of the injector windings. The height of this voltage spike (inductive kick) is proportional to the number of windings and the current flow through them. The more current flow and greater number of windings, the more potential for a greater inductive kick. The opposite is also true. The less current flow or fewer windings means less inductive kick. Typically you should see a minimum 35 volts.

If you see approximately 35 volts, it is because a zener diode is used with the driver to clamp the voltage. Make sure the beginning top of the spike is squared off, indicating the zener dumped the remainder of the spike. If it is not squared, that indicates the spike is not strong enough to make the zener fully dump, meaning there is a problem with a weak injector winding.

If a zener diode is not used in the computer, the spike from a good injector will be 60 or more volts.

At Point "E", notice that the trace is now just a few volts below system voltage and the injector is in the current limiting, or the "Hold" part of the pattern. This line will either remain flat and stable as shown here, or will cycle up and down rapidly. Both are normal methods to limit current flow. Any distortion may indicate shorted windings.

Point "F" is the actual turn-off point of the driver (and injector). To measure the millisecond on-time of the injector, measure between points "C" and "F". Note that we used cursors to do it for us; they are measuring a 2.56 mS on-time.

The top of Point "F" (second inductive kick) is created by the collapsing magnetic field caused by the final turn-off of the driver. This spike should be like the spike on top of point "D".

Point "G" shows a slight hump. This is actually the mechanical injector pintle closing.
````

## Chunk 8318: Interpreting A Current Controlled Pattern

- Title: Interpreting A Current Controlled Pattern
- Source path: `pages\10630.html`
- Chunk ID: `chunk_1840c043dcc6`
- Images: `images\G95C23863.gif`
- Duplicate sources: `pages\17806.html`

### Full Text

````text
ystem voltage and the injector is in the current limiting, or the "Hold" part of the pattern. This line will either remain flat and stable as shown here, or will cycle up and down rapidly. Both are normal methods to limit current flow. Any distortion may indicate shorted windings.

Point "F" is the actual turn-off point of the driver (and injector). To measure the millisecond on-time of the injector, measure between points "C" and "F". Note that we used cursors to do it for us; they are measuring a 2.56 mS on-time.

The top of Point "F" (second inductive kick) is created by the collapsing magnetic field caused by the final turn-off of the driver. This spike should be like the spike on top of point "D".

Point "G" shows a slight hump. This is actually the mechanical injector pintle closing. Recall that moving an iron core through a magnetic field will create a voltage surge. The pintle is the iron core here.

This pintle hump at Point "E" should occur near the end of the downward slope, and not afterwards. If it does occur after the slope has ended and the voltage has stabilized, it is because the pintle is slightly sticking. Some older Nissan TBI systems suffered from this.

If you see more than one hump it is because of a distorted pintle or seat. This faulty condition is known as "pintle float".

It is important to realize that it takes a good digital storage oscilloscope or analog lab scope to see this pintle hump clearly. Unfortunately, it cannot always be seen.
````

## Chunk 8319: Current Waveform Samples: Notes

- Title: Current Waveform Samples: Notes
- Source path: `pages\10631.html`
- Chunk ID: `chunk_bb4e36112d93`
- Images: none
- Duplicate sources: `pages\17807.html`

### Full Text

````text
# Current Waveform Samples: Notes
````

## Chunk 8320: Example #1 - Voltage Controlled Driver

- Title: Example #1 - Voltage Controlled Driver
- Source path: `pages\10632.html`
- Chunk ID: `chunk_eca643326857`
- Images: `images\G95D23864.gif`, `images\G95E23865.gif`, `images\G95F23866.gif`, `images\G95G23867.gif`
- Duplicate sources: `pages\17808.html`

### Full Text

````text
# Example #1 - Voltage Controlled Driver

The waveform pattern shown in Fig. Fig 1 indicate a normal current waveform from a Ford 3.0L V6 VIN [U] engine. This voltage controlled type circuit pulses the injectors in groups of three injectors. Injectors No. 1, 3, and 5 are pulsed together and cylinders 2, 4, and 6 are pulsed together. The specification for an acceptable bank resistance is 4.4 ohms. Using Ohm's Law and assuming a hot run voltage of 14 volts, we determine that the bank would draw a current of 3.2 amps.

However this is not the case because as the injector windings become saturated, counter voltage is created which impedes the current flow. This, coupled with the inherent resistance of the driver's transistor, impedes the current flow even more. So, what is a known good value for a dynamic current draw on a voltage controlled bank of injectors? The waveform pattern shown below indicates a good parallel injector current flow of 2 amps. See Fig 1 .

Note that if just one injector has a resistance problem and partially shorts, the entire parallel bank that it belongs to will draw more current. This can damage the injector driver.

The waveform pattern in Fig. Fig 2 indicates this type of problem with too much current flow. This is on other bank of injectors of the same vehicle; the even side. Notice the Lab Scope is set on a one amp per division scale. As you can see, the current is at an unacceptable 2.5 amps.

It is easy to find out which individual injector is at fault. All you need to do is inductively clamp onto each individual injector and compare them. To obtain a known-good value to compare against, we used the good bank to capture the waveform in Fig. Fig 3 . Notice that it limits current flow to 750 milliamps.

The waveform shown in Fig. Fig 4 illustrates the problem injector we found. This waveform indicates an unacceptable current draw of just over one amp as compared to the 750 milliamp draw of the known-good injector. A subsequent check with a DVOM found 8.2 ohms, which is under the 12 ohm specification.
````

## Chunk 8321: Example #2 - Voltage Controlled Driver

- Title: Example #2 - Voltage Controlled Driver
- Source path: `pages\10633.html`
- Chunk ID: `chunk_bb63c3c47f30`
- Images: `images\G95E23873.gif`, `images\G95F23874.gif`
- Duplicate sources: `pages\17809.html`

### Full Text

````text
# Example #2 - Voltage Controlled Driver

This time we will look at a GM 3.1L V6 VIN [T]. Fig. Fig 1 shows the 1, 3, 5 (odd) injector bank with the current waveform indicating about a 2.6 amp draw at idle. This pattern, taken from a known good vehicle, correctly stays at or below the maximum 2.6 amps current range. Ideally, the current for each bank should be very close in comparison.

Notice the small dimple on the current flow's rising edge. This is the actual injector opening or what engineers refer to as the "set point." For good idle quality, the set point should be uniform between the banks.

When discussing Ohm's Law as it pertains to this parallel circuit, consider that each injector has specified resistance of 12.2 ohms. Since all three injectors are in parallel the total resistance of this parallel circuit drops to 4.1 ohms. Fourteen volts divided by four ohms would pull a maximum of 3.4 amps on this bank of injectors. However, as we discussed in EXAMPLE #1 above, other factors knock this value down to roughly the 2.6 amp neighborhood.

Now we are going to take a look at the even bank of injectors; injectors 2, 4, and 6. See Fig 2 . Notice this bank peaked at 1.7 amps at idle as compared to the 2.6 amps peak of the odd bank (Fig. Fig 1 ). Current flow between even and odd injectors banks is not uniform, yet it is not causing a driveability problem. That is because it is still under the maximum amperage we figured out earlier. But be aware this vehicle could develop a problem if the amperage flow increases any more.

Checking the resistance of this even injector group with a DVOM yielded 6.2 ohms, while the odd injector group in the previous example read 4.1 ohms.
````

## Chunk 8322: Example #3 - Voltage Controlled Driver

- Title: Example #3 - Voltage Controlled Driver
- Source path: `pages\10634.html`
- Chunk ID: `chunk_d6e5f727ae49`
- Images: `images\G95G23875.gif`, `images\G95H23876.gif`
- Duplicate sources: `pages\17810.html`

### Full Text

````text
# Example #3 - Voltage Controlled Driver

Example #3 is of a Ford 5.0L V8 SEFI. Fig. Fig 1 shows a waveform of an individual injector at idle with the Lab Scope set on 200 milliamps per division. Notice the dimple in the rising edge. This dimple indicates the actual opening of the injector (set point) occurred at 400 milliamps and current peaked at 750 milliamps. This is a good specification for this engine.

The next waveform pattern in Fig. Fig 2 shows an abnormality with another injector. With the Lab Scope set on 500 milliamps per division, you can see that the current waveform indicates a 1200 milliamp draw. This is a faulty injector.

Abnormally low resistance injectors create excessive current draw, causing rough idle, and possible computer driver damage.
````

## Chunk 8323: Example #4 - Current Controlled Driver

- Title: Example #4 - Current Controlled Driver
- Source path: `pages\10635.html`
- Chunk ID: `chunk_fe7acf296444`
- Images: `images\G95D23872.gif`
- Duplicate sources: `pages\17811.html`

### Full Text

````text
# Example #4 - Current Controlled Driver

Example #4 is of a Ford 4.6L SEFI VIN [W]. See Fig 1 for the known-good waveform pattern. This Ford system is different from the one above in EXAMPLE #3 as it peaks at 900 milliamps and the actual opening of the injector (set point) is just below 600 milliamps.

This is offered as a comparison against the Ford pattern listed above, as they are both Ford SEFI injectors but with different operating ranges. The point is that you should not make any broad assumptions for any manufacturer.
````

## Chunk 8324: Example #5 - Current Controlled Driver

- Title: Example #5 - Current Controlled Driver
- Source path: `pages\10636.html`
- Chunk ID: `chunk_74b23a5d639e`
- Images: `images\G95H23868.gif`
- Duplicate sources: `pages\17812.html`

### Full Text

````text
# Example #5 - Current Controlled Driver

The known-good waveform in Fig. Fig 1 is from a Chrysler 3.0L V6 PFI VIN [3]. It is a perfect example of the peak and hold theory. The waveform shows a 1-amp per division current flow, ramping to 4 amps and then decreasing to 1-amp to hold the injector open.
````

## Chunk 8325: Example #6 - Current Controlled Driver

- Title: Example #6 - Current Controlled Driver
- Source path: `pages\10637.html`
- Chunk ID: `chunk_c0fb0e1ed66f`
- Images: `images\G95I23869.gif`
- Duplicate sources: `pages\17813.html`

### Full Text

````text
# Example #6 - Current Controlled Driver

This next known-good waveform is from a Ford 5.0L V8 CFI VIN [F]. See Fig 1 . The pattern, which is set on a 250 milliamps scale, indicates a 1.25 amp peak draw and a hold at 350 milliamps.
````

## Chunk 8326: Example #7 - Current Controlled Driver

- Title: Example #7 - Current Controlled Driver
- Source path: `pages\10638.html`
- Chunk ID: `chunk_86c953691c6a`
- Images: `images\G95C23871.gif`, `images\G95I23877.gif`
- Duplicate sources: `pages\17814.html`

### Full Text

````text
# Example #7 - Current Controlled Driver

The known-good current controlled type waveform in Fig. Fig 1 is from a GM 2.0L TBI VIN [1]. With the lab scope set at 2 amps per division, notice that this system peaks at 4 amps and holds at 1 amp.

The next waveform is from the same type of engine, except that it shows a faulty injector. See Fig 2 . Notice that the current went to almost 5 amps and stayed at 1 amp during the hold pattern. Excessive amounts of current flow from bad injectors are a common source of intermittent computer shutdown. Using a current waveform pattern is the most accurate method of pinpointing this problem.
````

## Chunk 8327: Example #8 - Current Controlled Driver

- Title: Example #8 - Current Controlled Driver
- Source path: `pages\10639.html`
- Chunk ID: `chunk_c4869439054e`
- Images: `images\G95B23870.gif`
- Duplicate sources: `pages\17815.html`

### Full Text

````text
# Example #8 - Current Controlled Driver

This known-good CPI system waveform from a GM 4.3L V6 CPI VIN [W] peaks at 4 amps and holds at 1-amp. See Fig 1 for waveform.
````

## Chunk 8328: Voltage Waveform Samples: Notes

- Title: Voltage Waveform Samples: Notes
- Source path: `pages\10640.html`
- Chunk ID: `chunk_2039e050b72e`
- Images: none
- Duplicate sources: `pages\17816.html`

### Full Text

````text
# Voltage Waveform Samples: Notes
````

## Chunk 8329: Example #1 - Voltage Controlled Driver

- Title: Example #1 - Voltage Controlled Driver
- Source path: `pages\10641.html`
- Chunk ID: `chunk_7ff10ed92cd6`
- Images: `images\G95E23857.gif`, `images\G95F23858.gif`
- Duplicate sources: `pages\17817.html`

### Full Text

````text
# Example #1 - Voltage Controlled Driver

These two known-good waveform patterns are from a Ford 4.6L V8 VIN [W]. Fig. Fig 1 illustrates the 64 volt inductive kick on this engine, indicating no clamping is occurring. The second pattern, Fig. Fig 2 , was taken during hot idle, closed loop, and no load.
````

## Chunk 8330: Example #2 - Voltage Controlled Driver

- Title: Example #2 - Voltage Controlled Driver
- Source path: `pages\10642.html`
- Chunk ID: `chunk_6c9030667d98`
- Images: `images\G95I23851.gif`
- Duplicate sources: `pages\17818.html`

### Full Text

````text
# Example #2 - Voltage Controlled Driver

The known-good waveform pattern in Fig. Fig 1 is from a GM 3.8L V6 PFI VIN [3]. It was taken during hot idle, closed loop and no load.
````

## Chunk 8331: Example #3 - Voltage Controlled Driver

- Title: Example #3 - Voltage Controlled Driver
- Source path: `pages\10643.html`
- Chunk ID: `chunk_ec52ebec480b`
- Images: `images\G95G23859.gif`
- Duplicate sources: `pages\17783.html`

### Full Text

````text
# Example #3 - Voltage Controlled Driver

This known-good waveform pattern, Fig. Fig 1 , is from a GM 5.0L V8 TPI VIN [F]. It was taken during hot idle, closed loop and no load.
````

## Chunk 8332: Example #4 - Current Controlled Driver

- Title: Example #4 - Current Controlled Driver
- Source path: `pages\10644.html`
- Chunk ID: `chunk_c6b3ddec7091`
- Images: `images\G95J23860.gif`
- Duplicate sources: `pages\17819.html`

### Full Text

````text
# Example #4 - Current Controlled Driver

From 1984 to 1987, Chrysler used this type injector drive on their TBI-equipped engines. See Fig 1 for a known-good pattern. Instead of the ground side controlling the injector, Chrysler permanently grounds out the injector and switches the power feed side. Most systems do not work this way.

These injectors peak at 6 amps of current flow and hold at 1 amp.
````

## Chunk 8333: Example #5 - Current Controlled Driver

- Title: Example #5 - Current Controlled Driver
- Source path: `pages\10645.html`
- Chunk ID: `chunk_ba5405aa06d4`
- Images: `images\G95A23861.gif`, `images\G95B23854.gif`
- Duplicate sources: `pages\17820.html`

### Full Text

````text
# Example #5 - Current Controlled Driver

These two known-good waveform patterns are from a Chrysler 3.0L V6 VIN [3]. The first waveform, Fig. Fig 1 , is a dual trace pattern that illustrates how Chrysler uses the rising edge of the engine speed signal to trigger the injectors. The second waveform, Fig. Fig 2 , was taken during hot idle, closed loop, and no load.
````

## Chunk 8334: Example #6 - Current Controlled Driver

- Title: Example #6 - Current Controlled Driver
- Source path: `pages\10646.html`
- Chunk ID: `chunk_dabb2d3be8c8`
- Images: `images\G95J23852.gif`
- Duplicate sources: `pages\17821.html`

### Full Text

````text
# Example #6 - Current Controlled Driver

This known-good pattern from a Ford 3.0L V6 PFI VIN [U] illustrates that a zener diode inside the computer is used to clamp the injector's inductive kick to 35-volts on this system. See Fig 1 .
````

## Chunk 8335: Example #7 - Current Controlled Driver

- Title: Example #7 - Current Controlled Driver
- Source path: `pages\10647.html`
- Chunk ID: `chunk_f750f2a94112`
- Images: `images\G95D23856.gif`
- Duplicate sources: `pages\17822.html`

### Full Text

````text
# Example #7 - Current Controlled Driver

This known-good waveform from a Ford 5.0L V8 CFI VIN [F] was taken during hot idle, closed loop, and no load. See Fig 1 .
````

## Chunk 8336: Example #8 - Current Controlled Driver

- Title: Example #8 - Current Controlled Driver
- Source path: `pages\10648.html`
- Chunk ID: `chunk_5fc07fd1cf02`
- Images: `images\G95D23849.gif`, `images\G95H23850.gif`
- Duplicate sources: `pages\17823.html`

### Full Text

````text
# Example #8 - Current Controlled Driver

These two known-good waveform patterns are from a GM 2.0L In-Line 4 VIN [1]. Fig. Fig 1 illustrates the 78 volt inductive spike that indicates a zener diode is not used. The second waveform, Fig. Fig 2 , was taken during hot idle, closed loop, and no load.
````

## Chunk 8337: Exhaust Systems: Notes

- Title: Exhaust Systems: Notes
- Source path: `pages\10649.html`
- Chunk ID: `chunk_a6d60b75165b`
- Images: none
- Duplicate sources: `pages\20403.html`

### Full Text

````text
# Exhaust Systems: Notes

These materials are confidential and are not to be disclosed to, or utilized by, any individual or entity other than participants of the Motorist Assurance Program (MAP).

The Automotive Maintenance and Repair Association (AMRA) and MAP do not warrant these materials or guarantee their accuracy, and AMRA and MAP assume no liability for errors.
````

## Chunk 8338: Catalytic Converters

- Title: Catalytic Converters
- Source path: `pages\10653.html`
- Chunk ID: `chunk_2e9111719438`
- Images: none
- Duplicate sources: `pages\20407.html`

### Full Text

````text
# Catalytic Converters

Condition | Code | Procedure

Air injection tube broken | A | Require repair or replacement of injection tube or replacement of catalytic converter

Air injection tube burnt | A | Require repair or replacement of injection tube or replacement of catalytic converter

Air injection tube leaking | A | Require repair or replacement of injection tube or replacement of catalytic converter

Air injection tube loose | A | Require repair or replacement of injection tube or replacement of catalytic converter

Air injection tube restricted | A | Require repair or replacement of injection tube or replacement of catalytic converter

Air injection tube threads damaged | A | Require repair or replacement of injection tube or replacement of catalytic converter

Air injection tube threads stripped (threads missing) | A | Require repair or replacement of injection tube or replacement of catalytic converter

Body Cracked | B | Require repair or replacement

Converter empty | A | Require repair or replacement

Converter fill plug missing | C | Require repair or replacement

Converter missing | C | Require repair or replacement

Exhaust gases leaking | A | Require repair or replacement

Flanges leaking | A | Require repair or replacement of flanges

Inlet pipes cracked | B | Require repair or replacement

Internal rattle (except pellet-type) | 2 | Further Inspection required

NOTE: If the converter is breaking up, suggest converter replacement. If an object has fallen into the converter, remove object

Mounting brackets that are part of converter broken | A | Require repair or replacement

Obvious overheating | Require testing of converter

NOTE: Overheating is caused by something other than the converter. Further diagnosis is required to determine the cause of the overheating.

Outlet pipes cracked | B | Require repair or replacement

Pieces of catalyst material found downstream | 1 | Suggest replacement

Plugged | A | Require replacement

NOTE: Determine cause and correct to ensure that new converter will not become plugged.

Testing has determined that existing converter has been lead-poisoned, contaminated or failed testing | A | Require repair or replacement
````

## Chunk 8339: Exhaust Connections

- Title: Exhaust Connections
- Source path: `pages\10655.html`
- Chunk ID: `chunk_1c0246966dfa`
- Images: none
- Duplicate sources: `pages\20409.html`

### Full Text

````text
# Exhaust Connections

Condition | Code | Procedure

Attaching hardware Incorrect | B | Require replacement of hardware

Clamp broken | A | Require replacement

Clamp Loose | A | Require repair or replacement

Clamp missing | C | Require replacement

Corroded, affecting structural integrity | 1 | Suggest replacement

Incorrect type (i.e. Flange, Ball & Socket, etc.) | B | Require replacement

Leaking | A | Require repair

Loose | A | Require repair
````

## Chunk 8340: Exhaust Systems: Hangers

- Title: Exhaust Systems: Hangers
- Source path: `pages\10656.html`
- Chunk ID: `chunk_4cc92c8a36ce`
- Images: none
- Duplicate sources: `pages\20410.html`

### Full Text

````text
# Exhaust Systems: Hangers

Condition | Code | Procedure

Broken | A | Require replacement

Corroded, affecting structural integrity | 1 | Suggest replacement

Incorrect type | B | Require replacement

Loose | B | Require repair or replacement

Missing | C | Require replacement

Out of position | B | Require repair or replacement

Rubber deteriorated | 1 | Suggest replacement
````

## Chunk 8341: Heat Risers (Mechanical EFE Devices)

- Title: Heat Risers (Mechanical EFE Devices)
- Source path: `pages\10657.html`
- Chunk ID: `chunk_312ac6d31c3a`
- Images: none
- Duplicate sources: `pages\20411.html`

### Full Text

````text
# Heat Risers (Mechanical EFE Devices)

Condition | Code | Procedure

Broken | A | Require replacement of affected parts

Diaphragm Inoperative | A | Require replacement

NOTE: If the inoperative diaphragm is separate from the heat riser, then require replacement of the inoperative diaphragm. If the inoperative diaphragm is part of the heat riser, then replace the heatriser

Leaking | B | Require repair or replacement

Noisy | 2 | Suggest repair or replacement of affected parts

Seized | A | Require repair or replacement of affected parts

Spring broken | B | Require replacement of spring(s)

Spring Inoperative | A | Require replacement of spring(s)
````

## Chunk 8342: Heat Shields

- Title: Heat Shields
- Source path: `pages\10658.html`
- Chunk ID: `chunk_9ea5913786aa`
- Images: none
- Duplicate sources: `pages\20412.html`

### Full Text

````text
# Heat Shields

Condition | Code | Procedure

Bent, affecting performance | B | Require repair or replacement

Broken | A | Require replacement

Corroded affecting structural integrity | 1 | Suggest replacement

Loose | B | Require repair or replacement

Missing | C | Require replacement
````

## Chunk 8343: Manifolds (Cast And Tube Type)

- Title: Manifolds (Cast And Tube Type)
- Source path: `pages\10659.html`
- Chunk ID: `chunk_6fbf89a15ad6`
- Images: none
- Duplicate sources: `pages\20413.html`

### Full Text

````text
# Manifolds (Cast And Tube Type)

Condition | Code | Procedure

Air injection tube in manifold broken | A | Require repair or replacement of injection tube or replacement of manifold

Air injection tube in manifold corroded, affecting structural integrity | 1 | Suggest replacement of Injection tube or manifold

Air injection tube in manifold leaking | A | Require repair or replacement of injection tube or replacement of manifold

Air injection tube in manifold loose | A | Require repair

Air injection tube in manifold restricted | A | Require replacement of injection tube or manifold

Air injection tube in manifold threads damaged | A | Require repair of injection tube or manifold

Air injection tube in manifold threads stripped (threads missing) | A | Require replacement of injection tube or manifold

Bolt Broken | A | Require replacement of bolt(s)

Bolt Loose | A | Require tightening or replacement of bolt(s)

Bolt Missing | C | Require replacement of bolt(s)

Corroded, affecting sealability | A | Require repair or replacement

Cylinder head threads stripped | A | Require repair or replacement of cylinder head

Gasket leaking | A | Require tightening or replacement of gasket

Heat Stove Bent | B | Require Repair Or Replacement of Stove

NOTE: Stove may not be available separately. This may require replacement of manifold.

Heat Stove Broken | A | Require replacement of stove

NOTE: Stove may not be available separately. This may require replacement of manifold.

Heat Stove Corroded, Affecting Structural Integrity | 1 | Suggest replacement of stove

NOTE: Stove may not be available separately. This may require replacement of manifold.

Heat Stove Missing | C | Require replacement of stove

NOTE: Stove may not be available separately. This may require replacement of manifold.

Manifold Broken | A | Require repair or replacement

Manifold Cracked | B | Require repair or replacement

Manifold Warped | A | Require repair or replacement

Out of specification | B | Require repair or replacement

Stud broken | A | Require replacement of stud

Stud missing | C | Require replacement of stud

Stud threads damaged | A | Require Repair Or Replacement of Stud

Stud threads stripped (threads missing) | A | Require replacement of stud
````

## Chunk 8344: Mechanical EFE Devices

- Title: Mechanical EFE Devices
- Source path: `pages\10660.html`
- Chunk ID: `chunk_f4cf71b4f59a`
- Images: none
- Duplicate sources: `pages\20414.html`

### Full Text

````text
# Mechanical EFE Devices

Condition | Code | Procedure

Broken | A | Require replacement of affected parts

Diaphragm Inoperative | A | Require replacement

NOTE: If the inoperative diaphragm is separate from the heat riser, then require replacement of the inoperative diaphragm. If the inoperative diaphragm is part of the heat riser, then replace the heatriser

Leaking | B | Require repair or replacement

Noisy | 2 | Suggest repair or replacement of affected parts

Seized | A | Require repair or replacement of affected arts

Spring broken | B | Require replacement of spring(s)

Spring Inoperative | A | Require replacement of spring(s)
````

## Chunk 8345: Muffler Valve

- Title: Muffler Valve
- Source path: `pages\10661.html`
- Chunk ID: `chunk_34a36e76b66d`
- Images: none
- Duplicate sources: `pages\20415.html`

### Full Text

````text
# Muffler Valve

Condition | Code | Procedure

Inoperative | A | Require repair or replacement

NOTE: It may be necessary to replace the muffler assembly to correct this condition.
````

## Chunk 8346: Mufflers And Resonators

- Title: Mufflers And Resonators
- Source path: `pages\10662.html`
- Chunk ID: `chunk_cd9f001441b2`
- Images: none
- Duplicate sources: `pages\20416.html`

### Full Text

````text
# Mufflers And Resonators

Condition | Code | Procedure

Body shell distorted, affecting performance or structural integrity | A | Require replacement

Corrosion Hole | A | Require replacement

Missing | C | Require replacement

Mounting bracket broken | A | Require repair or replacement

Mounting bracket cracked | B | Require repair or replacement

Nipple Cracked | A | Require repair or replacement

Nipple Loose | B | Require replacement

Outer wrap peeling (Exhaust Not Leaking) | 1 | Suggest replacement

Plugged | A | Require replacement

Puncture (other than drain hole) | A | Require replacement

Rattling or knocking noise from inside muffler | B | Require replacement

Seam open (exhaust leaking) | A | Require replacement

Sound quality unsatisfactory | 2 | Suggest replacement to address customer need and/or request

Split (exhaust leaking) | A | Require replacement

NOTE: Further diagnosis required to determine cause of the split seam (i.e. Backfiring).

Weak due to corrosion, but no leaks present | 1 | Suggest replacement
````

## Chunk 8347: Heating, Ventilation & Air Conditioning Systems: Notes

- Title: Heating, Ventilation & Air Conditioning Systems: Notes
- Source path: `pages\10664.html`
- Chunk ID: `chunk_5f4725716c4c`
- Images: none
- Duplicate sources: `pages\20320.html`

### Full Text

````text
# Heating, Ventilation & Air Conditioning Systems: Notes

These materials are confidential and are not to be disclosed to, or utilized by, any individual or entity other than participants of the Motorist Assurance Program (MAP).

The Automotive Maintenance and Repair Association (AMRA) and MAP do not warrant these materials or guarantee their accuracy, and AMRA and MAP assume no liability for errors.
````

## Chunk 8348: Heating, Ventilation & Air Conditioning Systems: Accumulators

- Title: Heating, Ventilation & Air Conditioning Systems: Accumulators
- Source path: `pages\10668.html`
- Chunk ID: `chunk_2b48410b56aa`
- Images: none
- Duplicate sources: `pages\20324.html`

### Full Text

````text
# Heating, Ventilation & Air Conditioning Systems: Accumulators

Condition | Code | Procedure

NOTE: When replacing this component it is suggested to install or replace high and low side inline filters to prevent future component damage (see Code 5).

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Beyond vehicle manufacturer's service interval | 3 | Suggest replacement

Desiccant at the end of its useful life (saturated with moisture) | 1 | Suggest repair or replacement

Desiccant bag deteriorated | A | Require replacement. Further inspection required

NOTE: Inspect system to determine effects of desiccant bag deterioration.

Leaking | A | Require repair or replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

Tubing connection leaking | A | Require repair or replacement
````

## Chunk 8349: Actuators (Electrical)

- Title: Actuators (Electrical)
- Source path: `pages\10669.html`
- Chunk ID: `chunk_42f125cc7ad1`
- Images: none
- Duplicate sources: `pages\20325.html`

### Full Text

````text
# Actuators (Electrical)

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector melted, not affecting performance | 2 | Suggest repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector missing | C | Require replacement

Inoperative | A | Require replacement

NOTE: Inoperative includes intermittent operation.

Missing | C | Require replacement

Noisy | 2 | Suggest repair or replacement

Out of adjustment | B | Require repair or replacement

Terminal broken | A | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement
````

## Chunk 8350: Actuators (Vacuum)

- Title: Actuators (Vacuum)
- Source path: `pages\10670.html`
- Chunk ID: `chunk_c0c102318461`
- Images: none
- Duplicate sources: `pages\20326.html`

### Full Text

````text
# Actuators (Vacuum)

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement.

Connector melted, not affecting performance | 2 | Suggest repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector missing | C | Require replacement

Inoperative | A | Require replacement

NOTE: Inoperative includes intermittent operation.

Leaking (vacuum) | A | Require repair or replacement

Linkage bent, affecting performance | A | Require repair or replacement of linkage

Linkage bent, not affecting performance | 2 | Suggest repair or replacement of linkage

Linkage binding, affecting performance | A | Require repair or replacement of linkage

Linkage binding, not affecting performance | 1 | Suggest repair or replacement of linkage

Linkage broken | A | Require repair or replacement of linkage

Linkage loose, affecting performance | A | Require repair or replacement of linkage

Linkage loose, not affecting performance | 1 | Suggest repair or replacement of linkage

Linkage missing | C | Require replacement

Linkage noisy | 2 | Suggest repair or replacement

Missing | C | Require replacement

Noisy | 2 | Suggest repair or replacement

Out of adjustment | B | Require repair or replacement
````

## Chunk 8351: Air Conditioning Fittings

- Title: Air Conditioning Fittings
- Source path: `pages\10671.html`
- Chunk ID: `chunk_14d3cc3a12a6`
- Images: none
- Duplicate sources: `pages\20327.html`

### Full Text

````text
# Air Conditioning Fittings

Condition | Code | Procedure

Abrasion damage, affecting structural integrity | A | Require repair or replacement

Abrasion damage, not affecting structural integrity | No service suggested or required

Application incorrect | B | Require replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Clamp corroded, not reusable | 1 | Suggest replacement

Connected incorrectly | A | Require replacement

Corroded, affecting structural integrity | A | Require replacement

Corroded, not affecting structural integrity | No service suggested or required

Cracked | A | Require repair or replacement

Fitting type incorrect (such as compression fitting) | B | Require replacement

Flange leaking | A | Require repair or replacement

Insufficient clamping force, allowing hose to leak | A | Require repair or replacement

Leaking | A | Require repair or replacement

Melted | 1 | Suggest repair or replacement

Missing | C | Require replacement

Outer covering damaged to the extent that the inner fabric is visible | A | Require replacement

Protective sleeves damaged | 2 | Suggest replacement of sleeves

Protective sleeves missing | C | Require replacement of sleeves

Restricted, affecting performance | A | Require repair or replacement

Routed incorrectly | B | Require repair

Swollen | 1 | Suggest replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

Type incorrect | 2 | Suggest repair or replacement
````

## Chunk 8352: Air Conditioning Hoses

- Title: Air Conditioning Hoses
- Source path: `pages\10672.html`
- Chunk ID: `chunk_20e9cb914f03`
- Images: none
- Duplicate sources: `pages\20328.html`

### Full Text

````text
# Air Conditioning Hoses

Condition | Code | Procedure

Abrasion damage, affecting structural integrity | A | Require repair or replacement

Abrasion damage, not affecting structural integrity | No service suggested or required

Application incorrect | B | Require replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Clamp corroded, not reusable | 1 | Suggest replacement

Connected incorrectly | A | Require replacement

Corroded, affecting structural integrity | A | Require replacement

Corroded, not affecting structural integrity | No service suggested or required

Cracked | A | Require repair or replacement

Fitting type incorrect (such as compression fitting) | B | Require replacement

Flange leaking | A | Require repair or replacement

Insufficient clamping force, allowing hose to leak | A | Require repair or replacement

Leaking | A | Require repair or replacement

Melted | 1 | Suggest repair or replacement

Missing | C | Require replacement

Outer covering damaged to the extent that the inner fabric is visible | A | Require replacement

Protective sleeves damaged | 2 | Suggest replacement of sleeves

Protective sleeves missing | C | Require replacement of sleeves

Restricted, affecting performance | A | Require repair or replacement

Routed incorrectly | B | Require repair

Swollen | 1 | Suggest replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

Type incorrect | 2 | Suggest repair or replacement
````

## Chunk 8353: Air Conditioning Metal Lines

- Title: Air Conditioning Metal Lines
- Source path: `pages\10673.html`
- Chunk ID: `chunk_27012ecf8f8e`
- Images: none
- Duplicate sources: `pages\20329.html`

### Full Text

````text
# Air Conditioning Metal Lines

Condition | Code | Procedure

Abrasion damage, affecting structural integrity | A | Require repair or replacement

Abrasion damage, not affecting structural integrity | No service suggested or required

Application incorrect | B | Require replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Clamp corroded, not reusable | 1 | Suggest replacement

Connected incorrectly | A | Require replacement

Corroded, affecting structural integrity | A | Require replacement

Corroded, not affecting structural integrity | No service suggested or required

Cracked | A | Require repair or replacement

Fitting type incorrect (such as compression fitting) | B | Require replacement

Flange leaking | A | Require repair or replacement

Insufficient clamping force, allowing hose to leak | A | Require repair or replacement

Leaking | A | Require repair or replacement

Melted | 1 | Suggest repair or replacement

Missing | C | Require replacement

Outer covering damaged to the extent that the inner fabric is visible | A | Require replacement

Protective sleeves damaged | 2 | Suggest replacement of sleeves

Protective sleeves missing | C | Require replacement of sleeves

Restricted, affecting performance | A | Require repair or replacement

Routed incorrectly | B | Require repair

Swollen | 1 | Suggest replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

Type incorrect | 2 | Suggest repair or replacement
````

## Chunk 8354: Air Control Doors

- Title: Air Control Doors
- Source path: `pages\10674.html`
- Chunk ID: `chunk_9f6fc0c8e506`
- Images: none
- Duplicate sources: `pages\20330.html`

### Full Text

````text
# Air Control Doors

Condition | Code | Procedure

Air control door binding | A | Require repair or replacement

Air control door broken | A | Require repair or replacement

Air control door leaking | A | Require repair or replacement

Air control door seized | A | Require repair or replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Cracked | 2 | Suggest repair or replacement

Drain hole restricted | A | Require repair

Drain plugged | A | Require repair

Duct disconnected | A | Require repair or replacement

Duct leaking | A | Require repair or replacement

Duct missing | C | Require replacement

Duct restricted | A | Require repair or replacement

Leaking | B | Require repair or replacement

Noisy | 2 | Suggest cleaning or repair

Odor | 2 | Suggest cleaning or repair

Restricted | A | Require cleaning, repair, or replacement
````

## Chunk 8355: Air Dams (External)

- Title: Air Dams (External)
- Source path: `pages\10675.html`
- Chunk ID: `chunk_37c43d6ee2e3`
- Images: none
- Duplicate sources: `pages\20331.html`

### Full Text

````text
# Air Dams (External)

Condition | Code | Procedure

Application incorrect, affecting air conditioning system performance | A | Require repair or replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Bent, affecting air conditioning system performance | A | Require repair or replacement

Blocked, affecting air conditioning system performance | A | Require repair or replacement

Broken, affecting air conditioning system performance | A | Require repair or replacement

Cracked, affecting air conditioning system performance | A | Require repair or replacement

Loose, affecting air conditioning system performance | A | Require repair

Loose, not affecting air conditioning system performance | 2 | Suggest repair

Missing, affecting air conditioning system performance | C | Require replacement
````

## Chunk 8356: Air Distribution System

- Title: Air Distribution System
- Source path: `pages\10676.html`
- Chunk ID: `chunk_f2e197dcfc6d`
- Images: none
- Duplicate sources: `pages\20332.html`

### Full Text

````text
# Air Distribution System

Condition | Code | Procedure

Air control door binding | A | Require repair or replacement

Air control door broken | A | Require repair or replacement

Air control door leaking | A | Require repair or replacement

Air control door seized | A | Require repair or replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Cracked | 2 | Suggest repair or replacement

Drain hole restricted | A | Require repair

Drain plugged | A | Require repair

Duct disconnected | A | Require repair or replacement

Duct leaking | A | Require repair or replacement

Duct missing | C | Require replacement

Duct restricted | A | Require repair or replacement

Leaking | B | Require repair or replacement

Noisy | 2 | Suggest cleaning or repair

Odor | 2 | Suggest cleaning or repair

Restricted | A | Require cleaning, repair, or replacement
````

## Chunk 8357: Heating, Ventilation & Air Conditioning Systems: Belts

- Title: Heating, Ventilation & Air Conditioning Systems: Belts
- Source path: `pages\10677.html`
- Chunk ID: `chunk_5155f9b29237`
- Images: none
- Duplicate sources: `pages\20333.html`

### Full Text

````text
# Heating, Ventilation & Air Conditioning Systems: Belts

Condition | Code | Procedure

Alignment incorrect | B | Further inspection required

NOTE: Determine cause of incorrect alignment and require repair.

Cracked | 1 | Suggest replacement

Frayed | 1 | Suggest replacement

Missing | C | Require replacement

Noisy | 2 | Further inspection required

NOTE: Determine cause of noise and suggest repair.

Plies separated | A | Require replacement

Serpentine belt routed incorrectly | B | Require repair

Tension out of specification | B | Require adjustment or replacement

Worn beyond adjustment range | B | Require replacement

Worn so it contacts bottom of pulley | A | Require replacement
````

## Chunk 8358: Blend Doors

- Title: Blend Doors
- Source path: `pages\10678.html`
- Chunk ID: `chunk_2b68cfe720d8`
- Images: none
- Duplicate sources: `pages\20334.html`

### Full Text

````text
# Blend Doors

Condition | Code | Procedure

Air control door binding | A | Require repair or replacement

Air control door broken | A | Require repair or replacement

Air control door leaking | A | Require repair or replacement

Air control door seized | A | Require repair or replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Cracked | 2 | Suggest repair or replacement

Drain hole restricted | A | Require repair

Drain plugged | A | Require repair

Duct disconnected | A | Require repair or replacement

Duct leaking | A | Require repair or replacement

Duct missing | C | Require replacement

Duct restricted | A | Require repair or replacement

Leaking | B | Require repair or replacement

Noisy | 2 | Suggest cleaning or repair

Odor | 2 | Suggest cleaning or repair

Restricted | A | Require cleaning, repair, or replacement
````

## Chunk 8359: Blower Fans (Blower Wheel Or Squirrel Cage)

- Title: Blower Fans (Blower Wheel Or Squirrel Cage)
- Source path: `pages\10679.html`
- Chunk ID: `chunk_d8d3b9906cca`
- Images: none
- Duplicate sources: `pages\20335.html`

### Full Text

````text
# Blower Fans (Blower Wheel Or Squirrel Cage)

Condition | Code | Procedure

Application incorrect | B | Require repair or replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Broken | A | Require replacement

Cracked | B | Require replacement

Distorted | A | Require replacement

Fins missing | C | Require replacement

Hub separated | A | Require replacement

Inoperative | A | Require replacement

NOTE: Inoperative includes intermittent operation.

Mounting loose | A | Require repair or replacement

Noisy | 2 | Suggest replacement

Out of balance | A | Require repair or replacement
````

## Chunk 8360: Blower Motors

- Title: Blower Motors
- Source path: `pages\10680.html`
- Chunk ID: `chunk_34b6f9d82c1a`
- Images: none
- Duplicate sources: `pages\20336.html`

### Full Text

````text
# Blower Motors

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector melted, not affecting performance | 2 | Suggest repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector missing | C | Require replacement

Current draw out of specification | B | Require repair or replacement

Inoperative | A | Require replacement

NOTE: Check fan motor/controls. Inoperative includes intermittent operation.

Missing | C | Require replacement

Motor speed insufficient | 2 | Suggest repair or replacement

Noisy | 2 | Suggest replacement

Rotation incorrect for application | B | Require repair or replacement

Terminal broken | A | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Vibration | 1 | Suggest replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead corroded | A | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8361: Blower Resistors

- Title: Blower Resistors
- Source path: `pages\10681.html`
- Chunk ID: `chunk_78a96b54f38f`
- Images: none
- Duplicate sources: `pages\20337.html`

### Full Text

````text
# Blower Resistors

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware,

Attaching hardware not functioning | A | Require repair or replacement of hardware

Conductor exposed | A | Require replacement

Connector broken | A | Require repair or replacement

Connector melted, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector melted, not affecting performance | 1 | Suggest repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector missing | C | Require replacement

Inoperative | A | Require replacement

NOTE: Inoperative includes intermittent operation.

Insulation overheated | A | Require replacement

Terminal broken | A | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement
````

## Chunk 8362: Blower Switches

- Title: Blower Switches
- Source path: `pages\10682.html`
- Chunk ID: `chunk_0727e1100e59`
- Images: none
- Duplicate sources: `pages\20338.html`

### Full Text

````text
# Blower Switches

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Binding, affecting performance | A | Require repair or replacement

Binding, not affecting performance | 2 | Suggest repair or replacement

Broken | A | Require repair or replacement

Burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Burned, not affecting performance | 2 | Suggest repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Cracked, affecting performance | A | Require repair or replacement

Cracked, not affecting performance | 1 | Suggest repair or replacement

Malfunctioning | A | Require repair or replacement

NOTE: Includes inoperative, intermittent operation, or failure to perform all functions.

Melted, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Melted, not affecting performance | 2 | Suggest repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Missing | C | Require replacement

NOTE: Missing includes high pressure cut-off switches not installed during a retrofit from R12 to 134a.

Out of adjustment | B | Require repair or replacement

Pressure switch leaking | A | Require repair or replacement

Terminal broken | A | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

Won't return | A | Require repair or replacement

Worn | 1 | Suggest replacement
````

## Chunk 8363: Circuit Breakers

- Title: Circuit Breakers
- Source path: `pages\10684.html`
- Chunk ID: `chunk_ecb322705fb8`
- Images: none
- Duplicate sources: `pages\20340.html`

### Full Text

````text
# Circuit Breakers

Condition | Code | Procedure

Application incorrect | B | Require replacement

Blown | A | Require replacement

NOTE: Determine cause and correct prior to replacement of part.

Corroded, affecting performance | A | Require repair or replacement

Corroded, not affecting performance | 2 | Suggest repair or replacement

Cracked, affecting performance | A | Require repair or replacement

Cracked, not affecting performance | 1 | Suggest repair or replacement

Inoperative | A | Require replacement

NOTE: Inoperative includes intermittent operation.

Insulation damaged, conductors exposed | A | Suggest repair or replacement

Missing | C | Require replacement

Routed incorrectly | B | Require repair

Secured incorrectly | B | Require repair

Terminal broken | A | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement
````

## Chunk 8364: Compressor Clutch Assemblies

- Title: Compressor Clutch Assemblies
- Source path: `pages\10685.html`
- Chunk ID: `chunk_e57fc5c221b9`
- Images: none
- Duplicate sources: `pages\20341.html`

### Full Text

````text
# Compressor Clutch Assemblies

Condition | Code | Procedure

Air gap incorrect | B | Require repair or replacement

Bearing seized | A | Require replacement of bearing or assembly

Bearing worn, affecting performance | A | Require replacement of bearing or assembly

Coil shows signs of overheating | 1 | Suggest replacement of coil

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to replacement of part.

Connector melted, not affecting performance | 2 | Suggest repair or replacement

NOTE: Determine cause and correct prior to replacement of part.

Connector missing | C | Require replacement

Hub broken | A | Require replacement

Hub cracked | B | Require replacement

Hub loose on shaft | A | Require replacement

Hub scored, affecting performance | A | Require replacement

Hub warped, affecting performance | A | Require replacement

Inoperative | A | Require repair or replacement

NOTE: Inoperative includes intermittent operation.

Noisy | 2 | Suggest repair or replacement

Slips | A | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Will not disengage | A | Require repair or replacement

Wire lead burned | A | Require repair or replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8365: Heating, Ventilation & Air Conditioning Systems: Compressors

- Title: Heating, Ventilation & Air Conditioning Systems: Compressors
- Source path: `pages\10686.html`
- Chunk ID: `chunk_e3a6093e1aca`
- Images: none
- Duplicate sources: `pages\20342.html`

### Full Text

````text
# Heating, Ventilation & Air Conditioning Systems: Compressors

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Bracket bent, affecting performance | A | Require repair or replacement

Bracket bent, not affecting performance | No service suggested or required

Bracket broken, affecting performance | A | Require replacement

Bracket broken, not affecting performance | No service suggested or required

Bracket corroded, affecting performance | A | Require repair or replacement

Bracket corroded, not affecting performance | 2 | Suggest repair or replacement

Bracket cracked, affecting performance | A | Require repair or replacement

Bracket cracked, not affecting performance | 1 | Suggest repair or replacement

Bracket holes elongated, affecting performance | A | Require repair or replacement

Bracket holes elongated, not affecting performance | No service suggested or required

Bracket loose, affecting performance | A | Require repair or replacement

Bracket loose, not affecting performance | 1 | Suggest repair or replacement

Bracket missing | C | Require replacement

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector melted, not affecting performance | 2 | Suggest repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector missing | C | Require replacement

Housing broken, affecting performance | A | Require repair or replacement

Housing broken, not affecting performance | No service suggested or required

Housing cracked, affecting performance | A | Require repair or replacement

Housing cracked, not affecting performance | 1 | Suggest repair or replacement

Inoperative | A | Require repair or replacement

NOTE: Inoperative includes intermittent operation.

Leaking | B | Require repair or replacement

Missing | C | Require replacement

Noisy | 2 | Suggest repair or replacement

NOTE: Compressor noise can also be caused by low oil level, state of charge, air contamination, or type of refrigerant.

Terminal broken | A | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

Tubing connection leaking | A | Require repair or replacement

Vibration | 1 | Suggest replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead corroded | A | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8366: Condenser Air Seals

- Title: Condenser Air Seals
- Source path: `pages\10687.html`
- Chunk ID: `chunk_1954365fc92c`
- Images: none
- Duplicate sources: `pages\20343.html`

### Full Text

````text
# Condenser Air Seals

Condition | Code | Procedure

Leaking | A | Require repair or replacement

Missing | C | Require replacement
````

## Chunk 8367: Condenser Fan Motors

- Title: Condenser Fan Motors
- Source path: `pages\10688.html`
- Chunk ID: `chunk_52b2eebb80b1`
- Images: none
- Duplicate sources: `pages\20344.html`

### Full Text

````text
# Condenser Fan Motors

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector melted, not affecting performance | 2 | Suggest repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector missing | C | Require replacement

Hydraulic fan motor leaking | A | Require repair or replacement

Inoperative | A | Require replacement

NOTE: Check fan motor/controls. Inoperative includes intermittent operation.

Missing | C | Require replacement

Noisy | 2 | Suggest replacement

Rotation incorrect for application | B | Require repair or replacement

Terminal broken | A | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Vibration | 1 | Suggest replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead corroded | A | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8368: Heating, Ventilation & Air Conditioning Systems: Condensers

- Title: Heating, Ventilation & Air Conditioning Systems: Condensers
- Source path: `pages\10689.html`
- Chunk ID: `chunk_fd6f588c4272`
- Images: none
- Duplicate sources: `pages\20345.html`

### Full Text

````text
# Heating, Ventilation & Air Conditioning Systems: Condensers

Condition | Code | Procedure

Abrasion damage, affecting structural integrity | A | Require repair or replacement

Abrasion damage, not affecting structural integrity | No service suggested or required

Air flow obstruction, affecting performance | A | Require repair or replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Bent, affecting performance | A | Require repair or replacement

Bent, not affecting performance | No service suggested or required

Bracket bent, affecting performance | A | Require repair or replacement

Bracket bent, not affecting performance | No service suggested or required

Bracket broken, affecting performance | A | Require replacement

Bracket broken, not affecting performance | No service suggested or required

Bracket corroded, affecting performance | A | Require repair or replacement

Bracket corroded, not affecting performance | 2 | Suggest repair or replacement

Bracket cracked, affecting performance | A | Require repair or replacement

Bracket cracked, not affecting performance | 1 | Suggest repair or replacement

Bracket holes elongated, affecting performance | A | Require repair or replacement

Bracket holes elongated, not affecting performance | No service suggested or required

Bracket loose, affecting performance | A | Require repair or replacement

Bracket loose, not affecting performance | 1 | Suggest repair or replacement

Bracket missing | C | Require replacement

Corroded, affecting structural integrity | A | Require replacement

Corroded, not affecting structural integrity | No service suggested or required

Fitting type incorrect (such as compression fitting) | B | Require replacement

Flange leaking | A | Require repair or replacement

Leaking | A | Require repair or replacement

Restricted internally | A | Require repair or replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement
````

## Chunk 8369: Heating, Ventilation & Air Conditioning Systems: Connectors

- Title: Heating, Ventilation & Air Conditioning Systems: Connectors
- Source path: `pages\10690.html`
- Chunk ID: `chunk_15ea80b500be`
- Images: none
- Duplicate sources: `pages\20346.html`

### Full Text

````text
# Heating, Ventilation & Air Conditioning Systems: Connectors

Condition | Code | Procedure

Application incorrect | B | Require repair or replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Circuit open | A | Require repair or replacement

Circuit resistance (voltage drop) out of specification | A | Require repair or replacement

Circuit shorted | A | Require repair or replacement

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector melted, not affecting performance | 2 | Suggest repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector missing | C | Require replacement

Diode open | A | Require repair or replacement

Diode shorted | A | Require repair or replacement

Insulation damaged, conductors exposed | A | Require repair or replacement

Insulation damaged, conductors not exposed | 1 | Suggest replacement

Protective shield (conduit) melted | 2 | Require replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Protective shield (conduit) missing | C | Require replacement

Routed incorrectly | B | Require repair

Secured incorrectly | B | Require repair

Terminal broken | A | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Voltage drop out of specification | A | Require repair or replacement
````

## Chunk 8370: Control Cables

- Title: Control Cables
- Source path: `pages\10691.html`
- Chunk ID: `chunk_9764b488c188`
- Images: none
- Duplicate sources: `pages\20347.html`

### Full Text

````text
# Control Cables

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Binding | A | Require repair or replacement

Bracket bent, affecting performance | A | Require repair or replacement

Bracket bent, not affecting performance | No service suggested or required

Bracket broken, affecting performance | A | Require replacement

Bracket broken, not affecting performance | No service suggested or required

Bracket Corroded, affecting performance | A | Require repair or replacement

Bracket corroded, not affecting performance | 2 | Suggest repair or replacement

Bracket cracked, affecting performance | A | Require repair or replacement

Bracket cracked, not affecting performance | 1 | Suggest repair or replacement

Bracket holes elongated, affecting performance | A | Require repair or replacement

Bracket holes elongated, not affecting performance | No service suggested or required

Bracket loose, affecting performance | A | Require repair or replacement

Bracket loose, not affecting performance | 1 | Suggest repair or replacement

Bracket missing | C | Require replacement

Broken | A | Require repair or replacement

Cracked | 2 | Suggest repair or replacement

Disconnected | A | Require repair or replacement

Kinked | 2 | Suggest repair or replacement

Melted | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Out of adjustment | B | Require repair or replacement

NOTE: Follow OEM recommended adjustment procedures. Require repair or replacement if out of specification.

Routed incorrectly | B | Suggest repair

Seized | A | Require repair or replacement
````

## Chunk 8371: Control Heads (Function Selectors)

- Title: Control Heads (Function Selectors)
- Source path: `pages\10692.html`
- Chunk ID: `chunk_49f7e322f64c`
- Images: none
- Duplicate sources: `pages\20348.html`

### Full Text

````text
# Control Heads (Function Selectors)

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector melted, not affecting performance | 2 | Suggest repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector missing | C | Require replacement

Contaminated | 2 | Suggest require replacement

Leaking | B | Require repair or replacement

Malfunctioning | A | Require repair or replacement

NOTE: Includes inoperative, intermittent operation, or failure to perform all functions.

Melted, affecting performance | A | Require repair or replacement

Melted, not affecting performance | No service suggested or required

Terminal broken | A | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Wire lead burned | A | Require repair or replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead open | A | Require repair or replacement
````

## Chunk 8372: Control Linkages

- Title: Control Linkages
- Source path: `pages\10693.html`
- Chunk ID: `chunk_7f6405b83f5d`
- Images: none
- Duplicate sources: `pages\20349.html`

### Full Text

````text
# Control Linkages

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Bent, affecting performance | A | Require repair or replacement

Binding | A | Require repair or replacement

Bracket bent, affecting performance | A | Require repair or replacement

Bracket bent, not affecting performance | No service suggested or required

Bracket broken, affecting performance | A | Require replacement

Bracket broken, not affecting performance | No service suggested or required

Bracket corroded, affecting performance | A | Require repair or replacement

Bracket corroded, not affecting performance | 2 | Suggest repair or replacement

Bracket cracked, affecting performance | A | Require repair or replacement

Bracket cracked, not affecting performance | 1 | Suggest repair or replacement

Bracket holes elongated, affecting performance | A | Require repair or replacement

Bracket holes elongated, not affecting performance | No service suggested or required

Bracket loose, affecting performance | A | Require repair or replacement

Bracket loose, not affecting performance | 1 | Suggest repair or replacement

Bracket missing | C | Require replacement

Broken | A | Require replacement

Cracked | B | Require repair or replacement

Disconnected | A | Require repair or replacement

Missing | C | Require replacement

Noisy | 2 | Suggest repair or replacement

Out of adjustment | B | Require repair or replacement

NOTE: Follow OEM recommended adjustment procedures. Require repair or replacement if out of specification.

Seized | A | Require repair or replacement
````

## Chunk 8373: Control Modules

- Title: Control Modules
- Source path: `pages\10694.html`
- Chunk ID: `chunk_41c5f775b5e1`
- Images: none
- Duplicate sources: `pages\20350.html`

### Full Text

````text
# Control Modules

Condition | Code | Procedure

Application incorrect | B | Require replacement

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require repair or replacement of hardware

Code set (if applicable) | A | Further inspection required

NOTE: Refer to manufacturer's diagnostic trouble code procedure and require repair or replacement of affected component(s).

Connector broken | A | Require repair or replacement

Connector melted, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector melted, not affecting performance | 2 | Suggest repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector missing | C | Require repair

Contaminated | A | Require repair or replacement

NOTE: Determine source of contamination, such as engine coolant, fuel, metal particles, or water. Require repair or replacement. Check for accepted cleaning procedure.

Inoperative | A | Require repair or replacement

NOTE: Inoperative includes intermittent operation. Some components may be serviceable.

Leaking | B | Require repair or replacement

Missing | C | Require replacement

Terminal broken | A | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead corroded | A | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8374: Heating, Ventilation & Air Conditioning Systems: Coolant

- Title: Heating, Ventilation & Air Conditioning Systems: Coolant
- Source path: `pages\10695.html`
- Chunk ID: `chunk_ee08d80e478e`
- Images: none
- Duplicate sources: `pages\20351.html`

### Full Text

````text
# Heating, Ventilation & Air Conditioning Systems: Coolant

Condition | Code | Procedure

Acidity (pH) incorrect | 1 | Suggest correction or replacement

At or beyond service interval | 3 | Suggest replacement

Contaminated | B | Require replacement or recycling. Further inspection required

NOTE: Determine source of contamination and require correction prior to coolant replacement.

Fluid discolored | No service suggested or required

NOTE: Further testing necessary to determine condition of fluid.

Level incorrect | B | Require filling to proper level

NOTE: Determine source of incorrect level and suggest repair.

Mixture incorrect | B | Require correction or replacement

Type incorrect | B | Require replacement
````

## Chunk 8375: Cooling Fan Blades

- Title: Cooling Fan Blades
- Source path: `pages\10696.html`
- Chunk ID: `chunk_1a8898de7195`
- Images: none
- Duplicate sources: `pages\20352.html`

### Full Text

````text
# Cooling Fan Blades

Condition | Code | Procedure

Application incorrect | B | Require replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Bent | A | Require replacement

Broken | A | Require replacement

Cracked | B | Require replacement

Loose | A | Require repair or replacement

Missing | C | Require replacement
````

## Chunk 8376: Cooling Fan Clutches

- Title: Cooling Fan Clutches
- Source path: `pages\10697.html`
- Chunk ID: `chunk_ecbf38b670e4`
- Images: none
- Duplicate sources: `pages\20353.html`

### Full Text

````text
# Cooling Fan Clutches

Condition | Code | Procedure

Application incorrect | B | Require replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Bearing noisy | A | Require replacement

Bearing worn | A | Require replacement

Fastener loose | A | Require repair or replacement of fastener

Inoperative | A | Require replacement

NOTE: Inoperative includes intermittent operation.

Leaking | B | Suggest replacement

Seized | A | Require replacement

Slips (insufficient fan speed) | A | Require replacement

Thermal control incorrect | B | Require repair or replacement
````

## Chunk 8377: Cooling Fan Motors

- Title: Cooling Fan Motors
- Source path: `pages\10698.html`
- Chunk ID: `chunk_f63e3e09e1e0`
- Images: none
- Duplicate sources: `pages\20354.html`

### Full Text

````text
# Cooling Fan Motors

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector melted, not affecting performance | 2 | Suggest repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector missing | C | Require replacement

Hydraulic fan motor leaking | A | Require repair or replacement

Inoperative | A | Require replacement

NOTE: Check fan motor/controls. Inoperative includes intermittent operation.

Missing | C | Require replacement

Noisy | 2 | Suggest replacement

Rotation incorrect for application | B | Require repair or replacement

Terminal broken | A | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Vibration | 1 | Suggest replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead corroded | A | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8378: Evaporator Pressure Regulators (EPRS)

- Title: Evaporator Pressure Regulators (EPRS)
- Source path: `pages\10701.html`
- Chunk ID: `chunk_31cf8b6aa0d6`
- Images: none
- Duplicate sources: `pages\20357.html`

### Full Text

````text
# Evaporator Pressure Regulators (EPRS)

Condition | Code | Procedure

Inoperative | A | Require repair or replacement

NOTE: Inoperative includes intermittent operation.
````

## Chunk 8379: Heating, Ventilation & Air Conditioning Systems: Evaporators

- Title: Heating, Ventilation & Air Conditioning Systems: Evaporators
- Source path: `pages\10702.html`
- Chunk ID: `chunk_dfcdc7141062`
- Images: none
- Duplicate sources: `pages\20358.html`

### Full Text

````text
# Heating, Ventilation & Air Conditioning Systems: Evaporators

Condition | Code | Procedure

Abrasion damage, affecting structural integrity | A | Require repair or replacement

Abrasion damage, not affecting structural integrity | No service suggested or required

Air flow obstruction, affecting performance | A | Require repair or replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Bracket bent, affecting performance | A | Require repair or replacement

Bracket bent, not affecting performance | No service suggested or required

Bracket broken, affecting performance | A | Require replacement

Bracket broken, not affecting performance | No service suggested or required

Bracket corroded, affecting performance | A | Require repair or replacement

Bracket corroded, not affecting performance | 2 | Suggest repair or replacement

Bracket cracked, affecting performance | A | Require repair or replacement

Bracket cracked, not affecting performance | 1 | Suggest repair or replacement

Bracket holes elongated, affecting performance | A | Require repair or replacement

Bracket holes elongated, not affecting performance | No service suggested or required

Bracket loose, affecting performance | A | Require repair or replacement

Bracket loose, not affecting performance | 1 | Suggest repair or replacement

Bracket missing | C | Require replacement

Corroded, affecting structural integrity | A | Require replacement

Corroded, not affecting structural integrity | No service suggested or required

Evaporator foam seal leaking | A | Require replacement

Evaporator foam seal missing | C | Require replacement

Fitting type incorrect (such as compression fitting) | B | Require replacement

Flange leaking | A | Require repair or replacement

Leaking | B | Require repair or replacement

Microbial growth causing odor | 2 | Suggest microbial odor removal

NOTE: If the evaporator case is contaminated with debris, it may be necessary to remove the debris before applying microbial odor treatment.

Restricted internally | A | Require repair or replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement
````

## Chunk 8380: Expansion Valves

- Title: Expansion Valves
- Source path: `pages\10703.html`
- Chunk ID: `chunk_152a1352b0eb`
- Images: none
- Duplicate sources: `pages\20359.html`

### Full Text

````text
# Expansion Valves

Condition | Code | Procedure

Application incorrect | B | Require replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Corroded internally | 1 | Suggest replacement

Filter screen torn | A | Require replacement of screen

Inoperative | A | Require repair or replacement

NOTE: Expansion valve operation may be affected by capillary tube location, corrosion, and insulation tape. Inoperative includes intermittent operation.

Leaking | B | Require replacement

Restricted | A | Require repair or replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement
````

## Chunk 8381: Function Selectors

- Title: Function Selectors
- Source path: `pages\10704.html`
- Chunk ID: `chunk_845f75b7c0f0`
- Images: none
- Duplicate sources: `pages\20360.html`

### Full Text

````text
# Function Selectors

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector melted, not affecting performance | 2 | Suggest repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector missing | C | Require replacement

Contaminated | 2 | Suggest require replacement

Leaking | B | Require repair or replacement

Malfunctioning | A | Require repair or replacement

NOTE: Includes inoperative, intermittent operation, or failure to perform all functions.

Melted, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Melted, not affecting performance | No service suggested or required

Terminal broken | A | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Wire lead burned | A | Require repair or replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8382: Fuses, Fusible Links And Circuit Breakers

- Title: Fuses, Fusible Links And Circuit Breakers
- Source path: `pages\10705.html`
- Chunk ID: `chunk_af484524d188`
- Images: none
- Duplicate sources: `pages\20361.html`

### Full Text

````text
# Fuses, Fusible Links And Circuit Breakers

Condition | Code | Procedure

Application incorrect | B | Require replacement

Blown | A | Require replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Corroded, affecting performance | A | Require repair or replacement

Corroded, not affecting performance | 2 | Suggest repair or replacement

Cracked, affecting performance | A | Require repair or replacement

Cracked, not affecting performance | 1 | Suggest repair or replacement

Inoperative | A | Require replacement

NOTE: Inoperative includes intermittent operation.

Insulation damaged, conductors exposed | A | Suggest repair or replacement

Missing | C | Require replacement

Routed incorrectly | B | Require repair

Secured incorrectly | B | Require repair

Terminal broken | A | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement
````

## Chunk 8383: Fusible Links

- Title: Fusible Links
- Source path: `pages\10706.html`
- Chunk ID: `chunk_c964f1054e52`
- Images: none
- Duplicate sources: `pages\20362.html`

### Full Text

````text
# Fusible Links

Condition | Code | Procedure

Application incorrect | B | Require replacement

Blown | A | Require replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Corroded, affecting performance | A | Require repair or replacement

Corroded, not affecting performance | 2 | Suggest repair or replacement

Cracked, affecting performance | A | Require repair or replacement

Cracked, not affecting performance | 1 | Suggest repair or replacement

Inoperative | A | Require replacement

NOTE: Inoperative includes intermittent operation.

Insulation damaged, conductors exposed | A | Suggest repair or replacement

Missing | C | Require replacement

Routed incorrectly | B | Require repair

Secured incorrectly | B | Require repair

Terminal broken | A | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement
````

## Chunk 8384: Heating, Ventilation & Air Conditioning Systems: Gaskets

- Title: Heating, Ventilation & Air Conditioning Systems: Gaskets
- Source path: `pages\10707.html`
- Chunk ID: `chunk_22aaa39141e2`
- Images: none
- Duplicate sources: `pages\20363.html`

### Full Text

````text
# Heating, Ventilation & Air Conditioning Systems: Gaskets

Condition | Code | Procedure

Leaking | A | Require repair or replacement

NOTE: Require inspection of mating and sealing surface and repair or replace as necessary.
````

## Chunk 8385: Heater Cases

- Title: Heater Cases
- Source path: `pages\10708.html`
- Chunk ID: `chunk_d9804e7664b9`
- Images: none
- Duplicate sources: `pages\20364.html`

### Full Text

````text
# Heater Cases

Condition | Code | Procedure

Air control door binding | A | Require repair or replacement

Air control door broken | A | Require repair or replacement

Air control door leaking | A | Require repair or replacement

Air control door seized | A | Require repair or replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Cracked | 2 | Suggest repair or replacement

Drain hole restricted | A | Require repair

Drain plugged | A | Require repair

Duct disconnected | A | Require repair or replacement

Duct leaking | A | Require repair or replacement

Duct missing | C | Require replacement

Duct restricted | A | Require repair or replacement

Leaking | B | Require repair or replacement

Microbial growth causing odor | 2 | Suggest microbial odor removal

NOTE: If the heater case is contaminated with debris, it may be necessary to remove the debris before applying microbial odor treatment.

Noisy | 2 | Suggest cleaning or repair

Restricted | A | Require cleaning, repair, or replacement
````

## Chunk 8386: Heater Control Valves

- Title: Heater Control Valves
- Source path: `pages\10709.html`
- Chunk ID: `chunk_e81f274fe26f`
- Images: none
- Duplicate sources: `pages\20365.html`

### Full Text

````text
# Heater Control Valves

Condition | Code | Procedure

Application incorrect | B | Require replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Binding | 2 | Suggest repair or replacement

Coolant leak | A | Require repair or replacement

Disconnected | A | Require repair or replacement

Malfunctioning | A | Require repair or replacement

NOTE: Includes inoperative, intermittent operation, or failure to perform all functions.

Missing | C | Require replacement

Restricted | A | Require repair or replacement

Seized | A | Require repair or replacement

Vacuum leak | A | Require repair or replacement
````

## Chunk 8387: Heater Cores

- Title: Heater Cores
- Source path: `pages\10710.html`
- Chunk ID: `chunk_4241f04660bc`
- Images: none
- Duplicate sources: `pages\20366.html`

### Full Text

````text
# Heater Cores

Condition | Code | Procedure

Air flow obstruction | A | Require repair or replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Connection leaking | A | Require repair or replacement

Corroded | 1 | Suggest repair or replacement

Disconnected | A | Require repair or replacement

Fins damaged, affecting performance | A | Require repair or replacement

Fins damaged, not affecting performance | No service suggested or required

Internal restrictions, affecting performance | A | Require repair or replacement

Leaking | B | Require repair or replacement

Missing | C | Require replacement
````

## Chunk 8388: Heater Hoses

- Title: Heater Hoses
- Source path: `pages\10711.html`
- Chunk ID: `chunk_0a0e8b32313f`
- Images: none
- Duplicate sources: `pages\20367.html`

### Full Text

````text
# Heater Hoses

Condition | Code | Procedure

Application incorrect | B | Require replacement

At or beyond service interval | 3 | Suggest replacement

Connected incorrectly | A | Require repair

Corroded, not reusable | 1 | Suggest replacement

Cracked | B | Require repair or replacement

Hard (brittle) | 1 | Suggest repair or replacement

Inner fabric (webbing) damaged | A | Require replacement

Insufficient clamping force, allowing hose to leak | A | Require repair or replacement

Leaking | A | Require repair or replacement

Melted | 1 | Suggest repair or replacement

Missing | C | Require replacement

Outer covering damaged | 1 | Suggest replacement

Outer covering damaged to the extent that the inner fabric is visible | A | Require replacement

Protective sleeves damaged | 2 | Suggest replacement of sleeves

Protective sleeves missing | C | Suggest replacement of sleeves

Restricted, affecting performance | A | Require repair or replacement

Restricted, not affecting performance | 2 | Suggest repair or replacement

Routed incorrectly | B | Suggest repair

Safety clip missing | C | Require replacement

Spongy | 1 | Suggest repair or replacement

Stripped | A | Require replacement

Surface cracks (dry-rotted) | 1 | Suggest repair or replacement

Swollen | B | Require replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

Type incorrect | 2 | Suggest repair or replacement
````

## Chunk 8389: High Pressure Relief Valves (HPRV)

- Title: High Pressure Relief Valves (HPRV)
- Source path: `pages\10712.html`
- Chunk ID: `chunk_0a215e6e36eb`
- Images: none
- Duplicate sources: `pages\20368.html`

### Full Text

````text
# High Pressure Relief Valves (HPRV)

Condition | Code | Procedure

Inoperative | A | Require repair or replacement

NOTE: Inoperative includes intermittent operation.

Leaking | A | Require repair or replacement

Missing | C | Require replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement
````

## Chunk 8390: Heating, Ventilation & Air Conditioning Systems: Idlers

- Title: Heating, Ventilation & Air Conditioning Systems: Idlers
- Source path: `pages\10713.html`
- Chunk ID: `chunk_7682769f9855`
- Images: none
- Duplicate sources: `pages\20369.html`

### Full Text

````text
# Heating, Ventilation & Air Conditioning Systems: Idlers

Condition | Code | Procedure

Alignment incorrect | B | Require repair or replacement

Application incorrect | B | Require replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Bearing worn | 1 | Suggest replacement

Belt tension incorrect | B | Require adjustment or repair

Bracket cracked | A | Require repair or replacement

Housing cracked | A | Require repair or replacement

Missing | C | Require replacement

Noisy | 2 | Suggest replacement

Pulley damaged, affecting belt life | A | Require replacement

Seized | A | Require repair or replacement
````

## Chunk 8391: Metal Fittings

- Title: Metal Fittings
- Source path: `pages\10715.html`
- Chunk ID: `chunk_eb9d3237baf1`
- Images: none
- Duplicate sources: `pages\20371.html`

### Full Text

````text
# Metal Fittings

Condition | Code | Procedure

Abrasion damage, affecting structural integrity | A | Require repair or replacement

Abrasion damage, not affecting structural integrity | No service suggested or required

Application incorrect | B | Require replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Clamp corroded, not reusable | 1 | Suggest replacement

Connected incorrectly | A | Require replacement

Corroded, affecting structural integrity | A | Require replacement

Corroded, not affecting structural integrity | No service suggested or required

Cracked | B | Require repair or replacement

Fitting type incorrect (such as compression fitting) | B | Require replacement

Flange leaking | A | Require repair or replacement

Insufficient clamping force, allowing hose to leak | A | Require repair or replacement

Leaking | B | Require repair or replacement

Melted | 1 | Suggest repair or replacement

Missing | C | Require replacement

Outer covering damaged to the extent that the inner fabric is visible | A | Require replacement

Protective sleeves damaged | 2 | Suggest replacement of sleeves

Protective sleeves missing | C | Require replacement of sleeves

Restricted, affecting performance | A | Require repair or replacement

Routed incorrectly | B | Require repair

Swollen | 1 | Suggest replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

Type incorrect | 2 | Suggest repair or replacement
````

## Chunk 8392: Metal Lines

- Title: Metal Lines
- Source path: `pages\10716.html`
- Chunk ID: `chunk_eb84aef92e60`
- Images: none
- Duplicate sources: `pages\20372.html`

### Full Text

````text
# Metal Lines

Condition | Code | Procedure

Abrasion damage, affecting structural integrity | A | Require repair or replacement

Abrasion damage, not affecting structural integrity | No service suggested or required

Application incorrect | B | Require replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Clamp corroded, not reusable | 1 | Suggest replacement

Connected incorrectly | A | Require replacement

Corroded, affecting structural integrity | A | Require replacement

Corroded, not affecting structural integrity | No service suggested or required

Cracked | B | Require repair or replacement

Fitting type incorrect (such as compression fitting) | B | Require replacement

Flange leaking | A | Require repair or replacement

Insufficient clamping force, allowing hose to leak | A | Require repair or replacement

Leaking | A | Require repair or replacement

Melted | 1 | Suggest repair or replacement

Missing | C | Require replacement

Outer covering damaged to the extent that the inner fabric is visible | A | Require replacement

Protective sleeves damaged | 2 | Suggest replacement of sleeves

Protective sleeves missing | C | Require replacement of sleeves

Restricted, affecting performance | A | Require repair or replacement

Swollen | 1 | Suggest replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

Type incorrect | 2 | Suggest repair or replacement
````

## Chunk 8393: Mix And Air Control Doors (Blend Doors)

- Title: Mix And Air Control Doors (Blend Doors)
- Source path: `pages\10717.html`
- Chunk ID: `chunk_46ee58fabc59`
- Images: none
- Duplicate sources: `pages\20373.html`

### Full Text

````text
# Mix And Air Control Doors (Blend Doors)

Condition | Code | Procedure

Air control door binding | A | Require repair or replacement

Air control door broken | A | Require repair or replacement

Air control door leaking | A | Require repair or replacement

Air control door seized | A | Require repair or replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Cracked | 2 | Suggest repair or replacement

Drain hole restricted | A | Require repair

Drain plugged | A | Require repair

Duct disconnected | A | Require repair or replacement

Duct leaking | A | Require repair or replacement

Duct missing | C | Require replacement

Duct restricted | A | Require repair or replacement

Leaking | B | Require repair or replacement

Noisy | 2 | Suggest cleaning or repair

Odor | 2 | Suggest cleaning or repair

Restricted | A | Require cleaning, repair, or replacement
````

## Chunk 8394: ORIFACE Tubes

- Title: ORIFACE Tubes
- Source path: `pages\10718.html`
- Chunk ID: `chunk_e21524f6c09a`
- Images: none
- Duplicate sources: `pages\20374.html`

### Full Text

````text
# ORIFACE Tubes

Condition | Code | Procedure

Application incorrect | B | Require replacement

Bypassing internally | A | Require repair or replacement

Filter screen torn | A | Require replacement

Installation incorrect | B | Require repair

Restricted | A | Require repair or replacement
````

## Chunk 8395: Heating, Ventilation & Air Conditioning Systems: O-Rings

- Title: Heating, Ventilation & Air Conditioning Systems: O-Rings
- Source path: `pages\10719.html`
- Chunk ID: `chunk_216776c0fea9`
- Images: none
- Duplicate sources: `pages\20375.html`

### Full Text

````text
# Heating, Ventilation & Air Conditioning Systems: O-Rings

Condition | Code | Procedure

Leaking | A | Require repair or replacement

NOTE: Require inspection of mating and sealing surface and repair or replace as necessary.
````

## Chunk 8396: Pilot-Operated Absolutes (POAS)

- Title: Pilot-Operated Absolutes (POAS)
- Source path: `pages\10720.html`
- Chunk ID: `chunk_35e0cab227a9`
- Images: none
- Duplicate sources: `pages\20376.html`

### Full Text

````text
# Pilot-Operated Absolutes (POAS)

Condition | Code | Procedure

Connection damaged | B | Require repair or replacement

Fitting damaged | B | Require repair or replacement

Inoperative | A | Require repair or replacement

NOTE: Inoperative includes intermittent operation.

Leaking | B | Require repair or replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

Threads stripped (threads missing) | A | Require replacement
````

## Chunk 8397: Heating, Ventilation & Air Conditioning Systems: Plenums

- Title: Heating, Ventilation & Air Conditioning Systems: Plenums
- Source path: `pages\10721.html`
- Chunk ID: `chunk_29a0a2be5352`
- Images: none
- Duplicate sources: `pages\20377.html`

### Full Text

````text
# Heating, Ventilation & Air Conditioning Systems: Plenums

Condition | Code | Procedure

Air control door binding | A | Require repair or replacement

Air control door broken | A | Require repair or replacement

Air control door leaking | A | Require repair or replacement

Air control door seized | A | Require repair or replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Cracked | 2 | Suggest repair or replacement

Drain hole restricted | A | Require repair

Drain plugged | A | Require repair

Duct disconnected | A | Require repair or replacement

Duct leaking | A | Require repair or replacement

Duct missing | C | Require replacement

Duct restricted | A | Require repair or replacement

Leaking | B | Require repair or replacement

Noisy | 2 | Suggest cleaning or repair

Odor | 2 | Suggest cleaning or repair

Restricted | A | Require cleaning, repair, or replacement
````

## Chunk 8398: Pressure Control Valves

- Title: Pressure Control Valves
- Source path: `pages\10722.html`
- Chunk ID: `chunk_9408c92e4b65`
- Images: none
- Duplicate sources: `pages\20378.html`

### Full Text

````text
# Pressure Control Valves

Condition | Code | Procedure

Connection damaged | B | Require repair or replacement

Fitting damaged | B | Require repair or replacement

Inoperative | A | Require repair or replacement

NOTE: Inoperative includes intermittent operation.

Leaking | B | Require repair or replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement
````

## Chunk 8399: Pressure Sensors

- Title: Pressure Sensors
- Source path: `pages\10723.html`
- Chunk ID: `chunk_c5095749123c`
- Images: none
- Duplicate sources: `pages\20379.html`

### Full Text

````text
# Pressure Sensors

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Calibration incorrect | B | Require repair or replacement

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector melted, not affecting performance | 2 | Suggest repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector missing | C | Require replacement

Inoperative | A | Require repair or replacement

NOTE: Inoperative includes intermittent operation.

Missing | C | Require replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Wire lead burned | A | Require repair or replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8400: Heating, Ventilation & Air Conditioning Systems: Pulleys

- Title: Heating, Ventilation & Air Conditioning Systems: Pulleys
- Source path: `pages\10724.html`
- Chunk ID: `chunk_bc08911f712c`
- Images: none
- Duplicate sources: `pages\20380.html`

### Full Text

````text
# Heating, Ventilation & Air Conditioning Systems: Pulleys

Condition | Code | Procedure

Alignment incorrect | B | Require repair or replacement

Application incorrect | B | Require replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Bearing noisy | 2 | Suggest replacement

Bearing seized | A | Require repair or replacement

Bearing worn | 1 | Suggest replacement

Cracked | B | Require replacement

Loose | B | Require repair or replacement

Missing | C | Require replacement

Pulley damaged, affecting belt life | A | Require replacement
````

## Chunk 8401: Heating, Ventilation & Air Conditioning Systems: Radiators

- Title: Heating, Ventilation & Air Conditioning Systems: Radiators
- Source path: `pages\10725.html`
- Chunk ID: `chunk_054d51991df5`
- Images: none
- Duplicate sources: `pages\20381.html`

### Full Text

````text
# Heating, Ventilation & Air Conditioning Systems: Radiators

Condition | Code | Procedure

Air flow obstruction | A | Require repair

Application incorrect | B | Require replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Connection leaking | A | Require repair or replacement

Corroded | 1 | Suggest repair or replacement

Drain inoperative | A | Require repair or replacement

Fins damaged, affecting performance | A | Require repair or replacement

Fins damaged, not affecting performance | No service suggested or required

Internal oil cooler leaking | A | Require repair or replacement

Internal restrictions | B | Require repair or replacement

Leaking | B | Require repair or replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require repair or replacement

Tubes damaged, affecting performance | A | Require repair or replacement

Tubes damaged, not affecting performance | No service suggested or required
````

## Chunk 8402: Heating, Ventilation & Air Conditioning Systems: Receiver-DRIERS

- Title: Heating, Ventilation & Air Conditioning Systems: Receiver-DRIERS
- Source path: `pages\10726.html`
- Chunk ID: `chunk_3de5fb6916c1`
- Images: none
- Duplicate sources: `pages\20382.html`

### Full Text

````text
# Heating, Ventilation & Air Conditioning Systems: Receiver-DRIERS

Condition | Code | Procedure

damage (see Code 5).

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Contaminated, affecting performance | A | Require replacement

Desiccant at the end of its useful life (saturated with moisture) | 1 | Suggest repair or replacement

Desiccant bag deteriorated | A | Require replacement. Further inspection required

NOTE: Inspect system to determine effects of desiccant bag deterioration.

Fusible plug leaking | A | Require replacement of plug

Leaking | B | Require replacement

Pressure relief device leaking | A | Require replacement of pressure relief device

Restricted | A | Require repair or replacement

Sight glass no longer transparent | 2 | Suggest replacement of drier

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

Tubing connection leaking | A | Require repair or replacement
````

## Chunk 8403: Refrigerant Oil

- Title: Refrigerant Oil
- Source path: `pages\10727.html`
- Chunk ID: `chunk_405df659f1bf`
- Images: none
- Duplicate sources: `pages\20383.html`

### Full Text

````text
# Refrigerant Oil

Condition | Code | Procedure

Contaminated | A | Require repair or replacement

Overfilled | B | Require repair

Underfilled | B | Require repair
````

## Chunk 8404: Heating, Ventilation & Air Conditioning Systems: Refrigerant

- Title: Heating, Ventilation & Air Conditioning Systems: Refrigerant
- Source path: `pages\10728.html`
- Chunk ID: `chunk_a13c712f74e6`
- Images: none
- Duplicate sources: `pages\20384.html`

### Full Text

````text
# Heating, Ventilation & Air Conditioning Systems: Refrigerant

Condition | Code | Procedure

Contaminated (other than refrigerant blends) | B | Require service to remove contamination

Different types of refrigerants in the same system (other than refrigerant blends) | B | Require repair

Overcharged | B | Require repair

Refrigerant type does not match fittings and label | B | Require repair

Undercharged | B | Require repair
````

## Chunk 8405: Heating, Ventilation & Air Conditioning Systems: Relays

- Title: Heating, Ventilation & Air Conditioning Systems: Relays
- Source path: `pages\10729.html`
- Chunk ID: `chunk_cd97857d0dae`
- Images: none
- Duplicate sources: `pages\20385.html`

### Full Text

````text
# Heating, Ventilation & Air Conditioning Systems: Relays

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Housing broken | A | Require replacement

Housing cracked | 2 | Suggest replacement

Inoperative | A | Require replacement

NOTE: Inoperative includes intermittent operation.

Melted, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Melted, not affecting performance | 2 | Suggest repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Missing | C | Require replacement

Terminal broken | A | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement
````

## Chunk 8406: Heating, Ventilation & Air Conditioning Systems: Seals

- Title: Heating, Ventilation & Air Conditioning Systems: Seals
- Source path: `pages\10730.html`
- Chunk ID: `chunk_83eb3d6a3d8b`
- Images: none
- Duplicate sources: `pages\20386.html`

### Full Text

````text
# Heating, Ventilation & Air Conditioning Systems: Seals

Condition | Code | Procedure

Leaking | A | Require repair or replacement

NOTE: Require inspection of mating and sealing surface and repair or replace as necessary.
````

## Chunk 8407: Service Ports

- Title: Service Ports
- Source path: `pages\10731.html`
- Chunk ID: `chunk_f423163047f1`
- Images: none
- Duplicate sources: `pages\20387.html`

### Full Text

````text
# Service Ports

Condition | Code | Procedure

Application does not match refrigerant type | B | Require replacement

Leaking | A | Require repair or replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

Valve cap leaking | A | Require repair or replacement of cap

Valve cap missing | C | Require replacement of valve cap

Valve core sticking | B | Require repair or replacement
````

## Chunk 8408: Spring Lock Couplings

- Title: Spring Lock Couplings
- Source path: `pages\10732.html`
- Chunk ID: `chunk_ff9e03fbd5d7`
- Images: none
- Duplicate sources: `pages\20388.html`

### Full Text

````text
# Spring Lock Couplings

Condition | Code | Procedure

Leaking | A | Require repair or replacement

NOTE: Require inspection of mating and sealing surface and repair or replace as necessary.
````

## Chunk 8409: Suction Throttling Valves (STVS)

- Title: Suction Throttling Valves (STVS)
- Source path: `pages\10733.html`
- Chunk ID: `chunk_2cdb75bd2266`
- Images: none
- Duplicate sources: `pages\20389.html`

### Full Text

````text
# Suction Throttling Valves (STVS)

Condition | Code | Procedure

Connection damaged | B | Require repair or replacement

Fitting damaged | B | Require repair or replacement

Inoperative | A | Require repair or replacement

NOTE: Inoperative includes intermittent operation.

Leaking | B | Require repair or replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement
````

## Chunk 8410: Switches (Electrical)

- Title: Switches (Electrical)
- Source path: `pages\10734.html`
- Chunk ID: `chunk_0ad0c8441908`
- Images: none
- Duplicate sources: `pages\20390.html`

### Full Text

````text
# Switches (Electrical)

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Binding, affecting performance | A | Require repair or replacement

Binding, not affecting performance | 2 | Suggest repair or replacement

Broken | A | Require repair or replacement

Burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Burned, not affecting performance | 2 | Suggest repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Cracked, affecting performance | A | Require repair or replacement

Cracked, not affecting performance | 1 | Suggest repair or replacement

Malfunctioning | A | Require repair or replacement

NOTE: Includes inoperative, intermittent operation, or failure to perform all functions.

Melted, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Melted, not affecting performance | 2 | Suggest repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Missing | C | Require replacement

NOTE: Missing includes high pressure cut-off switches not installed during a retrofit from R12 to 134a.

Out of adjustment | B | Require repair or replacement

Pressure switch leaking | A | Require repair or replacement

Terminal broken | A | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

Won't return | A | Require repair or replacement

Worn | 1 | Suggest replacement
````

## Chunk 8411: Heating, Ventilation & Air Conditioning Systems: TENSIONERS

- Title: Heating, Ventilation & Air Conditioning Systems: TENSIONERS
- Source path: `pages\10735.html`
- Chunk ID: `chunk_796885474241`
- Images: none
- Duplicate sources: `pages\20391.html`

### Full Text

````text
# Heating, Ventilation & Air Conditioning Systems: TENSIONERS

Condition | Code | Procedure

Alignment incorrect | B | Require repair or replacement

Application incorrect | B | Require replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Bearing worn | 1 | Suggest replacement

Belt tension incorrect | B | Require adjustment or repair

Bracket cracked | A | Require repair or replacement

Housing cracked | B | Require repair or replacement

Missing | C | Require replacement

Noisy | 2 | Suggest replacement

Pulley damaged, affecting belt life | A | Require replacement

Seized | A | Require repair or replacement
````

## Chunk 8412: Thermistors And Pressure Sensors

- Title: Thermistors And Pressure Sensors
- Source path: `pages\10736.html`
- Chunk ID: `chunk_ae35d012d0e0`
- Images: none
- Duplicate sources: `pages\20392.html`

### Full Text

````text
# Thermistors And Pressure Sensors

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Calibration incorrect | B | Require repair or replacement

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector melted, not affecting performance | 2 | Suggest repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector missing | C | Require replacement

Inoperative | A | Require repair or replacement

NOTE: Includes inoperative, intermittent operation, or failure to perform all functions.

Missing | C | Require replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Wire lead burned | A | Require repair or replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8413: Thermostats And Housings

- Title: Thermostats And Housings
- Source path: `pages\10737.html`
- Chunk ID: `chunk_7adee6149014`
- Images: none
- Duplicate sources: `pages\20393.html`

### Full Text

````text
# Thermostats And Housings

Condition | Code | Procedure

Application incorrect | B | Require replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware corroded | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Cracked | B | Require replacement

Housing corroded | 1 | Suggest replacement of housing

Inoperative | A | Require replacement

NOTE: Inoperative includes intermittent operation.

Installation incorrect | B | Require repair or replacement

Leaking | A | Require repair or replacement

Thermostat missing | C | Require replacement of thermostat

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require repair or replacement
````

## Chunk 8414: Vacuum Reservoirs

- Title: Vacuum Reservoirs
- Source path: `pages\10739.html`
- Chunk ID: `chunk_482cefb91f19`
- Images: none
- Duplicate sources: `pages\20395.html`

### Full Text

````text
# Vacuum Reservoirs

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Check valve leaking internally | A | Require replacement

Leaking | A | Require repair or replacement

Missing | C | Require replacement

Restricted | A | Require repair or replacement
````

## Chunk 8415: Vacuum Tubes

- Title: Vacuum Tubes
- Source path: `pages\10740.html`
- Chunk ID: `chunk_5d324023019c`
- Images: none
- Duplicate sources: `pages\20396.html`

### Full Text

````text
# Vacuum Tubes

Condition | Code | Procedure

Disconnected | A | Require repair

Melted | A | Require repair or replacement

Missing | C | Require replacement

Oil-soaked (spongy) | 1 | Suggest replacement

Restricted | A | Require repair or replacement

Routing incorrect | B | Require repair

Surface cracks (dry-rotted) | 1 | Suggest replacement
````

## Chunk 8416: Valves In Receiver (VIRS)

- Title: Valves In Receiver (VIRS)
- Source path: `pages\10741.html`
- Chunk ID: `chunk_9ae701f05ac7`
- Images: none
- Duplicate sources: `pages\20397.html`

### Full Text

````text
# Valves In Receiver (VIRS)

Condition | Code | Procedure

Application incorrect | B | Require replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Bracket bent, affecting performance | A | Require repair or replacement

Bracket bent, not affecting performance | No service suggested or required

Bracket broken, affecting performance | A | Require replacement

Bracket broken, not affecting performance | No service suggested or required

Bracket corroded, affecting performance | A | Require repair or replacement

Bracket corroded, not affecting performance | 2 | Suggest repair or replacement

Bracket cracked, affecting performance | A | Require repair or replacement

Bracket cracked, not affecting performance | 1 | Suggest repair or replacement

Bracket holes elongated, affecting performance | A | Require repair or replacement

Bracket holes elongated, not affecting performance | No service suggested or required

Bracket loose, affecting performance | A | Require repair or replacement

Bracket loose, not affecting performance | 1 | Suggest repair or replacement

Bracket missing | C | Require replacement

Connection damaged | B | Require repair or replacement

Contaminated, affecting performance | A | Require replacement

Corroded internally | 1 | Suggest replacement

Desiccant at the end of its useful life (saturated with moisture) | 1 | Suggest repair or replacement

Desiccant bag deteriorated | A | Require replacement. Further inspection required

NOTE: Inspect system to determine effects of desiccant bag deterioration.

Filter screen torn | A | Require replacement of screen

Fitting damaged | B | Require repair or replacement

Fusible plug leaking | A | Require replacement of plug

Inoperative | A | Require repair or replacement

NOTE: Inoperative includes intermittent operation.

Leaking | B | Require repair or replacement

Pressure relief device leaking | A | Require replacement of pressure relief device

Restricted | A | Require repair or replacement

Sight glass no longer transparent | 2 | Suggest replacement of drier

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

Tubing connection leaking | A | Require repair or replacement
````

## Chunk 8417: Water Pumps (Electric Auxiliary)

- Title: Water Pumps (Electric Auxiliary)
- Source path: `pages\10742.html`
- Chunk ID: `chunk_e651b504cea4`
- Images: none
- Duplicate sources: `pages\20398.html`

### Full Text

````text
# Water Pumps (Electric Auxiliary)

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector melted, not affecting performance | 2 | Suggest repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector missing | C | Require replacement

Inoperative | A | Require replacement

NOTE: Inoperative includes intermittent operation.

Leaking | B | Require repair or replacement

Missing | C | Require replacement

Noisy | 2 | Suggest replacement

Terminal broken | A | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Vibration | 1 | Suggest replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead corroded | A | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8418: Wiring Harnesses And Connectors

- Title: Wiring Harnesses And Connectors
- Source path: `pages\10743.html`
- Chunk ID: `chunk_d1b7a18cb16d`
- Images: none
- Duplicate sources: `pages\20399.html`

### Full Text

````text
# Wiring Harnesses And Connectors

Condition | Code | Procedure

Application incorrect | B | Require repair or replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Circuit open | A | Require repair or replacement

Circuit resistance (voltage drop) out of specification | A | Require repair or replacement

Circuit shorted | A | Require repair or replacement

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector melted, not affecting performance | 2 | Suggest repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector missing | C | Require replacement

Diode open | A | Require repair or replacement

Diode shorted | A | Require repair or replacement

Insulation damaged, conductors exposed | A | Require repair or replacement

Insulation damaged, conductors not exposed | 1 | Suggest replacement

Protective shield (conduit) melted | 2 | Require replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Protective shield (conduit) missing | C | Require replacement

Routed incorrectly | B | Require repair

Secured incorrectly | B | Require repair

Terminal broken | A | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement
````

## Chunk 8419: Automotive Terminology & Definitions

- Title: Automotive Terminology & Definitions
- Source path: `pages\10746.html`
- Chunk ID: `chunk_a9805ab4a5d2`
- Images: none
- Duplicate sources: `pages\20402.html`

### Full Text

````text
# Automotive Terminology & Definitions

a servo action device in an automatic transmission that cushions the motion of a clutch; in an air conditioning system, a device that combines the suction throttling valve and POA valves as well as the receiver/dryer; a component used to store or hold liquid refrigerant in an air conditioning system that also contains a jesiccant; in a non-integral ABS system, a chamber that temporarily stores fluid during the pressure decrease phase of ABS operation; in an integral ABS system , a sealed vessel containing a thick flexible diaphragm that separates brake fluid from high-pressure nitrogen gas.

a control device that delivers mechanical action in response to a vacuum or electrical signal; anything that the engine control computer uses to do something, such as trigger fuel injection or fire a spark plug. Most actuators on a computercontrolled engine system are activated by grounding their circuits rather than by actively powering them, since that protects the computer from short circuits.

to expose to the air or mix with air, as with a liquid; to charge a liquid with gas.

a system that cools and dehumidifies the air entering the passenger compartment of a vehicle.

a tube, channel or other tubular structure used to carry air to a specific location.

a switch that prevents air conditioner operation below a certain ambient temperature.

the temperature of the air surrounding an object.

the pressure exerted on an object by the weight of the earth's atmosphere. At sea level, 14.7 psi, less at higher altitudes.

the breaking down of a fluid into a fine mist that can be suspended in air.

a climate control system that uses the heating and air conditioning systems to maintain the interior temperature selected by the vehicle's passengers.

specialized add-on heating units, or combination heating/cooling units, that operate with the truck engine turned off. They eliminate the need to leave engines idling solely to heat or cool the cab and sleeper compartment.

two kinds of metal, with different thermal expansion rates, that when attached to one another, the resulting assembly will bend in the direction of the metal that expands the least.

a door in the heating and air conditioning system that controls the temperature of the air going into the passenger compartment.

the electric motor which drives the fan that circulates air inside the vehicle passenger compartment.

the temperature at which a liquid turns to vapor.

a thin, gas-filled tube that senses the temperature of the evaporator and relays this information to the thermostat and/or expansion valve.

a colorless, odorless, noncombustible gas, heavier than air; can be compressed into a super-cold solid known as dry ice; changes from solid to vapor at - 78.5°C.

the basis of the metric system of temperature measurement in which water's boiling point is 100°C and its freezing point is 0 C.

the electrical current that passes through the battery to restore it to full power; to fill, or bring up to the specific level, an A/C system with refrigerant; the required amount of refrigerant for an A/C system.

a gate or valve that allows passage of a gas or liquid in one direction only.

any organic chemical compounds made up of carbon, chlorine and fluorine atoms, usually used in refrigeration. R12 is a CFC.

a device that opens and closes the circuit that engages the air conditioning compressor clutch based on pressure or temperature.

an engine driven device that compresses refrigerant gas and pumps it through the air conditioning system.

the process of a vapor becoming a liquid; the opposite of evaporation.

to cool a vapor to below its boiling point, where it then condenses into a liquid.

a device, similar to a radiator, in which the refrigerant loses heat and changes state from a high-pressure gas to a high pressure liquid as it dissipates heat to the surrounding air.

plugs that fill holes in a block or head left from the casting process. Also called freeze, welsh or expansion plugs.

an A/C system that controls temperature by switching the compressor clutch on and off.

used to designate temperature readings or 1 degree as a 1/360 part of a circle.

to remove moisture (humidity) from the air.

any hygroscopic material that removes and traps moisture, usually found in a bag in the accumulator or receiver/drier in air conditioning systems.
````

## Chunk 8420: Automotive Terminology & Definitions

- Title: Automotive Terminology & Definitions
- Source path: `pages\10746.html`
- Chunk ID: `chunk_e1a60759f480`
- Images: none
- Duplicate sources: `pages\20402.html`

### Full Text

````text
r becoming a liquid; the opposite of evaporation.

to cool a vapor to below its boiling point, where it then condenses into a liquid.

a device, similar to a radiator, in which the refrigerant loses heat and changes state from a high-pressure gas to a high pressure liquid as it dissipates heat to the surrounding air.

plugs that fill holes in a block or head left from the casting process. Also called freeze, welsh or expansion plugs.

an A/C system that controls temperature by switching the compressor clutch on and off.

used to designate temperature readings or 1 degree as a 1/360 part of a circle.

to remove moisture (humidity) from the air.

any hygroscopic material that removes and traps moisture, usually found in a bag in the accumulator or receiver/drier in air conditioning systems.

flexible, impermeable membrane on which pressure acts to produce mechanical movement; in automotive terminology, any disc-shaped device; can be as diverse as thin membranes that separate two chambers in a component, and large metal discs that activate clutch pressure plates.

a radiator in which coolant enters the top of the radiator and is drawn downward by gravity (see crossflow radiator).

allows individualized control of heating and air conditioning. Most systems are adjustable for the driver and front passenger; others feature a third adjustment for rear passengers.

the process of applying vacuum to a closed refrigeration system to remove air and moisture.

the process through which a liquid is turned into vapor.

a heat exchanger, in which low-pressure refrigerant flows and changes state, absorbing heat from the surrounding air.

used in some air conditioning systems, a component with a fixed opening through which refrigerant passes as it is metered into the evaporator core. Also called an orifice tube.

used on some air conditioning systems, a temperature sensitive device that meters the flow of refrigerant into the evaporator core. Also called a thermostatic expansion valve (TXV).

a scale of temperature measurement with the boiling point of water at 212°F. In the metric system, water's boiling point is 100°Celsius.

a fail-safe cooling system allows a vehicle to be driven under limited power in the event that engine coolant is lost. In case of a ruptured hose, the engine operates in an emergency mode with limited power for driving a short distance (10-50 miles depending on the system). This eliminates the cost and inconvenience of having the vehicle towed to a service station and does not leave the customer stranded.

a device attached to a mechanically driven cooling fan that allows the fan to freewheel when the engine is cold or the vehicle is driven at speed.

an enclosure that routes air through the radiator cooling fins.

a mechanically or electrically driven propeller that draws or pushes air through the radiator, condenser, heater core or evaporator core.

a method of controlling refrigerant flow in an air conditioning system whereby the rate of flow is determined by the pressure difference across an orifice.

DuPont registered trade name for R-12 (dichlorodifluoromethane).

gases, such as carbon dioxide, Nox, methane, and water vapor, that help capture heat from the sun in the lower atmosphere of the earth. As the amount of greenhouse gases in the atmosphere increases, more heat is captured, which can lead to global warming (the greenhouse effect).

the pressure of the refrigerant at the compressor outlet.

device (e.g., a radiator) that is designed to transfer heat from the hot coolant that flows through it to the air blown through it by the fan.

a radiator-like device used to heat the inside of a vehicle. Hot coolant is pumped through it by the water pump, and heat from the coolant moves from the heater core to the passenger compartment as the blower fan forces air through it.

the high-pressure half of an A/C system, usually refers to all components between the compressor outlet and the expansion valve or expansion tube. In this part of the A/C system, the refrigerant is in a liquid form.

moisture in air, usually referred to as relative humidity since the amount of moisture air can hold increases as temperature increases.

acronym for Heating, Ventilation and Air Conditioning.

the amount of heat given off as a vapor changes state from a gas to a liquid without the temperature changing.

the amount of heat needed for a liquid to change state to a vapor without the temperature changing.
````

## Chunk 8421: Automotive Terminology & Definitions

- Title: Automotive Terminology & Definitions
- Source path: `pages\10746.html`
- Chunk ID: `chunk_d1d885a60fa1`
- Images: none
- Duplicate sources: `pages\20402.html`

### Full Text

````text
. Hot coolant is pumped through it by the water pump, and heat from the coolant moves from the heater core to the passenger compartment as the blower fan forces air through it.

the high-pressure half of an A/C system, usually refers to all components between the compressor outlet and the expansion valve or expansion tube. In this part of the A/C system, the refrigerant is in a liquid form.

moisture in air, usually referred to as relative humidity since the amount of moisture air can hold increases as temperature increases.

acronym for Heating, Ventilation and Air Conditioning.

the amount of heat given off as a vapor changes state from a gas to a liquid without the temperature changing.

the amount of heat needed for a liquid to change state to a vapor without the temperature changing.

a tool used to locate refrigerant leaks.

the suction side of an A/C system between the evaporator core inlet (after the expansion valve or expansion tube) and the compressor. In this part of the A/C system, the refrigerant is in a gas form.

the set of gauges that attaches to the high and low side of the A/C system and used for diagnosis.

used in some air conditioning systems, a component with a fixed opening through which refrigerant passes as it is metered into the evaporator core. Also called an expansion tube.

a precisely sized hole that controls the flow of fluid.

a sealing ring, usually made of rubber and installed in a groove; a type of valve seal that fits into a valve stem groove under the valve keepers.

polyalkyline glycol oil (lubricant) used with A/C systems containing R- 134a refrigerant.

a poisonous gas produced when R- 12 refrigerant is burned.

the condition of having pores through which fluids, gases or light can pass; tiny holes in casting caused by air bubbles.

a unit of measure for pressure.

the exertion of force upon a body, measured in pounds per square inch on a gauge.

measurement of pressure in pounds per square inch.

the generic term for CFC refrigerant used in older A/C systems. Also called Freon.

generic term for a modern refrigerant that does not contain CFCs and does not harm the ozone layer.

an A/C system component into which high-pressure liquid refrigerant flows and is temporarily stored and dehydrated, usually located between the condenser outlet and expansion valve.

to send refrigerant to an off-site facility where it is restored to its original purity so that it may be reused.

to remove refrigerant from a system and store it temporarily.

to remove contaminants such as moisture, particulates, etc, from refrigerant and re-introduce it into the A/C system.

the complete loop or circuit that refrigerant passes through as it changes state from a vapor, to a liquid, then back to a vapor.

either a mineral or synthetic oil designed specifically for A/C systems.

a chemical compound used in an A/C system to remove heat from the evaporator and transfer it to the condenser.

a spring operated valve used to open and close the service outlets in an A/C system. They are the service valves used to attach manifold gauges and to charge or evacuate the system.

any of the various designs of fittings that allow service tools such as manifold gauges to be attached to an A/C system. See also Schrader valve.

the low side tube and/or hose leading from the evaporator core outlet to the compressor inlet.

exists in a vessel when the pressure is lower than the atmospheric pressure.

a switch, usually mounted on the compressor on certain A/C systems that completes the circuit to the thermal limiter switch.

the addition of more heat to a gas after it has already vaporized; the heat added to vaporized refrigerant after it has changed state from a liquid to a gas controlled by the expansion valve.

a device used with a timing chain or belt to maintain its tension.

a device installed in the cooling system that allows the engine to come to operating temperature quickly and then maintain a minimum operating temperature.

used on some air conditioning systems, a temperature sensitive device that meters the flow of refrigerant into the evaporator core. Also called an expansion valve.

a pressure lower than atmospheric.

a substance in a gaseous state. Liquid becomes vapor when brought above the boiling point.

a device used to circulate coolant through the engine.

a device used to control the flow of hot coolant to the heater core, usually operated by cable or vacuum.
````

## Chunk 8422: Safety Messages

- Title: Safety Messages
- Source path: `pages\10747.html`
- Chunk ID: `chunk_1bddc8690d1a`
- Images: `images\GHH178508.png`, `images\GHH184079.png`, `images\GHH408804.png`, `images\GHH408805.png`, `images\GHH408806.png`
- Duplicate sources: `pages\10849.html`, `pages\10939.html`, `pages\11221.html`, `pages\20251.html`, `pages\20149.html`, `pages\20059.html`, `pages\12841.html`

### Full Text

````text
# Safety Messages

Your safety, and the safety of others, is very important. To help you make informed decisions, we have provided safety messages, and other safety information throughout this service information. Of course, it is not practical or possible to warn you about all the hazards associated with servicing this vehicle. You must use your own good judgment.

You will find important safety information in a variety of forms including:

- Safety Labels - on the vehicle.

- Safety Messages - preceded by a safety alert symbol and one of three signal words, DANGER, WARNING, or CAUTION. These signal words mean:

You WILL be KILLED or SERIOUSLY HURT if you don't follow instructions.

You CAN be KILLED or SERIOUSLY HURT if you don't follow instructions.

You CAN be HURT if you don't follow instructions.

- Instructions - how to service this vehicle correctly and safely.

All information contained in this service information is based on the latest product information available at the time of printing. We reserve the right to make changes at anytime without notice. No part of this publication may be reproduced, or stored in a retrieval system, or transmitted, in any form by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of the publisher. This includes text, images, and tables.

As you read this service information, you will find information that is preceded by a symbol. The purpose of this message is to help prevent damage to your vehicle, other property, or the environment.

Honda Motor Co., Ltd. Service Publication Office

All Rights Reserved Specifications apply to USA, Canada, and Mexico
````

## Chunk 8423: Danger/Warning/Caution Label Locations (USA/Canada models)

- Title: Danger/Warning/Caution Label Locations (USA/Canada models)
- Source path: `pages\10748.html`
- Chunk ID: `chunk_52ee511d506b`
- Images: `images\GHH408807.jpeg`, `images\GHH408808.jpeg`, `images\GHH408809.jpeg`, `images\GHH408810.jpeg`, `images\GHH408811.jpeg`, `images\GHH408812.jpeg`
- Duplicate sources: `pages\10850.html`, `pages\10940.html`, `pages\11222.html`, `pages\20252.html`, `pages\20150.html`, `pages\20060.html`, `pages\12842.html`

### Full Text

````text
# Danger/Warning/Caution Label Locations (USA/Canada models)

NOTE: Unless otherwise indicated, the illustrations show the 4-door models.

Front Passenger's Compartment: Courtesy of HONDA, U.S.A., INC.

Front Passenger's Compartment (4-door): Courtesy of HONDA, U.S.A., INC. | Rear Passenger's Compartment (2-door): Courtesy of HONDA, U.S.A., INC.

Rear Passenger's Compartment (5-door): Courtesy of HONDA, U.S.A., INC.

Engine Compartment: Courtesy of HONDA, U.S.A., INC. | Doorjamb Area: Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8424: Emergency Towing

- Title: Emergency Towing
- Source path: `pages\10749.html`
- Chunk ID: `chunk_30ff1e26f9b4`
- Images: `images\GHH408813.jpeg`, `images\GHH408814.jpeg`, `images\GHH408815.jpeg`, `images\GHH408816.jpeg`, `images\GHH408817.jpeg`, `images\GHH408818.jpeg`, `images\GHH408819.jpeg`
- Duplicate sources: `pages\10851.html`, `pages\10941.html`, `pages\11223.html`, `pages\20253.html`, `pages\20151.html`, `pages\20061.html`, `pages\12843.html`

### Full Text

````text
# Emergency Towing

NOTE: Unless otherwise indicated, the illustrations show the 4-door models.

If the vehicle needs to be towed, call a professional towing service.

NOTICE:

- Improper towing preparation will damage the transmission. Follow the below procedure exactly. If you cannot shift the transmission or start the engine, the vehicle must be transported on a flat-bed tow truck.

- Trying to lift or tow the vehicle by the bumpers will cause serious damage. The bumpers are not designed to support the vehicle's weight.

- It is best to tow the vehicle no farther than 50 miles (80 km), and keep the vehicle speeds below 35 mph (55 km/h) except when loading on a flat-bed tow truck.

For the vehicle equipped with the engine start/stop button

- If the 12 volt battery is discharged, the ACCESSORY mode cannot be selected by pushing the engine start/stop button. Charge or replace the 12 volt battery to unlock the steering wheel before towing.

- If the ACCESSORY mode cannot be selected because of in an electrical problem other than a discharged 12 volt battery, the flat-bed tow truck is the only way to transport the vehicle.

For the vehicle equipped with the electric parking brake

- If the 12 volt battery is discharged, the electric parking brake cannot be canceled by pushing the electric parking brake/automatic brake hold switch. Charge or replace the 12 volt battery to release the parking brake before towing.

- If the electric parking brake is disabled in an electrical problem or severe vehicle damage, the vehicle must be transported on a flat-bed tow truck.

Emergency Towing There are three popular methods of towing a vehicle.

Towing Method | Transmission Type | Shift Position | Notes

M/T | CVT | M/T | CVT

Cable-type Equipment Courtesy of HONDA, U.S.A., INC. | o | o | Neutral | N | Check the transmission fluid amount and for leaks. If transmission fluid leaks are found or fluid amount is low, the vehicle must be transported by a flat-bed tow truck. Turn the vehicle to the ACCESSORY or ON mode, and then release the parking brake.

- Check the transmission fluid amount and for leaks. If transmission fluid leaks are found or fluid amount is low, the vehicle must be transported by a flat-bed tow truck.

- Turn the vehicle to the ACCESSORY or ON mode, and then release the parking brake.

Flat-bed Tow Truck Equipment Courtesy of HONDA, U.S.A., INC. | o | o | Neutral | P | Secure the vehicle securely on a flat-bed truck. Apply the parking brake.

- Secure the vehicle securely on a flat-bed truck.

- Apply the parking brake.

Towing Method | Transmission Type | Shift Position | Notes

M/T | CVT | M/T | CVT

Front Wheel Lift Equipment Courtesy of HONDA, U.S.A., INC. | o | o | Neutral | N | Turn the vehicle to the ACCESSORY or ON mode, and then release the parking brake.

- Turn the vehicle to the ACCESSORY or ON mode, and then release the parking brake.

Towing Hooks/Tie Down Hook Slots Locations

- The front towing hook and detachable rear towing hook (for some models) can be used with a winch to pull the vehicle onto the flat-bed tow truck, and the front/rear tie down hook slots can be used to secure the vehicle to the flat-bed tow truck.

- The tie down hook slots are covered with rubber plugs. Be sure to reinstall them after use.

NOTICE:

- To avoid damage to the vehicle, use the front towing hook and detachable rear towing hook (for some models) for straight flat ground towing only. Do not tow on an angle.

- 2/4-door models (except Japan production models) are not equipped with a rear towing hook. Do not use the rear bumper or the rear tie down slots as a towing hook. It will cause a severe damage to the rear of the vehicle.

Front towing hook:

Courtesy of HONDA, U.S.A., INC. A: Front towing hook

Detachable rear towing hook (for some 4-door models): | Detachable rear towing hook (5-door models):

Courtesy of HONDA, U.S.A., INC. B: Detachable rear towing hook | Courtesy of HONDA, U.S.A., INC. C: Detachable rear towing hook

Tie down hook slots:

Courtesy of HONDA, U.S.A., INC. D: Front tie down hook slots E: Rear tie down hook slots F: Rubber plugs: Be sure to reinstall the plugs after use.
````

## Chunk 8425: Lift and Support Points: Notes

- Title: Lift and Support Points: Notes
- Source path: `pages\10750.html`
- Chunk ID: `chunk_48c24044b4a3`
- Images: none
- Duplicate sources: `pages\10852.html`, `pages\10942.html`, `pages\11224.html`, `pages\20254.html`, `pages\20152.html`, `pages\20062.html`, `pages\12844.html`

### Full Text

````text
# Lift and Support Points: Notes

NOTE:

- If you are going to remove heavy components such as suspension or the fuel tank from the rear of the vehicle, first support the front of the vehicle with tall safety stands. When substantial weight is removed from the rear of the vehicle, the center of gravity can change, causing the vehicle to tip forward on the lift.

- Unless otherwise indicated, the illustrations show the 4-door models.
````

## Chunk 8426: Vehicle Lift

- Title: Vehicle Lift
- Source path: `pages\10751.html`
- Chunk ID: `chunk_47850184d504`
- Images: `images\GHH408820.jpeg`
- Duplicate sources: `pages\10853.html`, `pages\10943.html`, `pages\11225.html`, `pages\20255.html`, `pages\20153.html`, `pages\20063.html`, `pages\12845.html`

### Full Text

````text
# Vehicle Lift

1. Position the lift pads (A) under the vehicle's front support points (B) and rear support points (C).

NOTICE:

Be sure the lift pads are properly placed to avoid damaging the vehicle.

Courtesy of HONDA, U.S.A., INC.

2. Raise the lift a few inches, and rock the vehicle gently to be sure it is firmly supported.

3. Raise the lift to its full height, and inspect the vehicle support points for solid contact with the lift pads.
````

## Chunk 8427: Safety Stands

- Title: Safety Stands
- Source path: `pages\10752.html`
- Chunk ID: `chunk_c976567abec7`
- Images: none
- Duplicate sources: `pages\10854.html`, `pages\10944.html`, `pages\11226.html`, `pages\20256.html`, `pages\20154.html`, `pages\20064.html`, `pages\12846.html`

### Full Text

````text
# Safety Stands

To support the vehicle on safety stands, use the same support points as for a vehicle lift. Always use safety stands when working on or under any vehicle that is supported only by a jack.
````

## Chunk 8428: Floor Jack

- Title: Floor Jack
- Source path: `pages\10753.html`
- Chunk ID: `chunk_6919395753d0`
- Images: `images\GHH408821.jpeg`, `images\GHH408822.jpeg`, `images\GHH408823.jpeg`
- Duplicate sources: `pages\10855.html`, `pages\10945.html`, `pages\11227.html`, `pages\20257.html`, `pages\20155.html`, `pages\20065.html`, `pages\12847.html`

### Full Text

````text
# Floor Jack

1. When lifting the front of the vehicle, set the parking brake. When lifting the rear of the vehicle, put the shift lever in reverse (M/T model) or P (CVT model) position/mode.

2. Block the wheels that are not being lifted.

3. Position the floor jack under the front jacking bracket (A) or the rear jacking bracket (B). Center the jacking bracket on the jack lift platform (C), and jack up the vehicle high enough to fit the safety stands under it.

NOTICE:

- Be sure the floor jack is properly placed to avoid damaging the vehicle.

- This vehicle has low ground clearance. To avoid damaging the vehicle, make sure there is enough clearance around the support points.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC. | Courtesy of HONDA, U.S.A., INC.

4. Position the safety stands under the support points, and adjusts them so the vehicle is level side-to-side.

5. Lower the vehicle onto the stands.
````

## Chunk 8429: Service Precautions: General

- Title: Service Precautions: General
- Source path: `pages\10754.html`
- Chunk ID: `chunk_a70112cb9faa`
- Images: `images\GHH408824.jpeg`, `images\GHH408825.jpeg`, `images\GHH408826.jpeg`, `images\GHH408827.jpeg`, `images\GHH408828.jpeg`, `images\GHH408829.jpeg`, `images\GHH408830.jpeg`, `images\GHH408831.jpeg`, `images\GHH408832.jpeg`, `images\GHH408833.jpeg`
- Duplicate sources: `pages\10856.html`, `pages\10946.html`, `pages\11228.html`, `pages\20258.html`, `pages\20156.html`, `pages\20066.html`, `pages\12848.html`

### Full Text

````text
# Service Precautions: General

WARNING:

Observe all safety precautions and notes while working.

NOTE: The following information are general precautions when servicing the vehicle and some features mentioned may not apply.

- Protect all painted surfaces and seats against dirt and scratches with a clean cloth or vinyl cover.

Courtesy of HONDA, U.S.A., INC.

- Work safely and give your work your undivided attention. When either the front or rear wheels are to be raised, block the remaining wheels. Communicate as frequently as possible when work involves two or more workers. Do not run the engine unless the shop or working area is well ventilated.

- When starting the engine or running the drive system with the vehicle lifted, pay attention to your surroundings and watch out for other worker's safety.

Courtesy of HONDA, U.S.A., INC.

- Before removing or disassembling parts, they must be inspected carefully to isolate the cause for which service is necessary. Observe all safety notes and precautions and follow the proper procedures as described in this service information.

Courtesy of HONDA, U.S.A., INC.

- Mark or place all removed parts in order in a parts rack so they can be reassembled in their original places.

Courtesy of HONDA, U.S.A., INC.

- Use the special tool when use of such a tool is specified.

Courtesy of HONDA, U.S.A., INC.

- Power tools must be used appropriately.

- Follow instructions and precautions carefully per the tool's manufacturer. Do not use power tools for tightening. Only use them during removals of fasteners.

- Follow instructions and precautions carefully per the tool's manufacturer.

- Do not use power tools for tightening. Only use them during removals of fasteners.

- Parts must be assembled with the proper torque according to the established maintenance standards.

- When tightening a series of bolts or nuts, begin with the center or large diameter bolts and tighten them in a crisscross pattern in two or more steps.

Courtesy of HONDA, U.S.A., INC.

- Use new packings, gaskets, O-rings, and cotter pins whenever reassembling.

- Do not reuse parts that require replacement. Always replace them.

Courtesy of HONDA, U.S.A., INC.

- Use genuine parts and lubricants or equivalents. When parts are to be reused, they must be inspected carefully to make sure they are not damaged or deteriorated and are in good usable condition.

Courtesy of HONDA, U.S.A., INC.

- Coat or fill parts with specified grease as indicated. Clean all removed parts with solvent upon disassembly.

Courtesy of HONDA, U.S.A., INC.

- Brake fluid and hydraulic components

- When replenishing the system, use extreme care to prevent dust and dirt from entering the system. Do not mix different brands of fluid as they may not be compatible. Do not reuse drained brake fluid. Because brake fluid can cause damage to painted and resin surfaces, be careful not to spill it on such materials. Quickly wash the brake fluid off the painted or resin surface using water or warm water if spilled. After disconnecting brake hoses or pipes, be sure to plug the openings to prevent loss of brake fluid. Clean all disassembled parts only in clean BRAKE CLEANER. Blow open all holes and passages with compressed air. Keep disassembled parts from air-borne dust and abrasives. Check that parts are clean before assembly.

- When replenishing the system, use extreme care to prevent dust and dirt from entering the system.

- Do not mix different brands of fluid as they may not be compatible.

- Do not reuse drained brake fluid.

- Because brake fluid can cause damage to painted and resin surfaces, be careful not to spill it on such materials. Quickly wash the brake fluid off the painted or resin surface using water or warm water if spilled.

- After disconnecting brake hoses or pipes, be sure to plug the openings to prevent loss of brake fluid.

- Clean all disassembled parts only in clean BRAKE CLEANER. Blow open all holes and passages with compressed air.

- Keep disassembled parts from air-borne dust and abrasives.

- Check that parts are clean before assembly.

Courtesy of HONDA, U.S.A., INC.

- Avoid oil or grease getting on rubber parts and tubes, unless specified.

- Make sure not to get any silicone grease on the terminal part of the connectors and switches, especially if you have silicone grease on your hands or gloves.
````

## Chunk 8430: Service Precautions: General

- Title: Service Precautions: General
- Source path: `pages\10754.html`
- Chunk ID: `chunk_1cfab49bd9fe`
- Images: `images\GHH408824.jpeg`, `images\GHH408825.jpeg`, `images\GHH408826.jpeg`, `images\GHH408827.jpeg`, `images\GHH408828.jpeg`, `images\GHH408829.jpeg`, `images\GHH408830.jpeg`, `images\GHH408831.jpeg`, `images\GHH408832.jpeg`, `images\GHH408833.jpeg`
- Duplicate sources: `pages\10856.html`, `pages\10946.html`, `pages\11228.html`, `pages\20258.html`, `pages\20156.html`, `pages\20066.html`, `pages\12848.html`

### Full Text

````text
fluid can cause damage to painted and resin surfaces, be careful not to spill it on such materials. Quickly wash the brake fluid off the painted or resin surface using water or warm water if spilled.

- After disconnecting brake hoses or pipes, be sure to plug the openings to prevent loss of brake fluid.

- Clean all disassembled parts only in clean BRAKE CLEANER. Blow open all holes and passages with compressed air.

- Keep disassembled parts from air-borne dust and abrasives.

- Check that parts are clean before assembly.

Courtesy of HONDA, U.S.A., INC.

- Avoid oil or grease getting on rubber parts and tubes, unless specified.

- Make sure not to get any silicone grease on the terminal part of the connectors and switches, especially if you have silicone grease on your hands or gloves.

- When spraying any agents that contain silicone, cover all the connectors, terminals, and switches in the area with a protective cloth or plastic sheet.

- Upon assembling, check every part for proper installation and operation.

- When disassembling and/or reassembling parts, do the service below.

- Check the proper parts are installed. Check the installed parts operate properly.

- Check the proper parts are installed.

- Check the installed parts operate properly.

- If harmful materials to human body come in contact with eyes, skins, or the mouth, take appropriate treatments and seek immediate medical attention.
````

## Chunk 8431: Auto Idle Stop System (If Equipped)

- Title: Auto Idle Stop System (If Equipped)
- Source path: `pages\10755.html`
- Chunk ID: `chunk_3d5b43321f51`
- Images: none
- Duplicate sources: `pages\10857.html`, `pages\10947.html`, `pages\11229.html`, `pages\20259.html`, `pages\20157.html`, `pages\20067.html`, `pages\12849.html`

### Full Text

````text
# Auto Idle Stop System (If Equipped)

Some models are equipped with an Auto Idle Stop System. Before servicing the vehicle, especially inside the engine compartment, turn the vehicle to the OFF (LOCK) mode, then keep the key away from the vehicle.

Before doing any service on the powertrain system, read the following precautions. See also "Auto Idle Stop System Description - Operation Conditions" for additional information.

Precaution for Disposal of EDLC Module (If Equipped)

- Vehicles with the Auto Idle Stop System are equipped with the EDLC (Electric Double Layer Capacitor) module.

- Because the EDLC module accumulates high voltage, it must be discharged completely before waste disposal of the vehicle and/or module itself. See "EDLC Module Removal and Installation" for more detail.

- There is electrolyte liquid in the EDLC module, and it is harmful physically and environmentally. If the electrolyte liquid is leaking due to a collision, etc., make sure to wear protective goggles and gloves when handling the EDLC.
````

## Chunk 8432: Real Time 4WD/AWD (Intelligent Control System) (If Equipped)

- Title: Real Time 4WD/AWD (Intelligent Control System) (If Equipped)
- Source path: `pages\10756.html`
- Chunk ID: `chunk_f9ff172600eb`
- Images: none
- Duplicate sources: `pages\10858.html`, `pages\10948.html`, `pages\11230.html`, `pages\20260.html`, `pages\20158.html`, `pages\20068.html`, `pages\12850.html`

### Full Text

````text
# Real Time 4WD/AWD (Intelligent Control System) (If Equipped)

The 4WD/AWD system distributes driving torque between the front and rear wheels when accelerating and when wheel spin occurs.

The 4WD/AWD with Intelligent Control does not have a manual switch to disable the 4WD/AWD system. Whenever service work requires spinning the front or rear wheels with the engine, always lift and support the vehicle so all four wheels are off the ground.
````

## Chunk 8433: Electric Powertrain System (If Equipped)

- Title: Electric Powertrain System (If Equipped)
- Source path: `pages\10757.html`
- Chunk ID: `chunk_8357274e2450`
- Images: none
- Duplicate sources: `pages\10859.html`, `pages\10949.html`, `pages\11231.html`, `pages\20261.html`, `pages\20159.html`, `pages\20069.html`, `pages\12851.html`

### Full Text

````text
# Electric Powertrain System (If Equipped)

The Electric Powertrain System used in hybrid models uses high voltage circuits and a lithium-ion battery module. The high voltage cables are identified by orange cabling. The safety labels are attached to high voltage and other related parts. Touching, disassembling, removing, or replacing high voltage parts or cables can cause severe electric shock that may result in serious injury or death. You must be familiar with Electric Powertrain System before working around it. Make sure you have read the Electric Powertrain Service Precautions in the Electric Powertrain section before doing repairs or service.
````

## Chunk 8434: Electrical Troubleshooting Information

- Title: Electrical Troubleshooting Information
- Source path: `pages\10758.html`
- Chunk ID: `chunk_18fb57c6b808`
- Images: `images\GHH408834.jpeg`, `images\GHH408835.jpeg`, `images\GHH408836.jpeg`, `images\GHH408837.jpeg`, `images\GHH408838.jpeg`, `images\GHH408839.jpeg`, `images\GHH408840.jpeg`, `images\GHH408841.jpeg`, `images\GHH408842.jpeg`, `images\GHH408843.jpeg`, `images\GHH408844.jpeg`, `images\GHH408845.jpeg`, `images\GHH408846.jpeg`
- Duplicate sources: `pages\10860.html`, `pages\10950.html`, `pages\11232.html`, `pages\20262.html`, `pages\20160.html`, `pages\20070.html`, `pages\12852.html`

### Full Text

````text
# Electrical Troubleshooting Information

Before Troubleshooting

1. Check applicable fuses in the appropriate fuse/relay box.

2. Check the 12 volt battery charge and whether the 12 volt battery has been damaged, and clean and tighten the connections.

NOTICE:

- Do not quick-charge a 12 volt battery unless the 12 volt battery ground cable has been disconnected, otherwise you will damage the alternator diodes.

- Do not attempt to crank the engine with the 12 volt battery ground cable loosely connected or you will severely damage the wiring.

3. Check the drive belt tension.

Handling Connectors

- Make sure the connectors are clean and have no loose wire terminals.

- Make sure multiple cavity connectors are packed with dielectric grease (except waterproof connectors).

- Most of the connectors have push-down release type locks (A).

Courtesy of HONDA, U.S.A., INC.

- Some connectors have a clip on their side used to attach them to a mounting bracket on the body or on another component. This clip has a pull type lock.

- Some mounted connectors cannot be disconnected unless you release the lock first and remove the connector from its mount bracket (A).

Courtesy of HONDA, U.S.A., INC.

- Never try to disconnect connectors by pulling on their wires; pull on the connector halves instead.

- Always reinstall plastic covers.

Courtesy of HONDA, U.S.A., INC.

- Before connecting connectors, make sure the terminals (A) are in place and not bent.

Courtesy of HONDA, U.S.A., INC.

- Check for loose retainers (A) and rubber seals (B).

Courtesy of HONDA, U.S.A., INC.

- The backs of some connectors are packed with dielectric grease. Add grease if necessary. If the grease is contaminated, replace the connector (if available) or the wire harness.

Courtesy of HONDA, U.S.A., INC.

- Insert the connector all the way and make sure it is securely locked.

- Position wires so that the open end of the cover faces down.

Courtesy of HONDA, U.S.A., INC.

Handling Wires and Harnesses

- Secure wires and wire harnesses to the frame with their respective wire ties at the designated locations.

- Remove clips carefully; don't damage their locks (A).

Courtesy of HONDA, U.S.A., INC.

- Slip pliers (A) under the clip base and through the hole at an angle, then squeeze the expansion tabs to release the clip.

Courtesy of HONDA, U.S.A., INC.

- After installing the harness clips, make sure the harness doesn't interfere with any moving parts.

- Keep the wire harnesses away from exhaust pipes and other hot parts, from sharp edges of brackets and holes, and from exposed screws and bolts.

- Seat grommets in their grooves properly (A). Do not leave grommets distorted (B).

Courtesy of HONDA, U.S.A., INC.

Testing and Repairs

- Do not use wires or harnesses with broken insulation. Replace them or repair them by wrapping the break with electrical tape.

- Never attempt to modify, splice, or repair SRS wiring. If there is an open or damage on SRS wiring or terminals, replace the harness.

- After installing parts, make sure that no wires are pinched under them.

- When using electrical test equipment, follow the manufacturer's instructions and those described in this service information.

- If possible, insert the probe of the tester from the wire side (except for waterproof connectors).

Courtesy of HONDA, U.S.A., INC.

- Use a probe with a tapered tip.

Courtesy of HONDA, U.S.A., INC.

WARNING:

- Puncturing the insulation on a wire can cause poor or intermittent electrical connections.

- For testing at connectors, bring the tester probe into contact with the terminal from the connector side of wire harness connectors in the engine compartment. For female connectors, just touch lightly with the tester probe and do not insert the probe.

For female connectors, just touch lightly with the tester probe and do not insert the probe.

When checking any control module(s) or unit(s) connector terminals, gently slide the sharp tester probe from the wire side into the connector until it comes in contact with the terminal end of the wire.

Courtesy of HONDA, U.S.A., INC.

- Some vehicles may use an aluminum wire harness. Special attention is needed to protect the harness from corrosion and damage during disconnecting of connectors.

- Do not break up the connectors of the aluminum wire harnesses. Never attempt to modify and repair the aluminum wire harnesses. Replace the wire harnesses if they are damaged.
````

## Chunk 8435: Electrical Troubleshooting Information

- Title: Electrical Troubleshooting Information
- Source path: `pages\10758.html`
- Chunk ID: `chunk_e6e9089412b9`
- Images: `images\GHH408834.jpeg`, `images\GHH408835.jpeg`, `images\GHH408836.jpeg`, `images\GHH408837.jpeg`, `images\GHH408838.jpeg`, `images\GHH408839.jpeg`, `images\GHH408840.jpeg`, `images\GHH408841.jpeg`, `images\GHH408842.jpeg`, `images\GHH408843.jpeg`, `images\GHH408844.jpeg`, `images\GHH408845.jpeg`, `images\GHH408846.jpeg`
- Duplicate sources: `pages\10860.html`, `pages\10950.html`, `pages\11232.html`, `pages\20262.html`, `pages\20160.html`, `pages\20070.html`, `pages\12852.html`

### Full Text

````text
ectors in the engine compartment. For female connectors, just touch lightly with the tester probe and do not insert the probe.

For female connectors, just touch lightly with the tester probe and do not insert the probe.

When checking any control module(s) or unit(s) connector terminals, gently slide the sharp tester probe from the wire side into the connector until it comes in contact with the terminal end of the wire.

Courtesy of HONDA, U.S.A., INC.

- Some vehicles may use an aluminum wire harness. Special attention is needed to protect the harness from corrosion and damage during disconnecting of connectors.

- Do not break up the connectors of the aluminum wire harnesses. Never attempt to modify and repair the aluminum wire harnesses. Replace the wire harnesses if they are damaged.

- Do not break up the connectors of the aluminum wire harnesses.

- Never attempt to modify and repair the aluminum wire harnesses. Replace the wire harnesses if they are damaged.
````

## Chunk 8436: Five-step Troubleshooting

- Title: Five-step Troubleshooting
- Source path: `pages\10759.html`
- Chunk ID: `chunk_b03a2110d23c`
- Images: none
- Duplicate sources: `pages\10861.html`, `pages\10951.html`, `pages\11233.html`, `pages\20263.html`, `pages\20161.html`, `pages\20071.html`, `pages\12853.html`

### Full Text

````text
# Five-step Troubleshooting

1. Verify the Complaint

Turn on all the components in the problem circuit to verify the customer's complaint. Note the symptoms. Do not begin disassembly or testing until you have narrowed down the problem area.

2. Analyze the Schematic

Look up the schematic for the problem circuit. Determine how the circuit is supposed to work by tracing the current paths from the power feed through the circuit components to ground. If several circuits fail at the same time, the fuse or ground is a likely cause.

Based on the symptoms and your understanding of the circuit operation, identify one or more possible causes of the problem.

3. Isolate the Problem by Testing the Circuit

Make circuit tests to check the diagnosis you made in step 2. Keep in mind that a logical, simple procedure is the key to efficient troubleshooting. Test for the most likely cause of the failure first. Try to make tests at points that are easily accessible.

4. Fix the Problem

Once the specific problem is identified, make the repair. Be sure to use proper tools and safe procedures.

5. Make Sure the Circuit Works

Turn on all components in the repaired circuit in all modes to make sure you've fixed the entire problem. If the problem was a blown fuse, be sure to test all of the circuits on the fuse. Make sure no new problems turn up and the original problem does not reoccur.
````

## Chunk 8437: Precaution for Handling Sodium-Filled Exhaust Valves (If Equipped)

- Title: Precaution for Handling Sodium-Filled Exhaust Valves (If Equipped)
- Source path: `pages\10761.html`
- Chunk ID: `chunk_839009fc92db`
- Images: `images\GHH408848.jpeg`, `images\GHH408849.jpeg`
- Duplicate sources: `pages\10863.html`, `pages\10953.html`, `pages\11235.html`, `pages\20265.html`, `pages\20163.html`, `pages\20073.html`, `pages\12855.html`

### Full Text

````text
# Precaution for Handling Sodium-Filled Exhaust Valves (If Equipped)

Read all of the instructions before disposing of sodium-filled exhaust valves.

WARNING:

- Sodium requires extreme caution in handling and disposal. Sodium is highly flammable and it reacts with water and oxygen in the air. Sodium reacts with water vigorously and may cause an explosion.

- Make sure to wear protective tools (such as goggles and gloves) when handling sodium. Keep sodium away from eyes and skin as it may cause caustic skin burns, and contact with eyes may cause blindness.

- When handling sodium, be sure to do so in a well-ventilated area as it reacts with water to form hydrogen gas.

- If you come in contact with sodium, flush thoroughly with a large amount of water and seek immediate medical attention.

Determination method of Sodium-Filled Exhaust Valves

Identification marks (A) for sodium-filled exhaust valves are located on the valve head and/or valve stem.

NOTE: The illustration is a typical sample of the sodium-filled valve.

Courtesy of HONDA, U.S.A., INC.

Waste Disposal of Sodium-Filled Valves

1. When the sodium-filled exhaust valves are NOT damaged

NOTE: You can dispose sodium-filled exhaust valves as you would with normal valves unless the sodium in the valve stem is exposed. If they are exposed, the valve stem must be neutralized using the Neutralization Procedure.

WARNING:

Do not destroy the valves intentionally to expose sodium.

2. When the sodium-filled exhaust valves are damaged

NOTE: Do the neutralization procedure before disposal.

WARNING:

- Make sure to wear protective goggles and gloves, and do this procedure in a well-ventilated area.

- When you do this procedure, make sure to have a fire extinguisher (dry powder type) on hand.

- Handle the damaged valves with tweezers or tongs, not with bare hands.

Neutralization Procedure

- Prepare a large container filled with 10 L (2.64 US gal) of water.

- Soak the damaged valves into the water. Soak the damaged valves completely. Keep all cigarettes, sparks, and flames away from the container. Chemical reaction of sodium and water generates hydrogen gas. Stay a few meters away from the container as this procedure may cause severe reaction of chemicals. This procedure can neutralize a maximum of six damaged valves at the same time.

- Soak the damaged valves completely.

- Keep all cigarettes, sparks, and flames away from the container. Chemical reaction of sodium and water generates hydrogen gas.

- Stay a few meters away from the container as this procedure may cause severe reaction of chemicals.

- This procedure can neutralize a maximum of six damaged valves at the same time.

- When the procedure is finished after 4-5 hours, pick up the damaged valves with tweezers or tongs, and dispose of them as normal valves.

WARNING:

The waste liquid after neutralization procedure contains highly-concentrated sodium hydroxide. It is very harmful physically and environmentally. Dispose the waste liquid according to your local regulations.

Courtesy of HONDA, U.S.A., INC.

Damaged valves Water solution of sodium hydroxide (waste liquid)

- Damaged valves

- Water solution of sodium hydroxide (waste liquid)
````

## Chunk 8438: Emission Group Identification

- Title: Emission Group Identification
- Source path: `pages\10762.html`
- Chunk ID: `chunk_22e80414d1db`
- Images: `images\GHH408850.jpeg`, `images\GHH408851.jpeg`, `images\GHH408852.jpeg`
- Duplicate sources: `pages\10864.html`, `pages\10954.html`, `pages\11236.html`, `pages\20266.html`, `pages\20164.html`, `pages\20074.html`, `pages\12856.html`

### Full Text

````text
# Emission Group Identification

Example:

Courtesy of HONDA, U.S.A., INC.

'17 Model CONFORMS TO REGULATIONS: 2017 MY

Test Group and Evaporative Family

Test Group: | Evaporative Family:

Courtesy of HONDA, U.S.A., INC. | Courtesy of HONDA, U.S.A., INC.

a. | Model Year | a. | Model Year

H: '17 | H: '17

b. | Manufacturer Subcode | b. | Manufacturer Subcode

HNX: Honda | HNX: Honda

c. | Family Type | c. | Family Type

V: Passenger Car | R: Refueling

d. | Displacement Group | d. | Canister Working Capacity Group

01.5: L15B7 | 0113: Civic Type-R, Civic Sedan/Coupe Si

02.0: K20C1

e. | Sequence Characters | e. | Sequence Characters

7H3: Civic Type-R | VSB: Civic Type-R, Civic Sedan/Coupe Si

6H3: Civic Sedan/Coupe Si
````

## Chunk 8439: Emission Group Identification

- Title: Emission Group Identification
- Source path: `pages\10763.html`
- Chunk ID: `chunk_56fa7e899e2f`
- Images: `images\GHH408853.jpeg`, `images\GHH408854.jpeg`, `images\GHH408855.jpeg`
- Duplicate sources: `pages\10865.html`, `pages\10955.html`, `pages\11237.html`, `pages\20267.html`, `pages\20165.html`, `pages\20075.html`, `pages\12857.html`

### Full Text

````text
# Emission Group Identification

Example:

Courtesy of HONDA, U.S.A., INC.

'17 Model CONFORMS TO REGULATIONS: 2017 MY

Test Group and Evaporative Family

Test Group: | Evaporative Family:

Courtesy of HONDA, U.S.A., INC. | Courtesy of HONDA, U.S.A., INC.

a. | Model Year | a. | Model Year

H: '17 | H: '17

b. | Manufacturer Subcode | b. | Manufacturer Subcode

HNX: Honda | HNX: Honda

c. | Family Type | c. | Family Type

V: Passenger Car | R: Refueling

d. | Displacement Group | d. | Canister Working Capacity Group

01.5: L15B7, L15BA | 0113: Civic ULEV 125

02.0: K20C2 | 0113: Civic SULEV30/PZEV

e. | Sequence Characters | e. | Sequence Characters

XH2: Civic 1.5 L ULEV 125 | VSB: Civic 1.5 L ULEV 125

CH3: Civic 2.0 L ULEV 125 | VSA: Civic 2.0 L ULEV 125

562: Civic 1.5 L SULEV30/PZEV | VSB: Civic 1.5 L SULEV30/PZEV

B63: Civic 2.0 L SULEV30/PZEV | VSA: Civic 2.0 L SULEV30/PZEV
````

## Chunk 8440: Emission Group Identification

- Title: Emission Group Identification
- Source path: `pages\10764.html`
- Chunk ID: `chunk_75a22a4cf284`
- Images: `images\GHH408856.jpeg`, `images\GHH408857.jpeg`, `images\GHH408858.jpeg`
- Duplicate sources: `pages\10866.html`, `pages\10956.html`, `pages\11238.html`, `pages\20268.html`, `pages\20166.html`, `pages\20076.html`, `pages\12858.html`

### Full Text

````text
# Emission Group Identification

Example:

Courtesy of HONDA, U.S.A., INC.

'16 Model CONFORMS TO REGULATIONS: 2016 MY

Test Group and Evaporative Family

Test Group: | Evaporative Family:

Courtesy of HONDA, U.S.A., INC. | Courtesy of HONDA, U.S.A., INC.

a. | Model Year | a. | Model Year

G: '16 | G: '16

b. | Manufacturer Subcode | b. | Manufacturer Subcode

HNX: Honda | HNX: Honda

c. | Family Type | c. | Family Type

V: Passenger Car | R: Refueling

d. | Displacement Group | d. | Canister Working Capacity Group

01.5: L15B7 | 0106: Civic ULEV 125

02.0: K20C2 | 0113: Civic SULEV30/PZEV

e. | Sequence Characters | e. | Sequence Characters

3H2: Civic 1.5 L ULEV 125 | VFD: Civic 1.5 L ULEV 125

CH3: Civic 2.0 L ULEV 125 | VFC: Civic 2.0 L ULEV 125

6K2: Civic 1.5 L SULEV30/PZEV | VSB: Civic 1.5 L SULEV30/PZEV

BK3: Civic 2.0 L SULEV30/PZEV | VSA: Civic 2.0 L SULEV30/PZEV
````

## Chunk 8441: Emission Group Identification

- Title: Emission Group Identification
- Source path: `pages\10765.html`
- Chunk ID: `chunk_ee4b98eead50`
- Images: `images\GHH408859.jpeg`, `images\GHH408860.jpeg`, `images\GHH408861.jpeg`
- Duplicate sources: `pages\10867.html`, `pages\10957.html`, `pages\11239.html`, `pages\20269.html`, `pages\20167.html`, `pages\20077.html`, `pages\12859.html`

### Full Text

````text
# Emission Group Identification

Example:

Courtesy of HONDA, U.S.A., INC.

'18 Model CONFORMS TO REGULATIONS: 2018 MY

Test Group and Evaporative Family

Test Group: | Evaporative Family:

Courtesy of HONDA, U.S.A., INC. | Courtesy of HONDA, U.S.A., INC.

a. | Model Year | a. | Model Year

J: '18 | J: '18

b. | Manufacturer Subcode | b. | Manufacturer Subcode

HNX: Honda | HNX: Honda

c. | Family Type | c. | Family Type

V: Passenger Car | R: Refueling

d. | Displacement Group | d. | Canister Working Capacity Group

01.5: L15BA, L15B7, L15BY | 0113: Civic Type-R, Civic ULEV 125,

02.0: K20C1, K20C2 | Civic SULEV 30, Civic Sedan Si/Coupe Si

e. | Sequence Characters | e. | Sequence Characters

2H3: Civic Type-R | VSB: Civic Type-R

TH2: Civic 1.5 L ULEV 125 | VSB: Civic 1.5 L ULEV 125

362: Civic 1.5 L SULEV 30 | VSB: Civic 1.5 L SULEV 30

VH3: Civic Sedan Si/Coupe Si | VSB: Civic Sedan Si/Coupe Si

C63: Civic 2.0 L SULEV 30 | VSA: Civic 2.0 L SULEV 30

DH3: Civic 2.0 L ULEV 125 | VSA: Civic 2.0 L ULEV 125
````

## Chunk 8442: Emission Group Identification

- Title: Emission Group Identification
- Source path: `pages\10766.html`
- Chunk ID: `chunk_6e2222378cb5`
- Images: `images\GHH408862.jpeg`, `images\GHH408863.jpeg`, `images\GHH408864.jpeg`
- Duplicate sources: `pages\10868.html`, `pages\10958.html`, `pages\11240.html`, `pages\20270.html`, `pages\20168.html`, `pages\20078.html`, `pages\12860.html`

### Full Text

````text
# Emission Group Identification

Example:

Courtesy of HONDA, U.S.A., INC.

'19 Model CONFORMS TO REGULATIONS: 2019 MY

Test Group and Evaporative Family

Test Group: | Evaporative Family:

Courtesy of HONDA, U.S.A., INC. | Courtesy of HONDA, U.S.A., INC.

a. | Model Year | a. | Model Year

K: '19 | J: '19

b. | Manufacturer Subcode | b. | Manufacturer Subcode

HNX: Honda | HNX: Honda

c. | Family Type | c. | Family Type

V: Passenger Car | R: Refueling

d. | Displacement Group | d. | Canister Working Capacity Group

01.5: L15BA, L15B7, L15BY | 0113: Civic Type-R, Civic ULEV 125,

02.0: K20C1, K20C2 | Civic SULEV 30, Civic Sedan Si/Coupe Si

e. | Sequence Characters | e. | Sequence Characters

1H3: Civic Type-R | VSB: Civic Type-R

GH2: Civic 1.5 L ULEV 125 Sedan/Coupe | VSB: Civic 1.5 L ULEV 125

SH2: Civic 1.5 L ULEV 125 Hatchback | VSB: Civic 1.5 L SULEV 30

2L2: Civic 1.5 L SULEV 30 Sedan/Coupe | VSB: Civic Sedan Si/Coupe Si

5L2: Civic 1.5 L SULEV 30 Hatchback | VSA: Civic 2.0 L SULEV 30

TH3: Civic Sedan Si/Coupe Si | VSA: Civic 2.0 L ULEV 125

CL3: Civic 2.0 L SULEV 30

DH3: Civic 2.0 L ULEV 125
````

## Chunk 8443: Emission Group Identification

- Title: Emission Group Identification
- Source path: `pages\10767.html`
- Chunk ID: `chunk_9709c582e3bd`
- Images: `images\GHH408865.jpeg`, `images\GHH408866.jpeg`, `images\GHH408867.jpeg`
- Duplicate sources: `pages\10869.html`, `pages\10959.html`, `pages\11241.html`, `pages\20271.html`, `pages\20169.html`, `pages\20079.html`, `pages\12861.html`

### Full Text

````text
# Emission Group Identification

Example:

Courtesy of HONDA, U.S.A., INC.

'20 Model CONFORMS TO REGULATIONS: 2020 MY

Test Group and Evaporative Family

Test Group: | Evaporative Family:

Courtesy of HONDA, U.S.A., INC. | Courtesy of HONDA, U.S.A., INC.

a. | Model Year | a. | Model Year

L: '20 | L: '20

b. | Manufacturer Subcode | b. | Manufacturer Subcode

HNX: Honda | HNX: Honda

c. | Family Type | c. | Family Type

V: Passenger Car | R: Refueling

d. | Displacement Group | d. | Canister Working Capacity Group

01.5: L15BA, L15B7 | 0113: Civic ULEV 125, Civic SULEV 30,

02.0: K20C1, K20C2 | Civic Sedan Si/Coupe Si, Civic Type-R

e. | Sequence Characters | e. | Sequence Characters

1BM: Civic Type-R | VSB: Civic Type-R

GH2: Civic 1.5 L ULEV 125 Sedan/Coupe/Hatchback | VSB: Civic 1.5 L ULEV 125

2L2: Civic 1.5 L SULEV 30 Sedan/Coupe/Hatchback | VSB: Civic 1.5 L SULEV 30

TBC: Civic Sedan Si/Coupe Si | VSB: Civic Sedan Si/Coupe Si

CL3: Civic 2.0 L SULEV 30 | VSA: Civic 2.0 L SULEV 30

DH3: Civic 2.0 L ULEV 125 | VSA: Civic 2.0 L ULEV 125
````

## Chunk 8444: Emission Group Identification

- Title: Emission Group Identification
- Source path: `pages\10768.html`
- Chunk ID: `chunk_d6eed8b51b2f`
- Images: `images\GHH408868.jpeg`, `images\GHH408869.jpeg`, `images\GHH408870.jpeg`
- Duplicate sources: `pages\10870.html`, `pages\10960.html`, `pages\11242.html`, `pages\20272.html`, `pages\20170.html`, `pages\20080.html`, `pages\12862.html`

### Full Text

````text
# Emission Group Identification

Example:

Courtesy of HONDA, U.S.A., INC.

'21 Model CONFORMS TO REGULATIONS: 2021 MY

Test Group and Evaporative Family

Test Group: | Evaporative Family:

Courtesy of HONDA, U.S.A., INC. | Courtesy of HONDA, U.S.A., INC.

a. | Model Year | a. | Model Year

M: '21 | M: '21

b. | Manufacturer Subcode | b. | Manufacturer Subcode

HNX: Honda | HNX: Honda

c. | Family Type | c. | Family Type

V: Passenger Car | R: Refueling

d. | Displacement Group | d. | Canister Working Capacity Group

01.5: L15BA, L15B7 | 0113: Civic ULEV 125, Civic SULEV 30,

02.0: K20C1, K20C2 | Civic Type-R

e. | Sequence Characters | e. | Sequence Characters

1BM: Civic Type-R | VSB: Civic Type-R

GH2: Civic 1.5 L ULEV 125 Sedan/Hatchback | VSB: Civic 1.5 L ULEV 125

2L2: Civic 1.5 L SULEV 30 Sedan/Hatchback | VSB: Civic 1.5 L SULEV 30

CL3: Civic 2.0 L SULEV 30 | VSA: Civic 2.0 L SULEV 30

DH3: Civic 2.0 L ULEV 125 | VSA: Civic 2.0 L ULEV 125
````

## Chunk 8445: VIN, Engine, (Motor), Transmission Numbers, and Paint Codes (USA/Canada) (2016): Notes

- Title: VIN, Engine, (Motor), Transmission Numbers, and Paint Codes (USA/Canada) (2016): Notes
- Source path: `pages\10769.html`
- Chunk ID: `chunk_3e4dbcd8a9b3`
- Images: none
- Duplicate sources: `pages\10871.html`, `pages\10961.html`, `pages\11243.html`, `pages\20273.html`, `pages\20171.html`, `pages\20081.html`, `pages\12863.html`

### Full Text

````text
# VIN, Engine, (Motor), Transmission Numbers, and Paint Codes (USA/Canada) (2016): Notes

NOTE: Unless otherwise indicated, the illustrations show the 4-door models.
````

## Chunk 8446: Vehicle Identification Number

- Title: Vehicle Identification Number
- Source path: `pages\10770.html`
- Chunk ID: `chunk_b81157ce04c8`
- Images: `images\GHH408871.jpeg`, `images\GHH408872.png`, `images\GHH408873.png`, `images\GHH408874.png`, `images\GHH408875.png`, `images\GHH408876.png`, `images\GHH408877.png`, `images\GHH408878.png`, `images\GHH408879.png`, `images\GHH408880.png`, `images\GHH408881.png`, `images\GHH408882.png`, `images\GHH408883.jpeg`
- Duplicate sources: `pages\10872.html`, `pages\10962.html`, `pages\11244.html`, `pages\20274.html`, `pages\20172.html`, `pages\20082.html`, `pages\12864.html`

### Full Text

````text
# Vehicle Identification Number

Courtesy of HONDA, U.S.A., INC.

a. | Manufacturer, Make, and Type of Vehicle

2HG: | Honda of Canada Mfg., Honda Canada Inc. Honda passenger vehicle

19X: | Honda Manufacturing of Indiana, LLC Honda passenger vehicle

b. | Line, Body, and Engine Type

FC1: Civic Sedan/L15B7

FC2: Civic Sedan/K20C2

FC3: Civic Coupe/L15B7

FC4: Civic Coupe/K20C2

c. | Body Type and Transmission Type

A: 2-door Coupe/6-speed Manual

B: 2-door Coupe/CVT

E: 4-door Sedan/6-speed Manual

F: 4-door Sedan/CVT

d. | Vehicle Grade (Series)

USA models | Canada models

3: EX-T | 2: DX

4: EX-T Honda Sensing | 3: EX-T

5: LX | 4: EX-T Honda Sensing

6: LX Honda Sensing | 5: LX

7: EX, EX-TL | 6: LX Honda Sensing

8: EX Honda Sensing, EX-TL Honda Sensing | 7: EX

9: Touring | 8: EX Honda Sensing

0: LX-P | 9: Touring

e. | Check Digit

f. | Model Year

G: '16

g. | Factory Code

H: Alliston, Ontario Plant, Canada

E: Greensburg, Indiana Plant, USA

h. | Serial Number

4-door (USA plant models) | 4-door (Canada plant models)

000001 : USA models | 000001 : Canada models (K20C2)

200001 : California models | 100001 : Canada models (L15B7)

400001 : Canada models | 500001 : USA/California models (K20C2)

630001 : USA/California models (L15B7)

2-door (USA/California models) | 2-door (Canada model)

300001 : K20C2 engine models | 400001 : K20C2 engine models

350001 : L15B7 engine models | 425001 : L15B7 engine models

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8447: Engine Number

- Title: Engine Number
- Source path: `pages\10771.html`
- Chunk ID: `chunk_792490aecab0`
- Images: `images\GHH408884.jpeg`, `images\GHH408885.png`, `images\GHH408886.png`
- Duplicate sources: `pages\10873.html`, `pages\10963.html`, `pages\11245.html`, `pages\20275.html`, `pages\20173.html`, `pages\20083.html`, `pages\12865.html`

### Full Text

````text
# Engine Number

Courtesy of HONDA, U.S.A., INC.

a. | Engine Type

L15B7: 1.5 L DOHC VTEC Direct Fuel-injected engine with charge air cooler and turbocharger

K20C2: 2.0 L DOHC i-VTEC Sequential Multiport Fuel-injected engine

b. | Serial Number

1000001 : L15B7, K20C2 (USA engine plant)

1200001 : K20C2 (Canada engine plant)
````

## Chunk 8448: Transmission Number

- Title: Transmission Number
- Source path: `pages\10772.html`
- Chunk ID: `chunk_e9f938748aef`
- Images: `images\GHH408887.jpeg`, `images\GHH408888.png`, `images\GHH408889.png`, `images\GHH408890.png`
- Duplicate sources: `pages\10874.html`, `pages\10964.html`, `pages\11246.html`, `pages\20276.html`, `pages\20174.html`, `pages\20084.html`, `pages\12866.html`

### Full Text

````text
# Transmission Number

Courtesy of HONDA, U.S.A., INC.

a. | Transmission Type

E5GT: 6-speed Manual (K20C2)

MDMA: CVT (K20C2)

JDJC: CVT (K20C2)

BCGA: CVT (L15B7)

b. | Serial Number

1000001 : JDJC, BCGA

1200001 : E5GT

4000001 : MDMA
````

## Chunk 8449: Paint Code

- Title: Paint Code
- Source path: `pages\10773.html`
- Chunk ID: `chunk_929fbf22b120`
- Images: `images\GHH408891.jpeg`
- Duplicate sources: `pages\10875.html`, `pages\10965.html`, `pages\11247.html`, `pages\20277.html`, `pages\20175.html`, `pages\20085.html`, `pages\12867.html`

### Full Text

````text
# Paint Code

Code | Color | 4-door | 2-door

USA models | Canada models | USA models | Canada models

models

models

models

models

NH-578 | Taffeta White | o | o | o | o

NH-731P | Crystal Black Pearl | o | o | o | o

NH-788P | White Orchid Pearl | o | o | o | o

NH-797M | Modern Steel Metallic | o | o | o | o

R-513 | Rallye Red | o | o | o | o

NH-830M | Lunar Silver Metallic | o | o | o | o

B-593M | Aegean Blue Metallic | o | o | o | o

B-607M | Cosmic Blue Metallic | o | o

GY-30P | Energy Green Pearl | o | o

R-560P | Burgundy Night Pearl | o | o

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8450: VIN, Engine, (Motor), Transmission Numbers, and Paint Codes (USA/Canada models Type-R/Si) (2017): Notes

- Title: VIN, Engine, (Motor), Transmission Numbers, and Paint Codes (USA/Canada models Type-R/Si) (2017): Notes
- Source path: `pages\10774.html`
- Chunk ID: `chunk_f48438593eb9`
- Images: none
- Duplicate sources: `pages\10876.html`, `pages\10966.html`, `pages\11248.html`, `pages\20278.html`, `pages\20176.html`, `pages\20086.html`, `pages\12868.html`

### Full Text

````text
# VIN, Engine, (Motor), Transmission Numbers, and Paint Codes (USA/Canada models Type-R/Si) (2017): Notes

NOTE: Unless otherwise indicated, the illustrations show Type-R.
````

## Chunk 8451: Vehicle Identification Number

- Title: Vehicle Identification Number
- Source path: `pages\10775.html`
- Chunk ID: `chunk_d46dedc6bdf3`
- Images: `images\GHH408892.jpeg`, `images\GHH408893.png`, `images\GHH408894.png`, `images\GHH408895.png`, `images\GHH408896.png`, `images\GHH408897.png`, `images\GHH408898.png`, `images\GHH408899.jpeg`
- Duplicate sources: `pages\10877.html`, `pages\10967.html`, `pages\11249.html`, `pages\20279.html`, `pages\20177.html`, `pages\20087.html`, `pages\12869.html`

### Full Text

````text
# Vehicle Identification Number

Courtesy of HONDA, U.S.A., INC.

a. | Manufacturer, Make, and Type of Vehicle

2HG: | Honda of Canada Mfg., Honda Canada Inc. Honda passenger vehicle

SHH: | Honda of the U.K. Manufacturing Ltd. Honda passenger vehicle

b. | Line, Body, and Engine Type

FC1: Civic Sedan Si/L15B7

FC3: Civic Coupe Si/L15B7

FK8: Civic Type-R/K20C1

c. | Body Type and Transmission Type

A: 2-door Coupe/6-speed Manual

E: 4-door Sedan/6-speed Manual

G: 5-door Hatchback/6-speed Manual

d. | Vehicle Grade (Series)

USA models | Canada models

3: TYPE-R | 3: TYPE-R

5: SI | 5: SI

7: TYPERT

e. | Check Digit

f. | Model Year

H: '17

g. | Factory Code

H: Alliston, Ontario Plant, Canada

U: SWINDON Factory, Honda of the U.K. MFG., England

h. | Serial Number

Type-R

200001 : USA model

300001 : Canada model

Si (4-door) | Si (2-door)

700001 : USA model | 750001 : USA model

200001 : Canada model | 220001 : Canada model

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8452: Engine Number

- Title: Engine Number
- Source path: `pages\10776.html`
- Chunk ID: `chunk_c289140d384f`
- Images: `images\GHH408900.jpeg`, `images\GHH408901.png`, `images\GHH408902.png`
- Duplicate sources: `pages\10878.html`, `pages\10968.html`, `pages\11250.html`, `pages\20280.html`, `pages\20178.html`, `pages\20088.html`, `pages\12870.html`

### Full Text

````text
# Engine Number

Courtesy of HONDA, U.S.A., INC.

a. | Engine Type

L15B7: 1.5 L DOHC VTEC Direct Fuel-injected engine with charge air cooler and turbocharger

K20C1: 2.0 L DOHC VTEC Direct Fuel-injected engine with charge air cooler and turbocharger

b. | Serial Number

2000001 : L15B7

3000001 : K20C1
````

## Chunk 8453: Transmission Number

- Title: Transmission Number
- Source path: `pages\10777.html`
- Chunk ID: `chunk_b121fd797661`
- Images: `images\GHH408903.jpeg`, `images\GHH408904.png`, `images\GHH408905.png`
- Duplicate sources: `pages\10879.html`, `pages\10969.html`, `pages\11251.html`, `pages\20281.html`, `pages\20179.html`, `pages\20089.html`, `pages\12871.html`

### Full Text

````text
# Transmission Number

Courtesy of HONDA, U.S.A., INC.

a. | Transmission Type

E5CJ: 6-speed Manual (L15B7)

SDEM: 6-speed Manual (K20C1)

b. | Serial Number

1000001 : SDEM

1200001 : E5CJ
````

## Chunk 8454: Paint Code

- Title: Paint Code
- Source path: `pages\10778.html`
- Chunk ID: `chunk_523a1eac27f4`
- Images: `images\GHH408906.jpeg`
- Duplicate sources: `pages\10880.html`, `pages\10970.html`, `pages\11252.html`, `pages\20282.html`, `pages\20180.html`, `pages\20090.html`, `pages\12872.html`

### Full Text

````text
# Paint Code

Code | Color | Type-R | Si (4-door) | Si (2-door)

USA models | Canada models | USA models | Canada models | USA models | Canada models

models

models

models

models

models

models

NH-0 | Championship White | o | o

NH-731P | Crystal Black Pearl | o | o | o | o | o | o

NH-788P | White Orchid Pearl | o | o | o | o

NH-797M | Modern Steel Metallic | o | o | o | o

NH-737M | Polished Metal Metallic | o | o

R-513 | Rallye Red | o | o | o | o | o | o

NH-830M | Lunar Silver Metallic | o | o | o | o

B-593M | Aegean Blue Metallic | o | o | o | o | o | o

GY-30P | Energy Green Pearl | o | o

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8455: VIN, Engine, (Motor), Transmission Numbers, and Paint Codes (USA/Canada models except Type-R/Si) (2017): Notes

- Title: VIN, Engine, (Motor), Transmission Numbers, and Paint Codes (USA/Canada models except Type-R/Si) (2017): Notes
- Source path: `pages\10779.html`
- Chunk ID: `chunk_121cfb222bfb`
- Images: none
- Duplicate sources: `pages\10881.html`, `pages\10971.html`, `pages\11253.html`, `pages\20283.html`, `pages\20181.html`, `pages\20091.html`, `pages\12873.html`

### Full Text

````text
# VIN, Engine, (Motor), Transmission Numbers, and Paint Codes (USA/Canada models except Type-R/Si) (2017): Notes

NOTE: Unless otherwise indicated, the illustrations show the 4-door models.
````

## Chunk 8456: Vehicle Identification Number

- Title: Vehicle Identification Number
- Source path: `pages\10780.html`
- Chunk ID: `chunk_74afc4ba900d`
- Images: `images\GHH408907.jpeg`, `images\GHH408908.png`, `images\GHH408909.png`, `images\GHH408910.png`, `images\GHH408911.png`, `images\GHH408912.png`, `images\GHH408913.png`, `images\GHH408914.png`, `images\GHH408915.png`, `images\GHH408916.png`, `images\GHH408917.png`, `images\GHH408918.png`, `images\GHH408919.png`, `images\GHH408920.png`, `images\GHH408921.png`, `images\GHH408922.jpeg`
- Duplicate sources: `pages\10882.html`, `pages\10972.html`, `pages\11254.html`, `pages\20284.html`, `pages\20182.html`, `pages\20092.html`, `pages\12874.html`

### Full Text

````text
# Vehicle Identification Number

Courtesy of HONDA, U.S.A., INC.

a. | Manufacturer, Make, and Type of Vehicle

2HG: | Honda of Canada Mfg., Honda Canada Inc. Honda passenger vehicle

19X: | Honda Manufacturing of Indiana, LLC Honda passenger vehicle

SHH: | Honda of the U.K. Manufacturing Ltd. Honda passenger vehicle

b. | Line, Body, and Engine Type

FC1: Civic Sedan/L15B7

FC2: Civic Sedan/K20C2

FC3: Civic Coupe/L15B7

FC4: Civic Coupe/K20C2

FK7: Civic Hatchback/L15BA

c. | Body Type and Transmission Type

A: 2-door Coupe/6-speed Manual

B: 2-door Coupe/CVT

E: 4-door Sedan/6-speed Manual

F: 4-door Sedan/CVT

G: 5-door Hatchback/6-speed Manual

H: 5-door Hatchback/CVT

d. | Vehicle Grade (Series)

USA models | Canada models

2: LX | 2: DX, LX

3: EX-T, LX Honda Sensing | 3: EX-T, LX Honda Sensing

4: EX-T Honda Sensing, SPORT | 4: EX-T Honda Sensing, SPORT, SPORT Honda Sensing

5: LX, EX | 5: LX, EX

6: LX Honda Sensing, EX Honda Sensing | 6: LX Honda Sensing, EX Honda Sensing

7: EX, EX-L, EXLN | 7: EX

8: EX Honda Sensing, EX-L Honda Sensing, EXLN Honda Sensing | 8: EX Honda Sensing

9: Touring, SPORT Touring | 9: Touring, SPORT Touring

0: LX-P

e. | Check Digit

f. | Model Year

H: '17

g. | Factory Code

H: Alliston, Ontario Plant, Canada

E: Greensburg, Indiana Plant, USA

U: SWINDON Factory, Honda of the U.K. MFG., England

h. | Serial Number

5-door

200001 : USA models

400001 : California models

300001 : Canada models

4-door (USA plant models) | 4-door (Canada plant models)

000001 : USA models | 000001 : Canada models (K20C2)

200001 : California models | 100001 : Canada models (L15B7)

400001 : Canada models | 500001 : USA/California models (K20C2)

630001 : USA/California models (L15B7)

2-door (USA/California models) | 2-door (Canada model)

300001 : K20C2 engine models | 400001 : K20C2 engine models

350001 : L15B7 engine models | 450001 : L15B7 engine models

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8457: Engine Number

- Title: Engine Number
- Source path: `pages\10781.html`
- Chunk ID: `chunk_e8c341988b09`
- Images: `images\GHH408923.jpeg`, `images\GHH408924.png`, `images\GHH408925.png`, `images\GHH408926.png`
- Duplicate sources: `pages\10883.html`, `pages\10973.html`, `pages\11255.html`, `pages\20285.html`, `pages\20183.html`, `pages\20093.html`, `pages\12875.html`

### Full Text

````text
# Engine Number

Courtesy of HONDA, U.S.A., INC.

a. | Engine Type

L15B7: 1.5 L DOHC VTEC Direct Fuel-injected engine with charge air cooler and turbocharger

L15BA: 1.5 L DOHC VTEC Direct Fuel-injected engine with charge air cooler and turbocharger

K20C2: 2.0 L DOHC i-VTEC Sequential Multiport Fuel-injected engine

b. | Serial Number

1000001 : L15BA

2000001 : L15B7, K20C2 (USA engine plant)

2200001 : K20C2 (Canada engine plant)
````

## Chunk 8458: Transmission Number

- Title: Transmission Number
- Source path: `pages\10782.html`
- Chunk ID: `chunk_e0015378ab09`
- Images: `images\GHH408927.jpeg`, `images\GHH408928.png`, `images\GHH408929.png`, `images\GHH408930.png`, `images\GHH408931.png`
- Duplicate sources: `pages\10884.html`, `pages\10974.html`, `pages\11256.html`, `pages\20286.html`, `pages\20184.html`, `pages\20094.html`, `pages\12876.html`

### Full Text

````text
# Transmission Number

Courtesy of HONDA, U.S.A., INC.

a. | Transmission Type

E5GT: 6-speed Manual (K20C2)

E5CD: 6-speed Manual (L15BA)

E5CC: 6-speed Manual (L15B7)

JDJC: CVT (K20C2)

BCGA: CVT (L15B7)

MCKA: CVT (L15BA)

b. | Serial Number

2000001 : JDJC, BCGA

1200001 : E5CD

2200001 : E5GT, E5CC

5000001 : MCKA
````

## Chunk 8459: Paint Code

- Title: Paint Code
- Source path: `pages\10783.html`
- Chunk ID: `chunk_7eaa9884e1b0`
- Images: `images\GHH408932.jpeg`
- Duplicate sources: `pages\10885.html`, `pages\10975.html`, `pages\11257.html`, `pages\20287.html`, `pages\20185.html`, `pages\20095.html`, `pages\12877.html`

### Full Text

````text
# Paint Code

Code | Color | 5-door | 4-door | 2-door

USA models | Canada models | USA models | Canada models | USA models | Canada models

models

models

models

models

models

models

NH-578 | Taffeta White | o | o | o | o

NH-731P | Crystal Black Pearl | o | o | o | o | o | o

NH-788P | White Orchid Pearl | o | o | o | o | o | o

NH-797M | Modern Steel Metallic | o | o | o | o

NH-737M | Polished Metal Metallic | o | o

R-513 | Rallye Red | o | o | o | o | o | o

R-539P | Passion Red Pearl | o | o

YR-604M | Golden Brown Pearl | o | o

NH-830M | Lunar Silver Metallic | o | o | o | o | o | o

B-593M | Aegean Blue Metallic | o | o | o | o | o | o

B-607M | Cosmic Blue Metallic | o | o

GY-30P | Energy Green Pearl | o | o

NH-877P | Sonic Gray Pearl | o | o

R-560P | Burgundy Night Pearl | o | o

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8460: VIN, Engine, (Motor), Transmission Numbers, and Paint Codes (USA/Canada models) (2018): Notes

- Title: VIN, Engine, (Motor), Transmission Numbers, and Paint Codes (USA/Canada models) (2018): Notes
- Source path: `pages\10784.html`
- Chunk ID: `chunk_b7a0f884cd60`
- Images: none
- Duplicate sources: `pages\10886.html`, `pages\10976.html`, `pages\11258.html`, `pages\20288.html`, `pages\20186.html`, `pages\20096.html`, `pages\12878.html`

### Full Text

````text
# VIN, Engine, (Motor), Transmission Numbers, and Paint Codes (USA/Canada models) (2018): Notes

NOTE: Unless otherwise indicated, the illustrations show Type-R.
````

## Chunk 8461: Vehicle Identification Number

- Title: Vehicle Identification Number
- Source path: `pages\10785.html`
- Chunk ID: `chunk_b49dc1278fc1`
- Images: `images\G00602702.png`, `images\GHH408934.png`, `images\GHH408935.png`, `images\GHH408936.png`, `images\GHH408937.png`, `images\GHH408938.png`, `images\GHH408939.png`, `images\GHH408940.png`, `images\GHH408941.png`, `images\GHH408942.png`, `images\GHH408943.png`, `images\GHH408944.png`, `images\GHH408945.png`, `images\GHH408946.png`, `images\GHH408947.png`, `images\GHH408948.png`, `images\GHH408949.png`, `images\GHH408950.png`, `images\GHH408951.png`, `images\GHH408952.png`, `images\GHH408953.png`, `images\GHH408954.png`, `images\GHH408955.jpeg`
- Duplicate sources: `pages\10887.html`, `pages\10977.html`, `pages\11259.html`, `pages\20289.html`, `pages\20187.html`, `pages\20097.html`, `pages\12879.html`

### Full Text

````text
# Vehicle Identification Number

Courtesy of HONDA, U.S.A., INC.

a. | Manufacturer, Make, and Type of Vehicle

SHH: | Honda of the U.K. Manufacturing Ltd. Honda passenger vehicle

2HG: | Honda Canada Inc. Honda passenger vehicle

19X: | Honda Manufacturing of Indiana, LLC Honda passenger vehicle

JHM: | Honda Motor Co., Ltd. Honda passenger vehicle

b. | Line, Body, and Engine Type

FC1: Civic Sedan, Civic Sedan Si/L15B7, L15BY

FC2: Civic Sedan/K20C2

FC3: Civic Coupe, Civic Coupe Si/L15B7

FC4: Civic Coupe/K20C2

FK7: Civic Hatchback/L15BA

FK8: Civic Type-R/K20C1

c. | Body Type and Transmission Type

A: 2-door Coupe/6-speed Manual

B: 2-door Coupe/CVT

E: 4-door Sedan/6-speed Manual

F: 4-door Sedan/CVT

G: 5-door Hatchback/6-speed Manual

H: 5-door Hatchback/CVT

d. | Vehicle Grade (Series)

USA models | Canada models

1: SE | 2: LX, DX

2: LX | 3: LX with Honda Sensing

3: LX with Honda Sensing, TYPE-R, EX-T | 4: Sport, Sport with Honda Sensing, EX-T with Honda Sensing

4: Sport, EX-T with Honda Sensing | 5: EX, LX, SI

5: EX, LX, SI | 6: EX with Honda Sensing, LX with Honda Sensing

6: EX with Honda Sensing, LX with Honda Sensing | 7: EX

7: TYPE-R Touring, EX-L | 8: SPORT

8: EX-L NAVI with Honda Sensing, EX-L, SPORT | 9: Sport Touring, Touring

9: Sport Touring, Touring

e. | Check Digit

f. | Model Year

J: '18

g. | Factory Code

U: Swindon, England Plant, U.K.

H: Honda of Canada Mfg in Canada

E: Greensburg, Indiana Plant, U.S.A.

X: Yorii, Saitama Automobile Plant in Japan

h. | Serial Number

Type-R | 5-door

200001 : USA model | 200001 : USA model

300001 : Canada model | 300001 : Canada model

400001 : USA (California) model

4-door (USA plant model) | 4-door (Canada plant model)

000001 : USA model | 000001 : Canada model (K20C2)

200001 : USA (California) model | 100001 : Canada model (L15B7)

400001 : Canada model | 500001 : USA model (K20C2)

650001 : USA model (L15B7)

4-door (Yorii factory model)

000001 : USA model

2-door (USA model) | 2-door (Canada model)

300001 : K20C2 engine model | 400001 : K20C2 engine model

350001 : L15B7 engine model | 450001 : L15B7 engine model

Si (4-door) | Si (2-door)

700001 : USA model | 750001 : USA model

200001 : Canada model | 220001 : Canada model

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8462: Engine Number

- Title: Engine Number
- Source path: `pages\10786.html`
- Chunk ID: `chunk_25d02e9b451c`
- Images: `images\GHH408956.jpeg`, `images\GHH408957.png`, `images\GHH408958.png`, `images\GHH408959.png`, `images\GHH408960.png`, `images\GHH408961.png`
- Duplicate sources: `pages\10791.html`, `pages\10888.html`, `pages\10893.html`, `pages\10978.html`, `pages\10983.html`, `pages\11260.html`, `pages\11265.html`, `pages\20290.html`, `pages\20295.html`, `pages\20188.html`, `pages\20193.html`, `pages\20098.html`, `pages\20103.html`, `pages\12880.html`, `pages\12885.html`

### Full Text

````text
# Engine Number

Courtesy of HONDA, U.S.A., INC.

a. | Engine Type

L15BA: 1.5 L DOHC VTEC Direct Fuel-injected engine with charge air cooler and turbocharger

L15BY: 1.5 L DOHC VTEC Direct Fuel-injected engine with charge air cooler and turbocharger

L15B7: 1.5 L DOHC VTEC Direct Fuel-injected engine with charge air cooler and turbocharger

K20C1: 2.0 L DOHC VTEC Direct Fuel-injected engine with charge air cooler and turbocharger

K20C2: 2.0 L DOHC i-VTEC Sequential Multiport Fuel-injected engine

b. | Serial Number

1730001 : L15BY

1300001 : L15BA

4000001 : L15B7, K20C2 (USA engine plant)

4200001 : K20C2 (Canada engine plant)

5000001 : K20C1
````

## Chunk 8463: Transmission Number

- Title: Transmission Number
- Source path: `pages\10787.html`
- Chunk ID: `chunk_88d898cb8d64`
- Images: `images\GHH408962.jpeg`, `images\GHH408963.png`, `images\GHH408964.png`, `images\GHH408965.png`, `images\GHH408966.png`
- Duplicate sources: `pages\10889.html`, `pages\10979.html`, `pages\11261.html`, `pages\20291.html`, `pages\20189.html`, `pages\20099.html`, `pages\12881.html`

### Full Text

````text
# Transmission Number

Courtesy of HONDA, U.S.A., INC.

a. | Transmission Type

ECDM: 6-speed Manual (L15BA)

ECCM: 6-speed Manual (L15B7 except Si)

E5CJ: 6-speed Manual (L15B7 Si)

E5GT: 6-speed Manual (K20C2)

SDEM: 6-speed Manual (K20C1)

JDJC: CVT (K20C2)

BCGA: CVT (L15BA, L15B7)

MCKA: CVT (L15BY)

b. | Serial Number

1000001 : ECCM

2000001 : SDEM, E5CD

3000001 : JDJC, E5GT, BCGA, E5CA

5200001 : MCKA
````

## Chunk 8464: Paint Code

- Title: Paint Code
- Source path: `pages\10788.html`
- Chunk ID: `chunk_45e454bf6a23`
- Images: `images\GHH408967.jpeg`
- Duplicate sources: `pages\10793.html`, `pages\10890.html`, `pages\10895.html`, `pages\10980.html`, `pages\10985.html`, `pages\11262.html`, `pages\11267.html`, `pages\20292.html`, `pages\20297.html`, `pages\20190.html`, `pages\20195.html`, `pages\20100.html`, `pages\20105.html`, `pages\12882.html`, `pages\12887.html`

### Full Text

````text
# Paint Code

Code | Color | Type-R | 5-door

USA models | Canada models | USA models | Canada models

models

models

models

models

NH-0 | Championship White | o | o

NH-731P | Crystal Black Pearl | o | o | o | o

NH-788P | White Orchid Pearl | o | o

NH-737M | Polished Metal Metallic | o | o | o | o

NH-877P | Sonic Gray Pearl | o | o | o | o

R-513 | Rallye Red | o | o | o | o

NH-830M | Lunar Silver Metallic | o | o

B-593M | Aegean Blue Metallic | o | o | o | o

Code | Color | 2-door | 4-door

USA models | Canada models | USA models | Canada models

models

models

models

models

NH-731P | Crystal Black Pearl | o | o | o | o

NH-797M | Modern Steel Metallic | o | o | o | o

NH-830M | Lunar Silver Metallic | o | o | o | o

NH-883P | Platinum White Pearl | o | o | o | o

R-513 | Rallye Red | o | o | o | o

R-539P | Molten Lava Pearl | o | o

Y-78P | Tonic Yellow Pearl | o | o

B-607M | Cosmic Blue Metallic | o | o

B-593M | Aegean Blue Metallic | o | o | o | o

Code | Color | Si (2-door) | Si (4-door)

USA models | Canada models | USA models | Canada models

models

models

models

models

NH-731P | Crystal Black Pearl | o | o | o | o

NH-797M | Modern Steel Metallic | o | o | o | o

NH-830M | Lunar Silver Metallic | o | o | o | o

Code | Color | Si (2-door) | Si (4-door)

USA models | Canada models | USA models | Canada models

models

models

models

models

NH-883P | Platinum White Pearl | o | o | o | o

R-513 | Rallye Red | o | o | o | o

Y-78P | Tonic Yellow Pearl | o | o

B-593M | Aegean Blue Metallic | o | o | o | o

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8465: VIN, Engine, (Motor), Transmission Numbers, and Paint Codes (USA/Canada models) (2019): Notes

- Title: VIN, Engine, (Motor), Transmission Numbers, and Paint Codes (USA/Canada models) (2019): Notes
- Source path: `pages\10789.html`
- Chunk ID: `chunk_e56e963bd98c`
- Images: none
- Duplicate sources: `pages\10891.html`, `pages\10981.html`, `pages\11263.html`, `pages\20293.html`, `pages\20191.html`, `pages\20101.html`, `pages\12883.html`

### Full Text

````text
# VIN, Engine, (Motor), Transmission Numbers, and Paint Codes (USA/Canada models) (2019): Notes

NOTE: Unless otherwise indicated, the illustrations show Type-R.
````

## Chunk 8466: Vehicle Identification Number

- Title: Vehicle Identification Number
- Source path: `pages\10790.html`
- Chunk ID: `chunk_ba74b1bd6c1e`
- Images: `images\GHH408933.jpeg`, `images\GHH408934.png`, `images\GHH408935.png`, `images\GHH408936.png`, `images\GHH408937.png`, `images\GHH408938.png`, `images\GHH408939.png`, `images\GHH408940.png`, `images\GHH408941.png`, `images\GHH408942.png`, `images\GHH408943.png`, `images\GHH408944.png`, `images\GHH408945.png`, `images\GHH408946.png`, `images\GHH408947.png`, `images\GHH408948.png`, `images\GHH408949.png`, `images\GHH408950.png`, `images\GHH408951.png`, `images\GHH408952.png`, `images\GHH408953.png`, `images\GHH408954.png`, `images\GHH408955.jpeg`
- Duplicate sources: `pages\10892.html`, `pages\10982.html`, `pages\11264.html`, `pages\20294.html`, `pages\20192.html`, `pages\20102.html`, `pages\12884.html`

### Full Text

````text
# Vehicle Identification Number

Courtesy of HONDA, U.S.A., INC.

a. | Manufacturer, Make, and Type of Vehicle

SHH: | Honda of the U.K. Manufacturing Ltd. Honda passenger vehicle

2HG: | Honda Canada Inc. Honda passenger vehicle

19X: | Honda Manufacturing of Indiana, LLC Honda passenger vehicle

JHM: | Honda Motor Co., Ltd. Honda passenger vehicle

b. | Line, Body, and Engine Type

FC1: Civic Sedan, Civic Sedan Si/L15B7, L15BY

FC2: Civic Sedan/K20C2

FC3: Civic Coupe, Civic Coupe Si/L15B7

FC4: Civic Coupe/K20C2

FK7: Civic Hatchback/L15BA

FK8: Civic Type-R/K20C1

c. | Body Type and Transmission Type

A: 2-door Coupe/6-speed Manual

B: 2-door Coupe/CVT

E: 4-door Sedan/6-speed Manual

F: 4-door Sedan/CVT

G: 5-door Hatchback/6-speed Manual

H: 5-door Hatchback/CVT

d. | Vehicle Grade (Series)

USA models | Canada models

1: SE | 2: LX, DX

2: LX | 3: LX with Honda Sensing

3: LX with Honda Sensing, TYPE-R, EXT | 4: Sport, Sport with Honda Sensing, EX-T with Honda Sensing

4: Sport | 5: LX, SI

5: SI | 6: EX with Honda Sensing, LX with Honda Sensing

6: EX with Honda Sensing, LX with Honda Sensing | 7: EX

7: TYPE-R Touring, EX-L | 8: SPORT

8: EX-L NAVI with Honda Sensing, EX-L, SPORT | 9: Sport Touring, Touring

9: Sport Touring, Touring

e. | Check Digit

f. | Model Year

K: '19

g. | Factory Code

U: Swindon, England Plant, U.K.

H: Honda of Canada Mfg in Canada

E: Greensburg, Indiana Plant, U.S.A.

X: Yorii, Saitama Automobile Plant in Japan

h. | Serial Number

Type-R | 5-door

200001 : USA model | 200001 : USA model

300001 : Canada model | 300001 : Canada model

400001 : USA (California) model

4-door (USA plant model) | 4-door (Canada plant model)

000001 : USA model | 000001 : Canada model (K20C2)

200001 : USA (California) model | 100001 : Canada model (L15B7)

400001 : Canada model | 500001 : USA model (K20C2)

650001 : USA model (L15B7)

4-door (Yorii factory model)

000001 : USA model

2-door (USA model) | 2-door (Canada model)

300001 : K20C2 engine model | 400001 : K20C2 engine model

350001 : L15B7 engine model | 450001 : L15B7 engine model

Si (4-door) | Si (2-door)

700001 : USA model | 750001 : USA model

200001 : Canada model | 220001 : Canada model

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8467: Transmission Number

- Title: Transmission Number
- Source path: `pages\10792.html`
- Chunk ID: `chunk_75385ecbe3c4`
- Images: `images\GHH408962.jpeg`, `images\GHH408963.png`, `images\GHH408964.png`, `images\GHH408965.png`, `images\GHH408966.png`
- Duplicate sources: `pages\10894.html`, `pages\10984.html`, `pages\11266.html`, `pages\20296.html`, `pages\20194.html`, `pages\20104.html`, `pages\12886.html`

### Full Text

````text
# Transmission Number

Courtesy of HONDA, U.S.A., INC.

a. | Transmission Type

ECDM: 6-speed Manual (L15BA)

ECCM: 6-speed Manual (L15B7 except Si)

E5CJ: 6-speed Manual (L15B7 Si)

E5GT: 6-speed Manual (K20C2)

SDEM: 6-speed Manual (K20C1)

JDJC: CVT (K20C2)

BCGA: CVT (L15BA, L15B7)

MCKA: CVT (L15BY)

b. | Serial Number

2000001 : ECCM, ECDM

3000001 : SDEM, E5CJ

4000001 : JDJC, E5GT, BCGA

5500001 : MCKA
````

## Chunk 8468: Vehicle Identification Number

- Title: Vehicle Identification Number
- Source path: `pages\10794.html`
- Chunk ID: `chunk_c87d07f07938`
- Images: `images\GHH408968.jpeg`, `images\GHH408969.png`, `images\GHH408970.png`, `images\GHH408971.png`, `images\GHH408972.png`, `images\GHH408973.png`, `images\GHH408974.png`, `images\GHH408975.png`, `images\GHH408976.png`, `images\GHH408977.png`, `images\GHH408978.png`, `images\GHH408979.png`, `images\GHH408980.png`, `images\GHH408981.png`, `images\GHH408982.png`, `images\GHH408983.png`, `images\GHH408984.png`, `images\GHH408985.png`, `images\GHH408986.png`, `images\GHH408987.png`, `images\GHH408988.png`, `images\GHH408989.jpeg`
- Duplicate sources: `pages\10896.html`, `pages\10986.html`, `pages\11268.html`, `pages\20298.html`, `pages\20196.html`, `pages\20106.html`, `pages\12888.html`

### Full Text

````text
# Vehicle Identification Number

Courtesy of HONDA, U.S.A., INC.

a. | Manufacturer, Make, and Type of Vehicle

SHH: | Honda of the U.K. Manufacturing Ltd. Honda passenger vehicle

2HG: | Honda Canada Inc. Honda passenger vehicle

19X: | Honda Manufacturing of Indiana, LLC Honda passenger vehicle

b. | Line, Body, and Engine Type

FC1: Civic Sedan, Civic Sedan Si/L15B7

FC2: Civic Sedan/K20C2

FC3: Civic Coupe, Civic Coupe Si/L15B7

FC4: Civic Coupe/K20C2

FK7: Civic Hatchback/L15BA

FK8: Civic Type-R/K20C1

c. | Body Type and Transmission Type

A: 2-door Coupe/6-speed Manual

B: 2-door Coupe/CVT

E: 4-door Sedan/6-speed Manual

F: 4-door Sedan/CVT

G: 5-door Hatchback/6-speed Manual

H: 5-door Hatchback/CVT

d. | Vehicle Grade (Series)

USA models | Canada models

1: SE | 2: DX

2: SE | 3: LX with Honda Sensing, TYPE-R

3: LX with Honda Sensing, EX-T, TYPE-R | 4: Sport, Sport with Honda Sensing, EX-T with Honda Sensing

4: Sport | 5: LX, SI

5: SI | 6: EX with Honda Sensing, LX with Honda Sensing

6: EX with Honda Sensing, LX with Honda Sensing | 7: EX

7: EX-TL, TYPE-R Touring | 8: SPORT

8: EX-L with Honda Sensing, SPORT | 9: Sport Touring, Touring

9: Sport Touring, Touring

e. | Check Digit

f. | Model Year

L: '20

g. | Factory Code

U: Swindon, Wiltshire, United Kingdom

H: Alliston, Ontario, Canada

E: Greensburg, Indiana, U.S.A.

h. | Serial Number

5-door | Type-R

200001 : USA model | 200001 : USA model

300001 : Canada model | 300001 : Canada model

400001 : USA (California) model

4-door (USA plant model) | 4-door (Canada plant model)

000001 : USA model | 000001 : Canada model (K20C2)

200001 : USA (California) model | 100001 : Canada model (L15B7)

400001 : Canada model | 500001 : USA model (K20C2)

650001 : USA model (L15B7)

2-door (USA model) | 2-door (Canada model)

300001 : K20C2 engine model | 400001 : K20C2 engine model

350001 : L15B7 engine model | 450001 : L15B7 engine model

Si (4-door) | Si (2-door)

700001 : USA model | 750001 : USA model

200001 : Canada model | 220001 : Canada model

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8469: Engine Number

- Title: Engine Number
- Source path: `pages\10795.html`
- Chunk ID: `chunk_705e372f3962`
- Images: `images\GHH408990.jpeg`, `images\GHH408991.png`, `images\GHH408992.png`, `images\GHH408993.png`, `images\GHH408994.png`
- Duplicate sources: `pages\10897.html`, `pages\10987.html`, `pages\11269.html`, `pages\20299.html`, `pages\20197.html`, `pages\20107.html`, `pages\12889.html`

### Full Text

````text
# Engine Number

Courtesy of HONDA, U.S.A., INC.

a. | Engine Type

L15BA: 1.5 L DOHC VTEC Direct Fuel-injected engine with charge air cooler and turbocharger

L15B7: 1.5 L DOHC VTEC Direct Fuel-injected engine with charge air cooler and turbocharger

K20C1: 2.0 L DOHC VTEC Direct Fuel-injected engine with charge air cooler and turbocharger

K20C2: 2.0 L DOHC i-VTEC Sequential Multiport Fuel-injected engine

b. | Serial Number

1550001 : L15BA

5000001 : L15B7, K20C2 (USA engine plant)

5200001 : K20C2 (Canada engine plant)

6000001 : K20C1
````

## Chunk 8470: Transmission Number

- Title: Transmission Number
- Source path: `pages\10796.html`
- Chunk ID: `chunk_69a086a30252`
- Images: `images\GHH408995.jpeg`, `images\GHH408996.png`, `images\GHH408997.png`, `images\GHH408998.png`, `images\GHH408999.png`, `images\GHH409000.png`
- Duplicate sources: `pages\10898.html`, `pages\10988.html`, `pages\11270.html`, `pages\20300.html`, `pages\20198.html`, `pages\20108.html`, `pages\12890.html`

### Full Text

````text
# Transmission Number

Courtesy of HONDA, U.S.A., INC.

a. | Transmission Type

ECDB: 6-speed Manual (L15BA)

ECCM: 6-speed Manual (L15B7 except Si)

ECDA: 6-speed Manual (L15B7 Si)

E5GT: 6-speed Manual (K20C2)

SDEM: 6-speed Manual (K20C1)

JDJC: CVT (K20C2)

BCGA: CVT (L15BA, L15B7)

b. | Serial Number

1000001 : ECDA, ECDB

3000001 : ECCM

4000001 : SDEM

5000001 : JDJC

5000001 : BCGA, E5GT
````

## Chunk 8471: Paint Code

- Title: Paint Code
- Source path: `pages\10797.html`
- Chunk ID: `chunk_c50b58083d72`
- Images: `images\GHH409001.jpeg`
- Duplicate sources: `pages\10899.html`, `pages\10989.html`, `pages\11271.html`, `pages\20301.html`, `pages\20199.html`, `pages\20109.html`, `pages\12891.html`

### Full Text

````text
# Paint Code

Code | Color | 5-door | Type-R

USA models | Canada models | USA models | Canada models

models

models

models

models

NH-0 | Championship White | o | o

NH-731P | Crystal Black Pearl | o | o | o | o

NH-883P | Platinum White Pearl | o | o

NH-737M | Polished Metal Metallic | o | o | o | o

NH-877P | Sonic Gray Pearl | o | o | o

R-513 | Rallye Red | o | o | o | o

NH-830M | Lunar Silver Metallic | o | o

B-593M | Aegean Blue Metallic | o | o | o | o

B-637P | Boost Blue Pearl | o | o

Code | Color | 2-door | 4-door

USA models | Canada models | USA models | Canada models

models

models

models

models

NH-731P | Crystal Black Pearl | o | o | o | o

NH-797M | Modern Steel Metallic | o | o | o | o

NH-830M | Lunar Silver Metallic | o | o | o | o

NH-883P | Platinum White Pearl | o | o | o | o

R-513 | Rallye Red | o | o | o | o

R-539P | Molten Lava Pearl | o

B-607M | Cosmic Blue Metallic | o | o

B-593M | Aegean Blue Metallic | o | o | o | o

Code | Color | Si (2-door) | Si (4-door)

USA models | Canada models | USA models | Canada models

models

models

models

models

NH-731P | Crystal Black Pearl | o | o | o | o

NH-797M | Modern Steel Metallic | o | o | o | o

NH-830M | Lunar Silver Metallic | o | o | o | o

Code | Color | Si (2-door) | Si (4-door)

USA models | Canada models | USA models | Canada models

models

models

models

models

NH-883P | Platinum White Pearl | o | o | o | o

R-513 | Rallye Red | o | o | o | o

B-593M | Aegean Blue Metallic | o | o | o | o

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8472: Vehicle Identification Number

- Title: Vehicle Identification Number
- Source path: `pages\10798.html`
- Chunk ID: `chunk_5bf999810f0e`
- Images: `images\GHH409002.jpeg`, `images\GHH409003.png`, `images\GHH409004.png`, `images\GHH409005.png`, `images\GHH409006.png`, `images\GHH409007.png`, `images\GHH409008.png`, `images\GHH409009.png`, `images\GHH409010.png`, `images\GHH409011.png`, `images\GHH409012.png`, `images\GHH409013.png`, `images\GHH409014.jpeg`
- Duplicate sources: `pages\10900.html`, `pages\10990.html`, `pages\11272.html`, `pages\20302.html`, `pages\20200.html`, `pages\20110.html`, `pages\12892.html`

### Full Text

````text
# Vehicle Identification Number

Courtesy of HONDA, U.S.A., INC.

a. | Manufacturer, Make, and Type of Vehicle

SHH: | Honda of the U.K. Manufacturing Ltd. Honda passenger vehicle

2HG: | Honda Canada Inc. Honda passenger vehicle

19X: | Honda Manufacturing of Indiana, LLC Honda passenger vehicle

b. | Line, Body, and Engine Type

FC1: Civic Sedan/L15B7

FC2: Civic Sedan/K20C2

FK7: Civic Hatchback/L15BA

FK8: Civic Type-R/K20C1

c. | Body Type and Transmission Type

F: 4-door Sedan/CVT

G: 5-door Hatchback/6-speed Manual

H: 5-door Hatchback/CVT

d. | Vehicle Grade (Series)

USA models | Canada models

0: Type-R Limited Edition | 0: Type-R Limited Edition

1: SE | 3: LX with Honda Sensing, Type-R

2: SE | 4: Sport, Sport with Honda Sensing

3: LX with Honda Sensing, EX-T | 5: LX

4: Sport | 6: EX with Honda Sensing

6: EX with Honda Sensing, LX | 7: EX

7: Type-R Touring, EX-TL | 8: SPORT

8: EX-L with Honda Sensing, SPORT | 9: Sport Touring, TOUR

9: Sport Touring, Touring

e. | Check Digit

f. | Model Year

M: '21

g. | Factory Code

U: Swindon, Wiltshire, United Kingdom

H: Alliston, Ontario, Canada

E: Greensburg, Indiana, U.S.A.

h. | Serial Number

5-door | Type-R

200101 : USA model | 200101 : USA model

300101 : Canada model | 300101 : Canada model

400101 : USA (California) model

4-door (USA plant model) | 4-door (Canada plant model)

000001 : USA model | 000001 : Canada model (K20C2)

200001 : USA (California) model | 100001 : Canada model (L15B7)

500001 : USA model (K20C2)

700001 : USA model (L15B7)

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8473: Engine Number

- Title: Engine Number
- Source path: `pages\10799.html`
- Chunk ID: `chunk_8119489a51a4`
- Images: `images\GHH409015.jpeg`, `images\GHH409016.png`, `images\GHH409017.png`, `images\GHH409018.png`, `images\GHH409019.png`, `images\GHH409020.png`, `images\GHH409021.png`
- Duplicate sources: `pages\10901.html`, `pages\10991.html`, `pages\11273.html`, `pages\20303.html`, `pages\20201.html`, `pages\20111.html`, `pages\12893.html`

### Full Text

````text
# Engine Number

Courtesy of HONDA, U.S.A., INC.

a. | Engine Type

L15BA: 1.5 L DOHC VTEC Direct Fuel-injected engine with charge air cooler and turbocharger

L15B7: 1.5 L DOHC VTEC Direct Fuel-injected engine with charge air cooler and turbocharger

K20C1: 2.0 L DOHC VTEC Direct Fuel-injected engine with charge air cooler and turbocharger

K20C2: 2.0 L DOHC i-VTEC Sequential Multiport Fuel-injected engine

b. | Serial Number

1650001 : L15BA

5000001 : K20C2 (USA engine plant)

5503001 : L15B7

5803001 : K20C2 (Canada engine plant)

6000001 : K20C1

7000001 : K20C1
````

## Chunk 8474: Transmission Number

- Title: Transmission Number
- Source path: `pages\10800.html`
- Chunk ID: `chunk_e4b4d4e06fee`
- Images: `images\GHH409022.jpeg`, `images\GHH409023.png`, `images\GHH409024.png`, `images\GHH409025.png`, `images\GHH409026.png`
- Duplicate sources: `pages\10902.html`, `pages\10992.html`, `pages\11274.html`, `pages\20304.html`, `pages\20202.html`, `pages\20112.html`, `pages\12894.html`

### Full Text

````text
# Transmission Number

Courtesy of HONDA, U.S.A., INC.

a. | Transmission Type

ECDB: 6-speed Manual (L15BA)

SDEM: 6-speed Manual (K20C1)

JDJC: CVT (K20C2)

BCGA: CVT (L15BA, L15B7)

b. | Serial Number

2000001 : ECDB

5000001 : SDEM

6000001 : JDJC

6000001 : BCGA
````

## Chunk 8475: Paint Code

- Title: Paint Code
- Source path: `pages\10801.html`
- Chunk ID: `chunk_c2341967266c`
- Images: `images\GHH409027.jpeg`
- Duplicate sources: `pages\10903.html`, `pages\10993.html`, `pages\11275.html`, `pages\20305.html`, `pages\20203.html`, `pages\20113.html`, `pages\12895.html`

### Full Text

````text
# Paint Code

Code | Color | 5-door | Type-R

USA models | Canada models | USA models | Canada models

models

models

models

models

NH-0 | Championship White | o | o

NH-731P | Crystal Black Pearl | o | o | o | o

NH-883P | Platinum White Pearl | o | o

NH-737M | Polished Metal Metallic | o | o | o | o

NH-877P | Sonic Gray Pearl | o | o | o

R-513 | Rallye Red | o | o | o | o

NH-830M | Lunar Silver Metallic | o | o

2-TONEY-82ANH-731P | Phoenix Yellow (Body) Crystal Black Pearl (Roof) | o | o

B-637P | Boost Blue Pearl | o | o

Code | Color | 4-door

USA models | Canada models

models

models

NH-731P | Crystal Black Pearl | o | o

NH-797M | Modern Steel Metallic | o | o

NH-830M | Lunar Silver Metallic | o | o

NH-883P | Platinum White Pearl | o | o

R-513 | Rallye Red | o | o

R-539P | Molten Lava Pearl | o

B-593M | Aegean Blue Metallic | o | o

B-607M | Cosmic Blue Metallic | o | o

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8476: VIN, Engine, (Motor), and Transmission Number Locations (Except Type-R)

- Title: VIN, Engine, (Motor), and Transmission Number Locations (Except Type-R)
- Source path: `pages\10802.html`
- Chunk ID: `chunk_96f85fa80157`
- Images: `images\GHH409028.jpeg`, `images\GHH409029.jpeg`
- Duplicate sources: `pages\10904.html`, `pages\10994.html`, `pages\11276.html`, `pages\20306.html`, `pages\20204.html`, `pages\20114.html`, `pages\12896.html`

### Full Text

````text
# VIN, Engine, (Motor), and Transmission Number Locations (Except Type-R)

Engine Compartment: Courtesy of HONDA, U.S.A., INC. | Front Passenger's Under Floor : Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8477: VIN, Engine, (Motor), and Transmission Number Locations (Type-R) (17-21)

- Title: VIN, Engine, (Motor), and Transmission Number Locations (Type-R) (17-21)
- Source path: `pages\10803.html`
- Chunk ID: `chunk_c46fff6886c5`
- Images: `images\GHH409030.jpeg`, `images\GHH409031.jpeg`
- Duplicate sources: `pages\10905.html`, `pages\10995.html`, `pages\11277.html`, `pages\20307.html`, `pages\20205.html`, `pages\20115.html`, `pages\12897.html`

### Full Text

````text
# VIN, Engine, (Motor), and Transmission Number Locations (Type-R) (17-21)

Engine Compartment: Courtesy of HONDA, U.S.A., INC. | Front Passenger's Under Floor : Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8478: General Information: Introduction: Symbols

- Title: General Information: Introduction: Symbols
- Source path: `pages\10804.html`
- Chunk ID: `chunk_de3f4b4fd3e4`
- Images: `images\GHH399704.png`, `images\GHH400682.png`, `images\GHH400684.png`, `images\GHH400969.png`, `images\GHH401956.png`, `images\GHH409032.png`, `images\GHH409033.png`, `images\GHH409034.png`, `images\GHH409035.png`, `images\GHH409036.png`, `images\GHH409037.png`
- Duplicate sources: `pages\10906.html`, `pages\10996.html`, `pages\11278.html`, `pages\20308.html`, `pages\20206.html`, `pages\20116.html`, `pages\12839.html`

### Full Text

````text
# General Information: Introduction: Symbols

These symbols show maintenance instructions and precautions in this service information.

Torque: N.m (kgf.m, lbf.ft)

Detailed information, notes, and precautions

Replace

Wire side

Terminal side

Apply oil

Apply brake fluid

Apply multipurpose grease

Apply specified grease

Use vacuum pump

Use insulated tools
````

## Chunk 8479: Design Specifications (2016)

- Title: Design Specifications (2016)
- Source path: `pages\10805.html`
- Chunk ID: `chunk_0f624f7da1b4`
- Images: none
- Duplicate sources: `pages\10907.html`, `pages\10997.html`, `pages\11279.html`, `pages\20309.html`, `pages\20207.html`, `pages\20117.html`, `pages\12898.html`

### Full Text

````text
# Design Specifications (2016)

Item | Measurement | Qualification | Specification

ENGINE | Fuel required (USA/Canada) | Regular UNLEADED gasoline with 87 Pump Octane Number or higher (ethanol can be used up to 15% by volume)

Fuel required (Mexico) | Regular UNLEADED gasoline with 91 Research Octane Number or higher

CLUTCH | Type | Single plate dry, diaphragm spring

MANUAL TRANSMISSION | Type | Synchronized six-speed forward, one reverse

Primary reduction | Direct 1:1

Gear ratio | 1st | 3.642

2nd | 2.080

3rd | 1.361

4th | 1.023

5th | 0.829

6th | 0.686

Reverse | 3.673

Final reduction | Type | Single helical gear

Gear ratio | 4.105

CVT | Type | Electronically-controlled continuously variable transmission, multi plate wet sump, hydraulic

Primary reduction | Direct 1:1

Gear ratio (1.5 L) | Low-High | 2.645-0.405

Reverse | 1.859-1.265

Gear ratio (2.0 L) | Low-High | 2.526-0.408

Reverse | 2.898-1.480

Final reduction (1.5 L) | Type | Single helical gear

Gear ratio | 3.238

Final reduction (2.0 L) | Type | Single helical gear

Gear ratio | 3.941

STEERING | Type | Rack and pinion with electrical power-assisted

Overall ratio | 10.94

Turns, lock-to-lock | 2.2

Steering wheel diameter | 370 mm (14.57 in)

SUSPENSION | Type | Front | MacPherson strut with stabilizer, coil spring

Rear | Independent multilink with stabilizer, coil spring

Shock absorber | Front and rear | Telescopic, hydraulic, nitrogen gas-filled

TIRES | Size | See tire information label attached to driver's doorjamb.

BRAKES | Type of service brake | Front | Power-assisted self-adjusting ventilated disc

Rear | Power-assisted self-adjusting solid disc

Type of parking brake | Electrical parking brake

Item | Measurement | Qualification | Specification

AIR CONDITIONING | Compressor | Type | Variable swash plate type

Capacity | 140 mL (8.5 cu in)/rev

Maximum speed | 9500 RPM

Condenser | Type | Corrugated fin

Evaporator | Type | Corrugated fin

Blower | Type | Stabilized swirling flow

Motor type | 235 W/12 V

Speed control | Continuously variable

Maximum capacity | 485 m 3 (17, 128 cu ft)/h

Temperature control | Air-mix type

Compressor clutch | Type | Dry, single plate, poly V-belt drive

Electrical power consumption at 68°F (20°C) | 35 W maximum at 12 V

Item | Measurement | Qualification | Specification

ELECTRICAL RATINGS | 12 volt battery | 55B24L | 12 V-47 Ah/20 HR (12 V-38 Ah/5 HR)

L2 | 12 V-60 Ah/20 HR (12 V-48 Ah/5 HR)

Fuses | Under-hood fuse/relay box | 125 A, 70 A, 60 A, 50 A, 40 A, 30 A, 20 A, 15 A, 10 A, 5 A

Under-dash fuse/relay box | 20 A, 15 A, 10 A, 5 A

Light bulbs | Headlights (low) | 12 V-55 W

LED

Headlights (high) | 12 V-60 W

LED

Front parking lights | LED

Daytime Running Lights (DRL) | LED

Front side marker lights | 12 V-3 W

Front turn signal lights | 12 V-21 W

LED

Side turn signal lights | LED

Fog lights | 12 V-35 W

Brake lights | 12 V-21 W

Taillights | LED

Inner taillight | LED

Rear side marker lights | LED

Rear turn signal lights | 12 V-21 W

Back-up lights | 4-door: 12 V-16 W

2-door: 12 V-6 W

High mount brake light | 4-door: 12 V-21 W

2-door: LED

License plate light | LED

Ceiling light | 12 V-8 W

Trunk light | 12 V-5 W

Vanity mirror lights | 12 V-2 W

Ambient light | LED

Front individual lights | 12 V-8 W

Tray light (upper/lower) | LED
````

## Chunk 8480: Design Specifications (17 Except Type-R/Si)

- Title: Design Specifications (17 Except Type-R/Si)
- Source path: `pages\10806.html`
- Chunk ID: `chunk_8fb160d4d3e4`
- Images: none
- Duplicate sources: `pages\10908.html`, `pages\10998.html`, `pages\11280.html`, `pages\20310.html`, `pages\20208.html`, `pages\20118.html`, `pages\12899.html`

### Full Text

````text
# Design Specifications (17 Except Type-R/Si)

Item | Measurement | Qualification | Specification

ENGINE | Fuel required (USA/Canada) | Regular UNLEADED gasoline with 87 Pump Octane Number or higher (ethanol can be used up to 15% by volume)

Fuel required (Mexico) | Regular UNLEADED gasoline with 91 Research Octane Number or higher

CLUTCH | Type | Single plate dry, diaphragm spring

MANUAL TRANSMISSION | Type | Synchronized six-speed forward, one reverse

Primary reduction | Direct 1:1

Gear ratio | 1st | 3.642

2nd | 2.080

3rd | 1.361

4th | 1.023

5th | 0.829

6th | 0.686

Reverse | 3.673

Final reduction | Type | Single helical gear

Gear ratio | 4.105

CVT | Type | Electronically-controlled continuously variable transmission, multi plate wet sump, hydraulic

Primary reduction | Direct 1:1

Gear ratio (1.5 L) | Low-High | 2.645-0.405

Reverse | 1.859-1.265

Gear ratio (2.0 L) | Low-High | 2.526-0.408

Reverse | 2.898-1.480

Final reduction (1.5 L) | Type | Single helical gear

Gear ratio | 3.238

Final reduction (2.0 L) | Type | Single helical gear

Gear ratio | 3.941

STEERING | Type | Rack and pinion with electrical power-assisted

Overall ratio | Without 18 inch wheels | 10.94

With 18 inch wheels | 11.10

Turns, lock-to-lock | Without 18 inch wheels | 2.20

With 18 inch wheels | 2.08

Steering wheel diameter | 370 mm (14.57 in)

SUSPENSION | Type | Front | MacPherson strut with stabilizer, coil spring

Rear | Independent multilink with stabilizer, coil spring

Shock absorber | Front and rear | Telescopic, hydraulic, nitrogen gas-filled

TIRES | Size | See tire information label attached to driver's doorjamb.

BRAKES | Type of service brake | Front | Power-assisted self-adjusting ventilated disc

Rear | Power-assisted self-adjusting solid disc

Type of parking brake | Electrical parking brake

Item | Measurement | Qualification | Specification

AIR CONDITIONING | Compressor | Type | Variable swash plate type

Capacity | 140 mL (8.5 cu in)/rev

Maximum speed | 9500 RPM

Condenser | Type | Corrugated fin

Evaporator | Type | Corrugated fin

Blower | Type | Stabilized swirling flow

Motor type | 235 W/12 V

Speed control | Continuously variable

Maximum capacity | 485 m 3 (17, 128 cu ft)/h

Temperature control | Air-mix type

Compressor clutch | Type | Dry, single plate, poly V-belt drive

Electrical power consumption at 68°F (20°C) | 35 W maximum at 12 V

Item | Measurement | Qualification | Specification

ELECTRICAL RATINGS | 12 volt battery (except 5-door) | 55B24L | 12 V-47 Ah/20 HR (12 V-38 Ah/5 HR)

L2 | 12 V-60 Ah/20 HR (12 V-48 Ah/5 HR)

12 volt battery (5-door) | 55B24L | 12 V-47 Ah/20 HR (12 V-36 Ah/5 HR)

LN2 | 12 V-60 Ah/20 HR (12 V-48 Ah/5 HR)

Fuses | Under-hood fuse/relay box | 125 A, 70 A, 60 A, 50 A, 40 A, 30 A, 20 A, 15 A, 10 A, 5 A

Under-dash fuse/relay box | 20 A, 15 A, 10 A, 5 A

Light bulbs | Headlights (low) | 12 V-55 W

LED

Headlights (high) | 12 V-60 W

LED

Front parking lights | LED

Daytime Running Lights (DRL) | LED

Front side marker lights | 12 V-3 W

Front turn signal lights | 12 V-21 W

LED

Side turn signal lights | LED

Fog lights | 12 V-35 W

Brake lights | 12 V-21 W

Taillights | LED

Inner taillight (s) | LED

Rear side marker lights | LED

Rear turn signal lights | 12 V-21 W

Back-up lights (except 2-door) | 12 V-16 W

Back-up lights (2-door) | 12 V-6 W

High mount brake light (4-door) | 12 V-21 W

High mount brake light (except 4-door) | LED

License plate light | LED

Ceiling light | 12 V-8 W

Trunk light | 12 V-5 W

Cargo area light | 12 V-5 W

Vanity mirror lights | 12 V-2 W

Ambient light | LED

Front individual map lights | 12 V-8 W

Tray light (upper/lower) | LED
````

## Chunk 8481: Design Specifications (Except Type-R/Si) (2018)

- Title: Design Specifications (Except Type-R/Si) (2018)
- Source path: `pages\10807.html`
- Chunk ID: `chunk_75ff4f089354`
- Images: none
- Duplicate sources: `pages\10909.html`, `pages\10999.html`, `pages\11281.html`, `pages\20311.html`, `pages\20209.html`, `pages\20119.html`, `pages\12900.html`

### Full Text

````text
# Design Specifications (Except Type-R/Si) (2018)

Item | Measurement | Qualification | Specification

CLUTCH | Type | Single plate dry, diaphragm spring

MANUAL TRANSMISSION | Type | Synchronized six-speed forward, one reverse

Primary reduction | Direct 1:1

Gear ratio | 1st | 3.642

2nd | 2.080

3rd | 1.361

4th | 1.023

5th | 0.829

6th | 0.686

Reverse | 3.673

Final reduction | Type | Single helical gear

Gear ratio | 4.105

CVT | Type | Electronically-controlled continuously variable transmission, multi plate wet sump, hydraulic

Primary reduction | Direct 1:1

Gear ratio (1.5 L) | Low-High | 2.645-0.405

Reverse | 1.859-1.265

Gear ratio (2.0 L) | Low-High | 2.526-0.408

Reverse | 2.898-1.480

Final reduction (1.5 L) | Type | Single helical gear

Gear ratio | 3.238

Final reduction (2.0 L) | Type | Single helical gear

Gear ratio | 3.941

STEERING | Type | Rack and pinion with electrical power-assisted

Overall ratio | Without 18 inch wheels | 10.94

With 18 inch wheels | 11.10

Turns, lock-to-lock | Without 18 inch wheels | 2.20

With 18 inch wheels | 2.08

Steering wheel diameter | 370 mm (14.57 in)

SUSPENSION | Type | Front | MacPherson strut with stabilizer, coil spring

Rear | Independent multilink with stabilizer, coil spring

Shock absorber | Front and rear | Telescopic, hydraulic, nitrogen gas-filled

TIRES | Size | See tire information label attached to driver's doorjamb.

BRAKES | Type of service brake | Front | Power-assisted self-adjusting ventilated disc

Rear | Power-assisted self-adjusting solid disc

Type of parking brake | Electrical parking brake

Item | Measurement | Qualification | Specification

AIR CONDITIONING | Compressor | Type | Variable swash plate type

Capacity | 140 mL (8.5 cu in)/rev

Maximum speed | 9500 RPM

Condenser | Type | Corrugated fin

Evaporator | Type | Corrugated fin

Blower | Type | Stabilized swirling flow

Motor type | 235 W/12 V

Speed control | Continuously variable

Maximum capacity | 485 m 3 (17, 128 cu ft)/h

Temperature control | Air-mix type

Compressor clutch | Type | Dry, single plate, poly V-belt drive

Electrical power consumption at 68°F (20°C) | 35 W maximum at 12 V

Item | Measurement | Qualification | Specification

ELECTRICAL RATINGS | 12 volt battery (except 5-door) | 55B24L | 12 V-47 Ah/20 HR (12 V-38 Ah/5 HR) 12 V-47 Ah/20 HR (12 V-36 Ah/5 HR) 12 V-45 Ah/20 HR (12 V-36 Ah/5 HR)

LN2 | 12 V-60 Ah/20 HR (12 V-48 Ah/5 HR)

12 volt battery (5-door) | 55B24L | 12 V-47 Ah/20 HR (12 V-36 Ah/5 HR)

LN2 | 12 V-60 Ah/20 HR (12 V-48 Ah/5 HR)

Fuses | Under-hood fuse/relay box | 125 A, 70 A, 60 A, 50 A, 40 A, 30 A, 20 A, 15 A, 10 A, 5 A

Under-dash fuse/relay box | 20 A, 15 A, 10 A, 5 A

Light bulbs | Headlights (low) | 12 V-55 W

LED

Headlights (high) | 12 V-60 W

LED

Front parking lights | LED

Daytime Running Lights (DRL) | LED

Front side marker lights | 12 V-3 W

Front turn signal lights | 12 V-21 W

LED

Side turn signal lights | LED

Fog lights | 12 V-35 W

Brake lights | 12 V-21 W

Taillights | LED

Inner taillight (s) | LED

Rear side marker lights | LED

Rear turn signal lights | 12 V-21 W

Back-up lights (except 2-door) | 12 V-16 W

Back-up lights (2-door) | 12 V-6 W

High mount brake light (4-door) | 12 V-21 W

High mount brake light (except 4-door) | LED

License plate light | LED

Ceiling light | 12 V-8 W

Trunk light | 12 V-5 W

Cargo area light | 12 V-5 W

Vanity mirror lights | 12 V-2 W

Ambient light | LED

Front individual map lights | 12 V-8 W

Tray light (upper/lower) | LED
````

## Chunk 8482: Design Specifications (Except Type-R/Si) (19-21)

- Title: Design Specifications (Except Type-R/Si) (19-21)
- Source path: `pages\10808.html`
- Chunk ID: `chunk_0a6480efda5e`
- Images: none
- Duplicate sources: `pages\10910.html`, `pages\11000.html`, `pages\11282.html`, `pages\20312.html`, `pages\20210.html`, `pages\20120.html`, `pages\12901.html`

### Full Text

````text
# Design Specifications (Except Type-R/Si) (19-21)

Item | Measurement | Qualification | Specification

CLUTCH | Type | Single plate dry, diaphragm spring

MANUAL TRANSMISSION | Type | Synchronized six-speed forward, one reverse

Primary reduction | Direct 1:1

Gear ratio | 1st | 3.642

2nd | 2.080

3rd | 1.361

4th | 1.023

5th | 0.829

6th | 0.686

Reverse | 3.673

Final reduction | Type | Single helical gear

Gear ratio | 4.105

CVT | Type | Electronically-controlled continuously variable transmission, multi plate wet sump, hydraulic

Primary reduction | Direct 1:1

Gear ratio (1.5 L) | Low-High | 2.645-0.405

Reverse | 1.859-1.265

Gear ratio (2.0 L) | Low-High | 2.526-0.408

Reverse | 2.898-1.480

Final reduction (1.5 L) | Type | Single helical gear

Gear ratio | 3.238

Final reduction (2.0 L) | Type | Single helical gear

Gear ratio | 3.941

STEERING | Type | Rack and pinion with electrical power-assisted

Overall ratio | Without 18 inch wheels | 10.94

With 18 inch wheels | 11.12

Turns, lock-to-lock | Without 18 inch wheels | 2.22

With 18 inch wheels | 2.11

Steering wheel diameter | 370 mm (14.57 in)

SUSPENSION | Type | Front | MacPherson strut with stabilizer, coil spring

Rear | Independent multilink with stabilizer, coil spring

Shock absorber | Front and rear | Telescopic, hydraulic, nitrogen gas-filled

TIRES | Size | See tire information label attached to driver's doorjamb.

BRAKES | Type of service brake | Front | Power-assisted self-adjusting ventilated disc

Rear | Power-assisted self-adjusting solid disc

Type of parking brake | Electrical parking brake

Item | Measurement | Qualification | Specification

AIR CONDITIONING | Compressor | Type | Variable swash plate type

Capacity | 140 mL (8.5 cu in)/rev

Maximum speed | 9500 RPM

Condenser | Type | Corrugated fin

Evaporator | Type | Corrugated fin

Blower | Type | Stabilized swirling flow

Motor type | 235 W/12 V

Speed control | Continuously variable

Maximum capacity | 485 m 3 (17, 128 cu ft)/h

Temperature control | Air-mix type

Compressor clutch | Type | Dry, single plate, poly V-belt drive

Electrical power consumption at 68°F (20°C) | 35 W maximum at 12 V

Item | Measurement | Qualification | Specification

ELECTRICAL RATINGS | 12 volt battery (except 5-door) | 55B24L | 12 V-47 Ah/20 HR (12 V-38 Ah/5 HR) 12 V-47 Ah/20 HR (12 V-36 Ah/5 HR) 12 V-45 Ah/20 HR (12 V-36 Ah/5 HR)

LN2 | 12 V-60 Ah/20 HR (12 V-48 Ah/5 HR)

12 volt battery (5-door) | 55B24L | 12 V-47 Ah/20 HR (12 V-36 Ah/5 HR)

LN2 | 12 V-60 Ah/20 HR (12 V-48 Ah/5 HR)

Fuses | Under-hood fuse/relay box | 125 A, 70 A, 60 A, 50 A, 40 A, 30 A, 20 A, 15 A, 10 A, 5 A

Under-dash fuse/relay box | 20 A, 15 A, 10 A, 5 A

Light bulbs | Headlights (low) | 12 V-55 W

LED

Headlights (high) | 12 V-60 W

LED

Front parking lights | LED

Daytime Running Lights (DRL) | LED

Front side marker lights | 12 V-3 W

Front turn signal lights | 12 V-21 W

LED

Side turn signal lights | LED

Fog lights | 12 V-35 W

LED

Brake lights | 12 V-21 W

Taillights | LED

Inner taillight (s) | LED

Rear side marker lights | LED

Rear turn signal lights | 12 V-21 W

Back-up lights (except 2-door) | 12 V-16 W

Back-up lights (2-door) | 12 V-6 W

High mount brake light (4-door) | 12 V-21 W

LED

High mount brake light (except 4-door) | LED

License plate light | LED

Ceiling light | 12 V-8 W

Trunk light | 12 V-5 W

Cargo area light | 12 V-5 W

Vanity mirror lights | 12 V-2 W

Ambient light | LED

Front individual map lights | 12 V-8 W

12 V-5 W

Glove box light | 12 V-3.4 W

LED

Tray light (upper/lower) | LED
````

## Chunk 8483: Design Specifications (Type-R/Si) (17-18)

- Title: Design Specifications (Type-R/Si) (17-18)
- Source path: `pages\10809.html`
- Chunk ID: `chunk_435615d0de34`
- Images: none
- Duplicate sources: `pages\10911.html`, `pages\11001.html`, `pages\11283.html`, `pages\20313.html`, `pages\20211.html`, `pages\20121.html`, `pages\12902.html`

### Full Text

````text
# Design Specifications (Type-R/Si) (17-18)

Item | Measurement | Qualification | Specification

ENGINE | Fuel required (USA/Canada) | UNLEADED gasoline with 91 Pump Octane Number or higher (ethanol can be used up to 15% by volume)

Fuel required (Mexico) | UNLEADED petrol with 95 Research Octane Number or higher

CLUTCH | Type | Single plate dry, diaphragm spring

MANUAL TRANSMISSION (Si) | Type | Synchronized six-speed forward, one reverse

Primary reduction | Direct 1:1

Gear ratio | 1st | 3.642

2nd | 2.080

3rd | 1.361

4th | 1.023

5th | 0.829

6th | 0.686

Reverse | 3.673

Final reduction | Type | Single helical gear

Gear ratio | 4.105

MANUAL TRANSMISSION (Type-R) | Type | Synchronized six-speed forward, one reverse

Primary reduction | Direct 1:1

Gear ratio | 1st | 3.625

2nd | 2.115

3rd | 1.529

4th | 1.125

5th | 0.911

6th | 0.734

Reverse | 3.757

Final reduction | Type | Single helical gear

Gear ratio | 4.111

STEERING | Type | Rack and pinion with electrical power-assisted

Overall ratio (Si) | 11.2

Overall ratio (Type-R) | 11.7

Turns, lock-to-lock | 2.1

Steering wheel diameter | 370 mm (14.57 in)

SUSPENSION | Type | Front | MacPherson strut with stabilizer, coil spring

Rear | Independent multilink with stabilizer, coil spring

Shock absorber | Front and rear | Telescopic, hydraulic, nitrogen gas-filled

TIRES | Size | See tire information label attached to driver's doorjamb.

BRAKES | Type of service brake | Front | Power-assisted self-adjusting ventilated disc

Rear | Power-assisted self-adjusting solid disc

Type of parking brake | Electrical parking brake

Item | Measurement | Qualification | Specification

AIR CONDITIONING | Compressor | Type | Variable capacity, swash plate type

Capacity | 140 mL (8.5 cu in)/rev

Maximum speed | 9500 RPM

Condenser | Type | Corrugated fin

Evaporator | Type | Corrugated fin

Blower | Type | Stabilized swirling flow

Motor type | 235 W/12 V

Speed control | Continuously variable

Temperature control | Air-mix type

Compressor clutch | Type | Dry, single plate, poly V-ribbed belt drive

Electrical power consumption at 68°F (20°C) | 35 W maximum at 12 V

Item | Measurement | Qualification | Specification

ELECTRICAL RATINGS | 12 volt battery | Si (USA) | 51R (55B24L): 12 V-47 Ah/20 HR (12 V-38 Ah/5 HR)

Except Si (USA) | EN LN2: 12 V-60 Ah/20 HR (12 V-48 Ah/5 HR)

Fuses | Under-hood fuse/relay box | 125 A, 70 A, 60 A, 50 A, 40 A, 30 A, 20 A, 15 A, 10 A, 5 A

Under-dash fuse/relay box | 20 A, 15 A, 10 A, 5 A

Light bulbs | Headlights (low) | 12 V-55 W

LED

Headlights (high) | 12 V-60 W

LED

Front parking lights | LED

Daytime Running Lights (DRL) | LED

Front side marker lights | 12 V-3 W

Front turn signal lights | 12 V-21 W

LED

Side turn signal lights (fender type) | 12 V-5 W

Side turn signal lights (door mirror type) | LED

Fog lights | 12 V-35 W

LED

Brake lights | 12 V-21 W

Taillights | LED

Inner taillights | LED

Rear side marker lights | LED

Rear turn signal lights | 12 V-21 W

Back-up lights (except 2-door) | 12 V-16 W

Back-up lights (2-door) | 12 V-6 W

High mount brake light | LED

License plate light | LED

Ceiling light | 12 V-8 W

Trunk area light (2/4-door) | 12 V-5 W

Cargo area light (5-door) | 12 V-5 W

Vanity mirror lights | 12 V-2 W

Ambient light | LED

Front individual map lights | 12 V-8 W

Tray light (upper/lower) | LED
````

## Chunk 8484: Design Specifications (Type-R/Si) (19-21)

- Title: Design Specifications (Type-R/Si) (19-21)
- Source path: `pages\10810.html`
- Chunk ID: `chunk_010607f8a5de`
- Images: none
- Duplicate sources: `pages\10912.html`, `pages\11002.html`, `pages\11284.html`, `pages\20314.html`, `pages\20212.html`, `pages\20122.html`, `pages\12903.html`

### Full Text

````text
# Design Specifications (Type-R/Si) (19-21)

Item | Measurement | Qualification | Specification

CLUTCH | Type | Single plate dry, diaphragm spring

MANUAL TRANSMISSION (Si) | Type | Synchronized six-speed forward, one reverse

Primary reduction | Direct 1:1

Gear ratio | 1st | 3.642

2nd | 2.080

3rd | 1.361

4th | 1.023

5th | 0.829

6th | 0.686

Reverse | 3.673

Final reduction | Type | Single helical gear

Gear ratio | 4.105

MANUAL TRANSMISSION (Type-R) | Type | Synchronized six-speed forward, one reverse

Primary reduction | Direct 1:1

Gear ratio | 1st | 3.625

2nd | 2.115

3rd | 1.529

4th | 1.125

5th | 0.911

6th | 0.734

Reverse | 3.757

Final reduction | Type | Single helical gear

Gear ratio | 4.111

STEERING | Type | Rack and pinion with electrical power-assisted

Overall ratio (Si) | 11.2

Overall ratio (Type-R) | 11.7

Turns, lock-to-lock | 2.1

Steering wheel diameter | 370 mm (14.57 in)

SUSPENSION | Type | Front | MacPherson strut with stabilizer, coil spring

Rear | Independent multilink with stabilizer, coil spring

Shock absorber | Front and rear | Telescopic, hydraulic, nitrogen gas-filled

TIRES | Size | See tire information label attached to driver's doorjamb.

BRAKES | Type of service brake | Front | Power-assisted self-adjusting ventilated disc

Rear | Power-assisted self-adjusting solid disc

Type of parking brake | Electrical parking brake

Item | Measurement | Qualification | Specification

AIR CONDITIONING | Compressor | Type | Variable capacity, swash plate type

Capacity | 140 mL (8.5 cu in)/rev

Maximum speed | 9500 RPM

Condenser | Type | Corrugated fin

Evaporator | Type | Corrugated fin

Blower | Type | Stabilized swirling flow

Motor type | 235 W/12 V

Speed control | Continuously variable

Temperature control | Air-mix type

Compressor clutch | Type | Dry, single plate, poly V-ribbed belt drive

Electrical power consumption at 68°F (20°C) | 35 W maximum at 12 V

Item | Measurement | Qualification | Specification

ELECTRICAL RATINGS | 12 volt battery | Si (USA) | 51R (55B24L): 12 V-47 Ah/20 HR (12 V-38 Ah/5 HR)

Except Si (USA) | EN LN2: 12 V-60 Ah/20 HR (12 V-48 Ah/5 HR)

Fuses | Under-hood fuse/relay box | 125 A, 70 A, 60 A, 50 A, 40 A, 30 A, 20 A, 15 A, 10 A, 5 A

Under-dash fuse/relay box | 20 A, 15 A, 10 A, 5 A

Light bulbs | Headlights (low) | 12 V-55 W

LED

Headlights (high) | 12 V-60 W

LED

Front parking lights | LED

Daytime Running Lights (DRL) | LED

Front side marker lights | 12 V-3 W

Front turn signal lights | 12 V-21 W

LED

Side turn signal lights | LED

Fog lights | 12 V-35 W

LED

Brake lights | 12 V-21 W

Taillights | LED

Inner taillights | LED

Rear side marker lights | LED

Rear turn signal lights | 12 V-21 W

Back-up lights (except 2-door) | 12 V-16 W

Back-up lights (2-door) | 12 V-6 W

High mount brake light | LED

License plate light | LED

Ceiling light | 12 V-8 W

Trunk area light (2/4-door) | 12 V-5 W

Cargo area light (5-door) | 12 V-5 W

Vanity mirror lights | 12 V-2 W

Ambient light | LED

Front individual map lights | 12 V-8 W

12 V-5 W

Glove box light | 12 V-3.4 W

LED

Tray light (upper/lower) | LED
````

## Chunk 8485: Service Information

- Title: Service Information
- Source path: `pages\10811.html`
- Chunk ID: `chunk_3b6b52cb1611`
- Images: none
- Duplicate sources: `pages\10913.html`, `pages\11003.html`, `pages\11285.html`, `pages\20315.html`, `pages\20213.html`, `pages\20123.html`, `pages\12904.html`

### Full Text

````text
# Service Information

The service and repair information contained in this service information is intended for use by qualified, professional technicians. Attempting service or repairs without the proper training, tools, and equipment could cause injury to you or others. It could also damage the vehicle or create an unsafe condition.

This service information describes the proper methods and procedures for doing service, maintenance, and repairs. Some procedures require the use of specially designed tools and dedicated equipment. Any person who intends to use a replacement part, a service procedure, or a tool that is not recommended by Honda, must determine the risks to their personal safety and the safe operation of the vehicle.

If you need to replace any parts, always use the correct parts supplied by a Honda dealer. Never use inferior quality parts.
````

## Chunk 8486: For Your Customer's Safety

- Title: For Your Customer's Safety
- Source path: `pages\10812.html`
- Chunk ID: `chunk_d16ee8bfde5c`
- Images: none
- Duplicate sources: `pages\10914.html`, `pages\11004.html`, `pages\11286.html`, `pages\20316.html`, `pages\20214.html`, `pages\20124.html`, `pages\12905.html`

### Full Text

````text
# For Your Customer's Safety

Proper service and maintenance are essential to the customer's safety and the reliability of the vehicle. Any error or oversight while servicing a vehicle can result in faulty operation, damage to the vehicle, or injury to others.

WARNING:

Improper service or repairs can create an unsafe condition that can cause your customers or others to be seriously hurt or killed.

Follow the procedures and precautions in this service information and other service materials carefully.
````

## Chunk 8487: For Your Safety

- Title: For Your Safety
- Source path: `pages\10813.html`
- Chunk ID: `chunk_6d0309a472f0`
- Images: none
- Duplicate sources: `pages\10915.html`, `pages\11005.html`, `pages\11287.html`, `pages\20317.html`, `pages\20215.html`, `pages\20125.html`, `pages\12906.html`

### Full Text

````text
# For Your Safety

Because this service information is intended for a professional service technician, we do not provide warnings about many basic shop safety practices (for example, hot parts-wear gloves). If you have not received shop safety training or do not feel confident about your knowledge of safe servicing practices, we recommend that you do not attempt to do the procedures described in this service information.

WARNING:

Failure to properly follow instructions and precautions can cause you to be seriously hurt or killed.

Follow the procedures and precautions in this service information carefully.

Some of the most important general service safety precautions follow this text. However, we cannot warn you of every conceivable hazard that can arise in doing service and repair procedures. Only you can decide whether or not you should do a given task.
````

## Chunk 8488: Important Safety Precautions

- Title: Important Safety Precautions
- Source path: `pages\10814.html`
- Chunk ID: `chunk_2e1261c0bb36`
- Images: none
- Duplicate sources: `pages\10916.html`, `pages\11006.html`, `pages\11288.html`, `pages\20318.html`, `pages\20216.html`, `pages\20126.html`, `pages\12907.html`

### Full Text

````text
# Important Safety Precautions

- Make sure you have a clear understanding of all basic shop safety practices, and that you are wearing appropriate clothing and using safety equipment. When doing any service task, be especially careful of the following:

- Read all of the instructions before you begin, and make sure you have the tools, the replacement or repair parts, and the skills required to do the tasks safely and completely. Protect your eyes by using proper safety glasses, goggles, or face shields anytime you hammer, drill, grind, or work around pressurized air or liquids and springs, or other stored-energy components. If there is any doubt, put on eye protection. Use other protective wear when necessary, such as gloves or safety shoes. Handling hot or sharp parts can cause severe burns or cuts. Before you grab something that looks like it can hurt you, stop and put on gloves. Protect yourself and others whenever you have the vehicle up in the air. Anytime you raise the vehicle, either with a lift or a jack, make sure that it is always securely supported. Use safety stands if needed. Protect yourself by wearing an approved welding helmet, gloves, and safety shoes anytime you are welding. You can receive burns from hot parts; allow the parts to cool before working in that area. Protect yourself from paints and harmful chemicals by wearing an approved respirator, eye protection, and gloves whenever you are painting. Spray paint only in an approved paint booth that is well ventilated.

- Read all of the instructions before you begin, and make sure you have the tools, the replacement or repair parts, and the skills required to do the tasks safely and completely.

- Protect your eyes by using proper safety glasses, goggles, or face shields anytime you hammer, drill, grind, or work around pressurized air or liquids and springs, or other stored-energy components. If there is any doubt, put on eye protection.

- Use other protective wear when necessary, such as gloves or safety shoes. Handling hot or sharp parts can cause severe burns or cuts. Before you grab something that looks like it can hurt you, stop and put on gloves.

- Protect yourself and others whenever you have the vehicle up in the air. Anytime you raise the vehicle, either with a lift or a jack, make sure that it is always securely supported. Use safety stands if needed.

- Protect yourself by wearing an approved welding helmet, gloves, and safety shoes anytime you are welding. You can receive burns from hot parts; allow the parts to cool before working in that area.

- Protect yourself from paints and harmful chemicals by wearing an approved respirator, eye protection, and gloves whenever you are painting. Spray paint only in an approved paint booth that is well ventilated.

- Make sure the engine is off before you begin any servicing procedures, unless the instruction tells you to do otherwise. This will help eliminate several potential hazards:

- Carbon monoxide poisoning from engine exhaust. Be sure there is adequate ventilation whenever you run the engine. Burns from hot parts or coolant. Let the engine and exhaust system cool before working in those areas. Injury from moving parts. If the instruction tells you to run the engine, be sure your hands, fingers, and clothing are out of the way.

- Carbon monoxide poisoning from engine exhaust. Be sure there is adequate ventilation whenever you run the engine.

- Burns from hot parts or coolant. Let the engine and exhaust system cool before working in those areas.

- Injury from moving parts. If the instruction tells you to run the engine, be sure your hands, fingers, and clothing are out of the way.

- Gasoline vapors and hydrogen gases from batteries are explosive. To reduce the possibility of a fire or explosion, be careful when working around gasoline or batteries:

- Use only a nonflammable solvent, not gasoline, to clean parts. Never drain or store gasoline in an open container. Keep all cigarettes, sparks, and flames away from the battery and all fuel-related parts.

- Use only a nonflammable solvent, not gasoline, to clean parts.

- Never drain or store gasoline in an open container.

- Keep all cigarettes, sparks, and flames away from the battery and all fuel-related parts.
````

## Chunk 8489: System Warning/Indicator Index

- Title: System Warning/Indicator Index
- Source path: `pages\10815.html`
- Chunk ID: `chunk_2bca5d4a238d`
- Images: `images\GHH409038.jpeg`, `images\GHH409039.jpeg`, `images\GHH409040.jpeg`, `images\GHH409041.png`, `images\GHH409042.png`, `images\GHH409043.png`, `images\GHH409044.png`, `images\GHH409045.png`, `images\GHH409046.png`, `images\GHH409047.png`, `images\GHH409048.png`, `images\GHH409049.png`, `images\GHH409050.png`, `images\GHH409051.png`, `images\GHH409052.png`, `images\GHH409053.png`, `images\GHH409054.png`, `images\GHH409055.png`, `images\GHH409056.jpeg`, `images\GHH409057.png`, `images\GHH409058.png`, `images\GHH409059.png`, `images\GHH409060.png`, `images\GHH409061.png`, `images\GHH409062.png`, `images\GHH409063.jpeg`, `images\GHH409064.png`, `images\GHH409065.jpeg`, `images\GHH409066.png`, `images\GHH409067.jpeg`, `images\GHH409068.png`, `images\GHH409069.jpeg`, `images\GHH409070.png`, `images\GHH409071.png`, `images\GHH409072.jpeg`, `images\GHH409073.png`, `images\GHH409074.jpeg`, `images\GHH409075.png`, `images\GHH409076.jpeg`, `images\GHH409077.png`, `images\GHH409078.jpeg`, `images\GHH409079.png`, `images\GHH409080.jpeg`, `images\GHH409081.jpeg`, `images\GHH409082.png`, `images\GHH409083.png`, `images\GHH409084.png`, `images\GHH409085.png`, `images\GHH409086.jpeg`, `images\GHH409087.jpeg`, `images\GHH409088.png`, `images\GHH409089.jpeg`, `images\GHH409090.png`, `images\GHH409091.jpeg`, `images\GHH409092.png`, `images\GHH409093.jpeg`, `images\GHH409094.png`, `images\GHH409095.png`, `images\GHH409096.jpeg`, `images\GHH409097.png`, `images\GHH409098.png`, `images\GHH409099.jpeg`, `images\GHH409100.png`, `images\GHH409101.png`, `images\GHH409102.jpeg`, `images\GHH409103.png`, `images\GHH409104.png`, `images\GHH409105.jpeg`, `images\GHH409106.png`, `images\GHH409107.png`, `images\GHH409108.jpeg`, `images\GHH409109.png`, `images\GHH409110.jpeg`, `images\GHH409111.jpeg`, `images\GHH409112.png`, `images\GHH409113.png`
- Duplicate sources: `pages\10917.html`, `pages\11007.html`, `pages\11289.html`, `pages\20319.html`, `pages\20217.html`, `pages\20127.html`, `pages\12908.html`

### Full Text

````text
# System Warning/Indicator Index

Without Multi-Information Display (MID)

Courtesy of HONDA, U.S.A., INC.

With Multi-Information Display (MID)

Courtesy of HONDA, U.S.A., INC.

NOTE:

- Check the diagnostic trouble code (DTC) with the HDS, then refer to the indicated DTC's troubleshooting.

- There are some indicators displayed on the multi-information display (MID).

Indicator | Indicator Name | Fault Detection Unit | HDS System Menu (DTC Check) | Diagnostic Procedure

Courtesy of HONDA, U.S.A., INC. | SECURITY INDICATOR (Red) | BODY CONTROL MODULE | Without keyless access system: IMMOBI Immobilizer setup Immobilizer Info System Check | Immobilizer system check Immobilizer system symptom troubleshooting information Immobilizer system symptom troubleshooting index

- Immobilizer system check

- Immobilizer system symptom troubleshooting information

- Immobilizer system symptom troubleshooting index

With keyless access system: ONE-PUSH START Backup Control Unit System Information System Check ONE-PUSH START Backup Control Unit System Information Status Log ONE-PUSH START KEYLESS ACCESS CONTROL Unit KEYLESS ACCESS System Information System Check 1 ONE-PUSH START KEYLESS ACCESS CONTROL Unit KEYLESS ACCESS System Information System Check 2 | Keyless access system check Keyless access system symptom troubleshooting information Keyless access system symptom troubleshooting index

ONE-PUSH START Backup Control Unit System Information Status Log

ONE-PUSH START KEYLESS ACCESS CONTROL Unit KEYLESS ACCESS System Information System Check 1

ONE-PUSH START KEYLESS ACCESS CONTROL Unit KEYLESS ACCESS System Information System Check 2

- Keyless access system check

- Keyless access system symptom troubleshooting information

- Keyless access system symptom troubleshooting index

Courtesy of HONDA, U.S.A., INC. | KEYLESS ACCESS INDICATOR (Amber) | BODY CONTROL MODULE | ONE-PUSH START PCU DTCs ONE-PUSH START Backup Control Unit DTCs ONE-PUSH START KEYLESS ACCESS CONTROL Unit DTCs | Body control module DTC troubleshooting index Keyless access system symptom troubleshooting information Keyless access system symptom troubleshooting index

ONE-PUSH START Backup Control Unit DTCs

ONE-PUSH START KEYLESS ACCESS CONTROL Unit DTCs

- Body control module DTC troubleshooting index

- Keyless access system symptom troubleshooting information

- Keyless access system symptom troubleshooting index

Courtesy of HONDA, U.S.A., INC. | 12 VOLT CHARGING SYSTEM INDICATOR (Red) | PCM | PGM FI DTCs/Freeze Data | Fuel and emissions systems general troubleshooting information Fuel and emissions systems DTC TROUBLESHOOTING INDEX Fuel and emissions systems symptom troubleshooting index Charging system symptom troubleshooting index

- Fuel and emissions systems general troubleshooting information

- Fuel and emissions systems DTC TROUBLESHOOTING INDEX

- Fuel and emissions systems symptom troubleshooting index

- Charging system symptom troubleshooting index

Courtesy of HONDA, U.S.A., INC. | MALFUNCTION INDICATOR LAMP (MIL) (Amber) | PCM | PGM FI DTCs/Freeze Data | Fuel and emissions systems general troubleshooting information Fuel and emissions systems DTC TROUBLESHOOTING INDEX Fuel and emissions systems symptom troubleshooting index

- Fuel and emissions systems general troubleshooting information

- Fuel and emissions systems DTC TROUBLESHOOTING INDEX

- Fuel and emissions systems symptom troubleshooting index

Courtesy of HONDA, U.S.A., INC. | EPS INDICATOR (Amber) | EPS CONTROL UNIT | EPS DTCs/Freeze Data | EPS system general troubleshooting information EPS system DTC troubleshooting index EPS system symptom troubleshooting index

- EPS system general troubleshooting information

- EPS system DTC troubleshooting index

- EPS system symptom troubleshooting index

Courtesy of HONDA, U.S.A., INC. | SRS INDICATOR (Red) | SRS UNIT | SRS SRS/SWS DTCs | SRS general troubleshooting information SRS DTC troubleshooting index SRS symptom troubleshooting index

- SRS general troubleshooting information

- SRS DTC troubleshooting index

- SRS symptom troubleshooting index

Indicator | Indicator Name | Fault Detection Unit | HDS System Menu (DTC Check) | Diagnostic Procedure

Courtesy of HONDA, U.S.A., INC. | VSA INDICATOR (Amber) | VSA MODULATOR-CONTROL UNIT | ABS/TCS/VSA DTCs | VSA system general troubleshooting information VSA system DTC troubleshooting index VSA system symptom troubleshooting index

- VSA system general troubleshooting information
````

## Chunk 8490: System Warning/Indicator Index

- Title: System Warning/Indicator Index
- Source path: `pages\10815.html`
- Chunk ID: `chunk_92631737ae29`
- Images: `images\GHH409038.jpeg`, `images\GHH409039.jpeg`, `images\GHH409040.jpeg`, `images\GHH409041.png`, `images\GHH409042.png`, `images\GHH409043.png`, `images\GHH409044.png`, `images\GHH409045.png`, `images\GHH409046.png`, `images\GHH409047.png`, `images\GHH409048.png`, `images\GHH409049.png`, `images\GHH409050.png`, `images\GHH409051.png`, `images\GHH409052.png`, `images\GHH409053.png`, `images\GHH409054.png`, `images\GHH409055.png`, `images\GHH409056.jpeg`, `images\GHH409057.png`, `images\GHH409058.png`, `images\GHH409059.png`, `images\GHH409060.png`, `images\GHH409061.png`, `images\GHH409062.png`, `images\GHH409063.jpeg`, `images\GHH409064.png`, `images\GHH409065.jpeg`, `images\GHH409066.png`, `images\GHH409067.jpeg`, `images\GHH409068.png`, `images\GHH409069.jpeg`, `images\GHH409070.png`, `images\GHH409071.png`, `images\GHH409072.jpeg`, `images\GHH409073.png`, `images\GHH409074.jpeg`, `images\GHH409075.png`, `images\GHH409076.jpeg`, `images\GHH409077.png`, `images\GHH409078.jpeg`, `images\GHH409079.png`, `images\GHH409080.jpeg`, `images\GHH409081.jpeg`, `images\GHH409082.png`, `images\GHH409083.png`, `images\GHH409084.png`, `images\GHH409085.png`, `images\GHH409086.jpeg`, `images\GHH409087.jpeg`, `images\GHH409088.png`, `images\GHH409089.jpeg`, `images\GHH409090.png`, `images\GHH409091.jpeg`, `images\GHH409092.png`, `images\GHH409093.jpeg`, `images\GHH409094.png`, `images\GHH409095.png`, `images\GHH409096.jpeg`, `images\GHH409097.png`, `images\GHH409098.png`, `images\GHH409099.jpeg`, `images\GHH409100.png`, `images\GHH409101.png`, `images\GHH409102.jpeg`, `images\GHH409103.png`, `images\GHH409104.png`, `images\GHH409105.jpeg`, `images\GHH409106.png`, `images\GHH409107.png`, `images\GHH409108.jpeg`, `images\GHH409109.png`, `images\GHH409110.jpeg`, `images\GHH409111.jpeg`, `images\GHH409112.png`, `images\GHH409113.png`
- Duplicate sources: `pages\10917.html`, `pages\11007.html`, `pages\11289.html`, `pages\20319.html`, `pages\20217.html`, `pages\20127.html`, `pages\12908.html`

### Full Text

````text
oubleshooting information

- EPS system DTC troubleshooting index

- EPS system symptom troubleshooting index

Courtesy of HONDA, U.S.A., INC. | SRS INDICATOR (Red) | SRS UNIT | SRS SRS/SWS DTCs | SRS general troubleshooting information SRS DTC troubleshooting index SRS symptom troubleshooting index

- SRS general troubleshooting information

- SRS DTC troubleshooting index

- SRS symptom troubleshooting index

Indicator | Indicator Name | Fault Detection Unit | HDS System Menu (DTC Check) | Diagnostic Procedure

Courtesy of HONDA, U.S.A., INC. | VSA INDICATOR (Amber) | VSA MODULATOR-CONTROL UNIT | ABS/TCS/VSA DTCs | VSA system general troubleshooting information VSA system DTC troubleshooting index VSA system symptom troubleshooting index

- VSA system general troubleshooting information

- VSA system DTC troubleshooting index

- VSA system symptom troubleshooting index

Courtesy of HONDA, U.S.A., INC. | VSA OFF INDICATOR (Amber) | VSA MODULATOR- CONTROL UNIT | ABS/TCS/VSA DTCs | VSA system general troubleshooting information VSA system DTC troubleshooting index VSA system symptom troubleshooting index

- VSA system general troubleshooting information

- VSA system DTC troubleshooting index

- VSA system symptom troubleshooting index

Courtesy of HONDA, U.S.A., INC. | ABS INDICATOR (Amber) | VSA MODULATOR-CONTROL UNIT | ABS/TCS/VSA DTCs | VSA system general troubleshooting information VSA system DTC troubleshooting index VSA system symptom troubleshooting index

- VSA system general troubleshooting information

- VSA system DTC troubleshooting index

- VSA system symptom troubleshooting index

Courtesy of HONDA, U.S.A., INC. | BRAKE SYSTEM INDICATOR (Red) | VSA MODULATOR-CONTROL UNIT | ABS/TCS/VSA DTCs | VSA system general troubleshooting information VSA system DTC troubleshooting index VSA system symptom troubleshooting index

- VSA system general troubleshooting information

- VSA system DTC troubleshooting index

- VSA system symptom troubleshooting index

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC. | BRAKE SYSTEM INDICATOR (Amber) | VSA MODULATOR-CONTROL UNIT MULTIPURPOSE CAMERA UNIT PCM | ABS/TCS/VSA DTCs DRIVING SUPPORT Integrated Driver Support System DTCs PGM FI DTCs/Freeze Data | VSA system general troubleshooting information VSA system DTC troubleshooting index VSA system symptom troubleshooting index Brake system symptom troubleshooting index Driving support system DTC troubleshooting index Driving support system symptom troubleshooting index Fuel and emissions systems general troubleshooting information Fuel and emissions systems DTC TROUBLESHOOTING INDEX Fuel and emissions systems symptom troubleshooting index

- VSA MODULATOR-CONTROL UNIT

- MULTIPURPOSE CAMERA UNIT

- PCM

DRIVING SUPPORT Integrated Driver Support System DTCs

PGM FI DTCs/Freeze Data

- VSA system general troubleshooting information

- VSA system DTC troubleshooting index

- VSA system symptom troubleshooting index

- Brake system symptom troubleshooting index

- Driving support system DTC troubleshooting index

- Driving support system symptom troubleshooting index

- Fuel and emissions systems general troubleshooting information

- Fuel and emissions systems DTC TROUBLESHOOTING INDEX

- Fuel and emissions systems symptom troubleshooting index

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC. | LOW TIRE PRESSURE/TPMS INDICATOR (Amber) | VSA MODULATOR-CONTROL UNIT | ABS/TCS/VSA DTCs | TPMS general troubleshooting information TPMS DTC troubleshooting index TPMS symptom troubleshooting index

- TPMS general troubleshooting information

- TPMS DTC troubleshooting index

- TPMS symptom troubleshooting index

Courtesy of HONDA, U.S.A., INC. | ADAPTIVE DAMPER SYSTEM WARNING | ADAPTIVE DAMPER CONTROL UNIT | Active Damper System/Adaptive Damper System DTCs/Freeze Data | Adaptive damper system general troubleshooting information Adaptive damper system DTC troubleshooting index Adaptive damper system symptom troubleshooting index

- Adaptive damper system general troubleshooting information

- Adaptive damper system DTC troubleshooting index

- Adaptive damper system symptom troubleshooting index

Courtesy of HONDA, U.S.A., INC. | SHIFT POSITION INDICATOR | TCM | AT DTCs/Freeze Data | CVT system general troubleshooting information CVT system DTC troubleshooting index CVT system symptom troubleshooting index

- CVT system general troubleshooting information

- CVT system DTC troubleshooting index
````

## Chunk 8491: System Warning/Indicator Index

- Title: System Warning/Indicator Index
- Source path: `pages\10815.html`
- Chunk ID: `chunk_430fcc4ee028`
- Images: `images\GHH409038.jpeg`, `images\GHH409039.jpeg`, `images\GHH409040.jpeg`, `images\GHH409041.png`, `images\GHH409042.png`, `images\GHH409043.png`, `images\GHH409044.png`, `images\GHH409045.png`, `images\GHH409046.png`, `images\GHH409047.png`, `images\GHH409048.png`, `images\GHH409049.png`, `images\GHH409050.png`, `images\GHH409051.png`, `images\GHH409052.png`, `images\GHH409053.png`, `images\GHH409054.png`, `images\GHH409055.png`, `images\GHH409056.jpeg`, `images\GHH409057.png`, `images\GHH409058.png`, `images\GHH409059.png`, `images\GHH409060.png`, `images\GHH409061.png`, `images\GHH409062.png`, `images\GHH409063.jpeg`, `images\GHH409064.png`, `images\GHH409065.jpeg`, `images\GHH409066.png`, `images\GHH409067.jpeg`, `images\GHH409068.png`, `images\GHH409069.jpeg`, `images\GHH409070.png`, `images\GHH409071.png`, `images\GHH409072.jpeg`, `images\GHH409073.png`, `images\GHH409074.jpeg`, `images\GHH409075.png`, `images\GHH409076.jpeg`, `images\GHH409077.png`, `images\GHH409078.jpeg`, `images\GHH409079.png`, `images\GHH409080.jpeg`, `images\GHH409081.jpeg`, `images\GHH409082.png`, `images\GHH409083.png`, `images\GHH409084.png`, `images\GHH409085.png`, `images\GHH409086.jpeg`, `images\GHH409087.jpeg`, `images\GHH409088.png`, `images\GHH409089.jpeg`, `images\GHH409090.png`, `images\GHH409091.jpeg`, `images\GHH409092.png`, `images\GHH409093.jpeg`, `images\GHH409094.png`, `images\GHH409095.png`, `images\GHH409096.jpeg`, `images\GHH409097.png`, `images\GHH409098.png`, `images\GHH409099.jpeg`, `images\GHH409100.png`, `images\GHH409101.png`, `images\GHH409102.jpeg`, `images\GHH409103.png`, `images\GHH409104.png`, `images\GHH409105.jpeg`, `images\GHH409106.png`, `images\GHH409107.png`, `images\GHH409108.jpeg`, `images\GHH409109.png`, `images\GHH409110.jpeg`, `images\GHH409111.jpeg`, `images\GHH409112.png`, `images\GHH409113.png`
- Duplicate sources: `pages\10917.html`, `pages\11007.html`, `pages\11289.html`, `pages\20319.html`, `pages\20217.html`, `pages\20127.html`, `pages\12908.html`

### Full Text

````text
x

Courtesy of HONDA, U.S.A., INC. | ADAPTIVE DAMPER SYSTEM WARNING | ADAPTIVE DAMPER CONTROL UNIT | Active Damper System/Adaptive Damper System DTCs/Freeze Data | Adaptive damper system general troubleshooting information Adaptive damper system DTC troubleshooting index Adaptive damper system symptom troubleshooting index

- Adaptive damper system general troubleshooting information

- Adaptive damper system DTC troubleshooting index

- Adaptive damper system symptom troubleshooting index

Courtesy of HONDA, U.S.A., INC. | SHIFT POSITION INDICATOR | TCM | AT DTCs/Freeze Data | CVT system general troubleshooting information CVT system DTC troubleshooting index CVT system symptom troubleshooting index

- CVT system general troubleshooting information

- CVT system DTC troubleshooting index

- CVT system symptom troubleshooting index

Courtesy of HONDA, U.S.A., INC. | LKAS INDICATOR (Amber) | MULTIPURPOSE CAMERA UNIT | DRIVING SUPPORT Integrated Driver Support System DTCs | Driving support system DTC troubleshooting index Driving support system symptom troubleshooting index LKAS general troubleshooting information LKAS symptom troubleshooting index

- Driving support system DTC troubleshooting index

- Driving support system symptom troubleshooting index

- LKAS general troubleshooting information

- LKAS symptom troubleshooting index

Indicator | Indicator Name | Fault Detection Unit | HDS System Menu (DTC Check) | Diagnostic Procedure

Courtesy of HONDA, U.S.A., INC. | ACC INDICATOR (Amber) | MULTIPURPOSE CAMERA UNIT | DRIVING SUPPORT Integrated Driver Support System DTCs | Driving support system DTC troubleshooting index Driving support system symptom troubleshooting index ACC system general troubleshooting information ACC system symptom troubleshooting index

- Driving support system DTC troubleshooting index

- Driving support system symptom troubleshooting index

- ACC system general troubleshooting information

- ACC system symptom troubleshooting index

Courtesy of HONDA, U.S.A., INC. | COLLISION MITIGATION BRAKE SYSTEM (CMBS) INDICATOR (Amber) | MULTIPURPOSE CAMERA UNIT | DRIVING SUPPORT Integrated Driver Support System DTCs | Driving support system DTC troubleshooting index Driving support system symptom troubleshooting index CMBS general troubleshooting information CMBS symptom troubleshooting index

- Driving support system DTC troubleshooting index

- Driving support system symptom troubleshooting index

- CMBS general troubleshooting information

- CMBS symptom troubleshooting index

Courtesy of HONDA, U.S.A., INC. | ROAD DEPARTURE MITIGATION (RDM) INDICATOR (Amber) | MULTIPURPOSE CAMERA UNIT | DRIVING SUPPORT Integrated Driver Support System DTCs | Driving support system DTC troubleshooting index Driving support system symptom troubleshooting index RDM system general troubleshooting information RDM system symptom troubleshooting index

- Driving support system DTC troubleshooting index

- Driving support system symptom troubleshooting index

- RDM system general troubleshooting information

- RDM system symptom troubleshooting index

Courtesy of HONDA, U.S.A., INC. | AUTO HIGH-BEAM INDICATOR (Amber) | MULTIPURPOSE CAMERA UNIT | DRIVING SUPPORT Integrated Driver Support System DTCs | Driving support system DTC troubleshooting index Driving support system symptom troubleshooting index High-beam support system general troubleshooting information

- Driving support system DTC troubleshooting index

- Driving support system symptom troubleshooting index

- High-beam support system general troubleshooting information

Courtesy of HONDA, U.S.A., INC. | STARTER SYSTEM INDICATOR (Amber) | PCM | PGM FI DTCs/Freeze Data | Fuel and emissions systems general troubleshooting information Fuel and emissions systems DTC TROUBLESHOOTING INDEX Fuel and emissions systems symptom troubleshooting index Starting system symptom troubleshooting index

- Fuel and emissions systems general troubleshooting information

- Fuel and emissions systems DTC TROUBLESHOOTING INDEX

- Fuel and emissions systems symptom troubleshooting index

- Starting system symptom troubleshooting index

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC. | LIGHT CONTROL INDICATOR (Amber) | BODY CONTROL MODULE | BODY ELECTRICAL Lighting DTCs | Body control module DTC troubleshooting index Exterior lights symptom troubleshooting

- Body control module DTC troubleshooting index

- Exterior lights symptom troubleshooting
````

## Chunk 8492: CANADIAN Model Cross-Reference: ACURA

- Title: CANADIAN Model Cross-Reference: ACURA
- Source path: `pages\10817.html`
- Chunk ID: `chunk_26325736d81c`
- Images: none
- Duplicate sources: `pages\20219.html`

### Full Text

````text
# CANADIAN Model Cross-Reference: ACURA

Canadian Model | US Model

1996-2000 1.6EL | Canadian Only (Based on 1996-2000 Japanese Market Honda Domani)

2001-2005 1.7EL | 2001-2005 Honda Civic

2004-2005 EL | 2004-2005 Honda Civic

2006-2011 CSX | 2006-2011 Honda Civic
````

## Chunk 8493: CANADIAN Model Cross-Reference: ASUNA

- Title: CANADIAN Model Cross-Reference: ASUNA
- Source path: `pages\10818.html`
- Chunk ID: `chunk_26cfc8ed34a5`
- Images: none
- Duplicate sources: `pages\20220.html`

### Full Text

````text
# CANADIAN Model Cross-Reference: ASUNA

Canadian Model | US Model

1992-93 Sunfire | 1990-92 Isuzu Impulse & 1990-93 Geo Storm ("R" Body)

1993 GT/ SE | 1988-93 Pontiac LeMans ("T Body)

1992-93 Sunrunner | 1989-99 Geo Tracker ("J" Body)
````

## Chunk 8494: CANADIAN Model Cross-Reference: AUDI

- Title: CANADIAN Model Cross-Reference: AUDI
- Source path: `pages\10819.html`
- Chunk ID: `chunk_03a62ef7c615`
- Images: none
- Duplicate sources: `pages\20221.html`

### Full Text

````text
# CANADIAN Model Cross-Reference: AUDI

Canadian Model | US Model

1985-86 Quattro | Nearest Match: 1984 Quattro Similar To: 1985-86 Coupe

1996-97 S6 | Nearest Match: 1996-97 A6
````

## Chunk 8495: CANADIAN Model Cross-Reference: BMW

- Title: CANADIAN Model Cross-Reference: BMW
- Source path: `pages\10820.html`
- Chunk ID: `chunk_b9f04ddb6add`
- Images: none
- Duplicate sources: `pages\20222.html`

### Full Text

````text
# CANADIAN Model Cross-Reference: BMW

Canadian Model | US Model

2012 320i | Canadian only Nearest Match: 2013 320i

2006-11 323i | Canadian only

2016 335i | Canadian only

2016 335i xDrive | Canadian only

2016 740Li xDrive | Canadian only

2016 760Li | Canadian only

2016 ActiveHybrid 3 | Canadian only

2016 ActiveHybrid 7 | Canadian only

2012 X1 | Canadian only
````

## Chunk 8496: CHRYSLER Corp.: CHRYSLER

- Title: CHRYSLER Corp.: CHRYSLER
- Source path: `pages\10821.html`
- Chunk ID: `chunk_9ba88e783f39`
- Images: none
- Duplicate sources: `pages\20223.html`

### Full Text

````text
# CHRYSLER Corp.: CHRYSLER

Canadian Model | US Model

1984-93 Daytona | 1984-93 Dodge Daytona

1988-93 Dynasty | 1988-93 Dodge Dynasty

1993-04 Intrepid | 1993-04 Dodge Intrepid

2000-02 Neon | 2000-02 Dodge Neon

2021 Grand Caravan | Canadian Only
````

## Chunk 8497: CHRYSLER Corp.: Dodge

- Title: CHRYSLER Corp.: Dodge
- Source path: `pages\10822.html`
- Chunk ID: `chunk_5ace89cbf912`
- Images: none
- Duplicate sources: `pages\20224.html`

### Full Text

````text
# CHRYSLER Corp.: Dodge

Canadian Model | US Model

1989-90 2000 | 1989-90 Mitsubishi Galant

1992-93 Colt Wagon | 1992-93 Plymouth Colt Vista

1994 Colt Wagon | 1994 Mitsubishi Expo (LRV)

1987-88 Expo | 1987-88 Colt Vista

1995-96 Colt | 1995-96 Eagle Summit 1995-96 Mitsubishi Mirage

2003-05 SX | 2003-05 Neon
````

## Chunk 8498: CHRYSLER Corp.: Eagle

- Title: CHRYSLER Corp.: Eagle
- Source path: `pages\10823.html`
- Chunk ID: `chunk_b622845050d0`
- Images: none
- Duplicate sources: `pages\20225.html`

### Full Text

````text
# CHRYSLER Corp.: Eagle

Canadian Model | US Model

1991-93 2000 GTX | 1989-93 Mitsubishi Galant

1989-91 Vista (Sedan/Notchback) | 1989-91 Dodge Colt

1992 Vista | 1992 Plymouth Colt

1989-91 Vista Wagon | 1989-91 Dodge Colt Vista
````

## Chunk 8499: CHRYSLER Corp.: PLYMOUTH

- Title: CHRYSLER Corp.: PLYMOUTH
- Source path: `pages\10824.html`
- Chunk ID: `chunk_067d53d508d2`
- Images: none
- Duplicate sources: `pages\20226.html`

### Full Text

````text
# CHRYSLER Corp.: PLYMOUTH

Canadian Model | US Model

1978-81 Caravelle | 1978-87 Dodge Diplomat

1982-84 Caravelle | 1982-84 Gran Fury Also: Dodge 600

1990-92 Colt 100/200 | 1990-92 Colt

1995-96 Colt | 1995-96 Eagle Summit 1995-96 Mitsubishi Mirage

1992-94 Colt Wagon | 1992-94 Mitsubishi Expo (LRV)

1987-89 Expo | 1987-89 Colt Vista
````

## Chunk 8500: General Motors: BUICK

- Title: General Motors: BUICK
- Source path: `pages\10825.html`
- Chunk ID: `chunk_5b5b831b1e30`
- Images: none
- Duplicate sources: `pages\20227.html`

### Full Text

````text
# General Motors: BUICK

Canadian Model | US Model

2005-10 Allure | 2005-10 Buick LaCrosse

1986-87 Somerset Regal | 1986-87 Regal (Somerset is a Regal trim level)
````

## Chunk 8501: General Motors: CHEVROLET

- Title: General Motors: CHEVROLET
- Source path: `pages\10826.html`
- Chunk ID: `chunk_eaea2607c701`
- Images: none
- Duplicate sources: `pages\20228.html`

### Full Text

````text
# General Motors: CHEVROLET

Canadian Model | US Model

1989-92 Sprint | 1989-92 Geo Metro 1989-92 Suzuki Swift

1989-92 Tracker | 1989-92 Geo Tracker 1989-92 Suzuki Sidekick

2004-08 Optra (Sedan/Wagon) | 2004-08 Suzuki Forenza

2004-08 Optra5 | 2004-08 Suzuki Reno

2004-06 Epica | 2004-06 Suzuki Verona

2012-14 Orlando | Canadian Only

2009 Uplander | Canadian Only Best Match: 2008 Uplander

2013-14 Chevrolet Trax | 2015 Chevrolet Trax
````

## Chunk 8502: General Motors: GMC

- Title: General Motors: GMC
- Source path: `pages\10827.html`
- Chunk ID: `chunk_f60fc7065a33`
- Images: none
- Duplicate sources: `pages\20229.html`

### Full Text

````text
# General Motors: GMC

Canadian Model | US Model

1989-92 Tracker | 1989-94 Geo Tracker

2002-05 Jimmy | 2002-05 Chevrolet Blazer (Not TrailBlazer)
````

## Chunk 8503: General Motors: Optima

- Title: General Motors: Optima
- Source path: `pages\10829.html`
- Chunk ID: `chunk_0fe13b9eb9ce`
- Images: none
- Duplicate sources: `pages\20231.html`

### Full Text

````text
# General Motors: Optima

Canadian Model | US Model

1988-91 Optima (Passport) | 1988-91 Pontiac LeMans ("T" Body)
````

## Chunk 8504: General Motors: PONTIAC

- Title: General Motors: PONTIAC
- Source path: `pages\10830.html`
- Chunk ID: `chunk_fceb3f1f6247`
- Images: none
- Duplicate sources: `pages\20232.html`

### Full Text

````text
# General Motors: PONTIAC

Canadian Model | US Model

1982 Parisienne | Best Match: 1983 Parisienne

1985-89 Firefly | 1985-89 Chevrolet Sprint

1990-00 Firefly | 1990-00 Suzuki Swift 1998-00 Chevrolet Metro

1987-91 Tempest | 1987-91 Chevrolet Corsica

2007 Montana SV6 | 2007 Buick Terraza 2007 Saturn Relay 2007 Chevrolet Uplander

2008-09 Montana SV6 | 2008 Chevrolet Uplander

1982-83 Grand LeMans | 1982-82 Bonneville 1981 Oldsmobile Cutlass

1985-87 Sunburst | 1985-87 Chevrolet Spectrum

1994-97 Sunrunner | 1994-97 Geo Tracker

2005-09 Wave & G3 Wave | 2005-09 Chevrolet Aveo

2010 G3 | 2010 Chevrolet Aveo

2010 G5 | 2010 Chevrolet Cobalt

2005-08 G5 Pursuit, G5, & Pursuit | 2005-08 Chevrolet Cobalt

1982-87 Acadian | 1982-87 Chevrolet Chevette
````

## Chunk 8505: CANADIAN Model Cross-Reference: HYUNDAI

- Title: CANADIAN Model Cross-Reference: HYUNDAI
- Source path: `pages\10831.html`
- Chunk ID: `chunk_c9354782e75a`
- Images: none
- Duplicate sources: `pages\20233.html`

### Full Text

````text
# CANADIAN Model Cross-Reference: HYUNDAI

Canadian Model | US Model

2015 Elantra Coupe | Canadian Only

1984-87 Pony | Canadian Only

2013-18 Santa Fe XL | Canadian Only 2013-18 Santa Fe

1985-88 Stellar | Canadian Only
````

## Chunk 8506: CANADIAN Model Cross-Reference: KIA

- Title: CANADIAN Model Cross-Reference: KIA
- Source path: `pages\10833.html`
- Chunk ID: `chunk_c01c9eade99b`
- Images: none
- Duplicate sources: `pages\20235.html`

### Full Text

````text
# CANADIAN Model Cross-Reference: KIA

Canadian Model | US Model

2010-11 Borrego | Canadian Only Best Match: 2009 Borrego

2017 Forte Koup | Canadian Only Best Match: 2017 Forte/Forte5

2001-10 Magentis | 2001-10 Optima

2011-12 Rondo | Canadian Only Best Match: 2010 Rondo
````

## Chunk 8507: CANADIAN Model Cross-Reference: MAZDA

- Title: CANADIAN Model Cross-Reference: MAZDA
- Source path: `pages\10834.html`
- Chunk ID: `chunk_ce1b5c74d6b4`
- Images: none
- Duplicate sources: `pages\20236.html`

### Full Text

````text
# CANADIAN Model Cross-Reference: MAZDA

Canadian Model | US Model

1992-96 MX3 Precidia | 1992-95 MX3

1995 323 | 1995 Protege

2016-17 Mazda 5 | Canadian Only

1997 B3000 | 1997 B4000 1997 Ford Ranger

2010 B-Series Trucks | Canadian Only Best Match: 2009 B-Series Trucks

2022 CX-3 | Canadian Only

1993-97 MX6 Mystere | 1993-97 MX6 193-97 Ford Probe

1992-95 929 Serenia | 1988-95 929

1993-97 626 Cronos | 1988-97 626
````

## Chunk 8508: CANADIAN Model Cross-Reference: MERCEDES-BENZ

- Title: CANADIAN Model Cross-Reference: MERCEDES-BENZ
- Source path: `pages\10835.html`
- Chunk ID: `chunk_05469f106ce9`
- Images: none
- Duplicate sources: `pages\20237.html`

### Full Text

````text
# CANADIAN Model Cross-Reference: MERCEDES-BENZ

Canadian Model | US Model

1992 350SD / 350SDL | 1992 300SD

2019-22 A250 | Canadian Only

2022 A35 AMG | Canadian Only

2006-11 B200 | Canadian Only

2013-19 B250 | Canadian Only

2008-09 C230 | 2008-09 C300

2010-11 C250 | 2010-11 C300

2009 CLK63 | Canadian Only Best Match: 2008 CLK63

2022-23 CLS53 AMG | Canadian Only

2007 E280 | 2007 E320

2008-09 E300 | 2008-09 E350

2012-15 E300 | Canadian Only

2016-17 GLE350d | Canadian Only

2018 GLE400 | Canadian Only

2016-18 GLE550 | Canadian Only

2015 ML550 | Canadian Only

2013 R350 | Canadian Only

2008-11 S450 | 2010-11 S400

2010 SL5502010 SL63 | Canadian Only

2010 SL63 | Canadian Only
````

## Chunk 8509: CANADIAN Model Cross-Reference: MERKUR

- Title: CANADIAN Model Cross-Reference: MERKUR
- Source path: `pages\10837.html`
- Chunk ID: `chunk_3fd9bff3a31d`
- Images: none
- Duplicate sources: `pages\20239.html`

### Full Text

````text
# CANADIAN Model Cross-Reference: MERKUR

Canadian Model | US Model

1987 Scorpio | Canadian Only Best Match: 1988 Scorpio
````

## Chunk 8510: CANADIAN Model Cross-Reference: MITSUBISHI

- Title: CANADIAN Model Cross-Reference: MITSUBISHI
- Source path: `pages\10838.html`
- Chunk ID: `chunk_ac2be4e5b4f4`
- Images: none
- Duplicate sources: `pages\20240.html`

### Full Text

````text
# CANADIAN Model Cross-Reference: MITSUBISHI

Canadian Model | US Model

2009 Endeavor | Canadian Only Best Match: 2008 Endeavor

2011-22 RVR | 2011-22 Outlander Sport
````

## Chunk 8511: CANADIAN Model Cross-Reference: NISSAN

- Title: CANADIAN Model Cross-Reference: NISSAN
- Source path: `pages\10839.html`
- Chunk ID: `chunk_a5c36f12bf93`
- Images: none
- Duplicate sources: `pages\20241.html`

### Full Text

````text
# CANADIAN Model Cross-Reference: NISSAN

Canadian Model | US Model

1991-95 Axxess Wagon | Canadian Only Best Match: 1990 Axxess Wagon

1986-88 Multi Wagon | 1986-88 Stanza Wagon

1984 Micra | Canadian Only

2015-19 Micra | Canadian Only

2017-22 Qashqai | 2017-2022 Rogue Sport

2005-06 X-Trail | Canadian Only
````

## Chunk 8512: CANADIAN Model Cross-Reference: RENAULT

- Title: CANADIAN Model Cross-Reference: RENAULT
- Source path: `pages\10840.html`
- Chunk ID: `chunk_5df5020fc954`
- Images: none
- Duplicate sources: `pages\20242.html`

### Full Text

````text
# CANADIAN Model Cross-Reference: RENAULT

Canadian Model | US Model

1984-86 LeCar | Canadian Only Best Match: 1983 LeCar
````

## Chunk 8513: CANADIAN Model Cross-Reference: SATURN

- Title: CANADIAN Model Cross-Reference: SATURN
- Source path: `pages\10841.html`
- Chunk ID: `chunk_b303f6bd65e2`
- Images: none
- Duplicate sources: `pages\20243.html`

### Full Text

````text
# CANADIAN Model Cross-Reference: SATURN

Canadian Model | US Model

2009 Astra | Canadian Only Same As: 2008 Astra
````

## Chunk 8514: CANADIAN Model Cross-Reference: Smart

- Title: CANADIAN Model Cross-Reference: Smart
- Source path: `pages\10842.html`
- Chunk ID: `chunk_e24694b5f075`
- Images: none
- Duplicate sources: `pages\20244.html`

### Full Text

````text
# CANADIAN Model Cross-Reference: Smart

Canadian Model | US Model

2005-07 Fortwo | Canadian Only Best Match: 2008 Fortwo
````

## Chunk 8515: CANADIAN Model Cross-Reference: SUBARU

- Title: CANADIAN Model Cross-Reference: SUBARU
- Source path: `pages\10843.html`
- Chunk ID: `chunk_9eb0bcf21a9d`
- Images: none
- Duplicate sources: `pages\20245.html`

### Full Text

````text
# CANADIAN Model Cross-Reference: SUBARU

Canadian Model | US Model

1988-89 Chaser | 1988-89 GL (Chaser is a hatchback version of the GL)
````

## Chunk 8516: CANADIAN Model Cross-Reference: SUZUKI

- Title: CANADIAN Model Cross-Reference: SUZUKI
- Source path: `pages\10844.html`
- Chunk ID: `chunk_89d721746ff0`
- Images: none
- Duplicate sources: `pages\20246.html`

### Full Text

````text
# CANADIAN Model Cross-Reference: SUZUKI

Canadian Model | US Model

1986-88 Forsa | 1986-88 Chevrolet Sprint

1982-85 Samurai (SJ410) | Canadian Only

2004-08 Swift+ | 2004-08 Chevrolet Aveo

2009 Swift+ | 2009 Chevrolet Aveo
````

## Chunk 8517: CANADIAN Model Cross-Reference: TOYOTA

- Title: CANADIAN Model Cross-Reference: TOYOTA
- Source path: `pages\10845.html`
- Chunk ID: `chunk_35ec24077073`
- Images: none
- Duplicate sources: `pages\20247.html`

### Full Text

````text
# CANADIAN Model Cross-Reference: TOYOTA

Canadian Model | US Model

1998-99 Paseo | Canadian Only Best Match: 1997 Paseo

1999 Tercel | Canadian Only Best Match: 1998 Tercel

2006 Yaris | Canadian Only Best Match: 2007 Yaris

2014 Matrix | Canadian Only Best Match: 2013 Matrix

2016 Venza | Canadian Only Best Match: 2015 Venza
````

## Chunk 8518: CANADIAN Model Cross-Reference: VOLKSWAGEN

- Title: CANADIAN Model Cross-Reference: VOLKSWAGEN
- Source path: `pages\10846.html`
- Chunk ID: `chunk_62828efa0102`
- Images: none
- Duplicate sources: `pages\20248.html`

### Full Text

````text
# CANADIAN Model Cross-Reference: VOLKSWAGEN

Canadian Model | US Model

1995 Corrado | Canadian Only

1992 & 1994 EuroVan (Gas) | Canadian Only Best Match: 1993 Eurovan

1993-97 EuroVan (Diesel) | Canadian Only (No Diesel Eurovans Sold in U.S.)

2007-08 Golf (A5) | Canadian Only Best Match: 2006 Golf

2008-09 Golf (A6) | Canadian Only Best Match: 2010 Golf

1993 GTI | Canadian Only Best Match: 1993 Cabriolet

1994 GTI | Canadian Only Best Match: 1994 Jetta III

1989 Scirocco | Same As: 1988 Scirocco

1985-92 Transporter Van/Pickup | Canadian Only

1993-03 Transporter Van | 1993-03 EuroVan
````

## Chunk 8519: CANADIAN Model Cross-Reference: VOLVO

- Title: CANADIAN Model Cross-Reference: VOLVO
- Source path: `pages\10847.html`
- Chunk ID: `chunk_8e590e2ea3d6`
- Images: none
- Duplicate sources: `pages\20249.html`

### Full Text

````text
# CANADIAN Model Cross-Reference: VOLVO

Canadian Model | US Model

1987-88 244 & 245 | Canadian Only Best Match: 1987-88 240

2007 C30 | Canadian Only Best Match: 2007 S40, V50, C70 Are Similar
````

## Chunk 8520: Conversion Table

- Title: Conversion Table
- Source path: `pages\10918.html`
- Chunk ID: `chunk_b0be04e8daf4`
- Images: none
- Duplicate sources: `pages\20148.html`

### Full Text

````text
# Conversion Table

Liter | CID

1.0 | 59

1.0 | 60

1.0 | 61

1.1 | 66

1.1 | 68

1.1 | 70

1.2 | 71

1.2 | 72

1.2 | 73

1.2 | 76

1.3 | 77

1.3 | 78

1.3 | 79

1.3 | 80

1.3 | 81

1.3 | 82

1.4 | 85

1.4 | 85

1.4 | 86

1.5 | 89

1.5 | 90

1.5 | 91

1.6 | 94

1.6 | 95

1.6 | 96

1.6 | 97

1.6 | 98

1.6 | 99

1.7 | 102

1.7 | 103

1.7 | 105

1.8 | 107

1.8 | 109

1.8 | 110

1.8 | 111

1.8 | 112

1.9 | 113

1.9 | 114

1.9 | 116

1.9 | 119

2.0 | 119

2.0 | 120

2.0 | 121

2.0 | 122

2.1 | 125

2.1 | 126

2.1 | 128

2.1 | 129

2.1 | 130

2.1 | 131

2.2 | 132

2.2 | 133

2.2 | 134

2.2 | 135

2.2 | 136

2.2 | 137

2.3 | 138

2.3 | 140

2.3 | 141

2.3 | 143

2.4 | 143

2.4 | 144

2.4 | 145

2.4 | 146

2.4 | 147

2.4 | 149

2.5 | 150

2.5 | 151

2.5 | 152

2.5 | 153

2.6 | 155

2.6 | 156

2.6 | 157

2.6 | 158

2.6 | 159

2.7 | 162

2.7 | 163

2.7 | 164

2.7 | 167

2.8 | 168

2.8 | 170

2.8 | 171

2.8 | 173

2.9 | 174

2.9 | 179

3.0 | 180

3.0 | 181

3.0 | 182

3.0 | 183

3.0 | 184

3.1 | 191

3.1 | 192

3.2 | 193

3.2 | 194

3.2 | 195

3.2 | 196

3.2 | 197

3.2 | 198

3.3 | 199

3.3 | 200

3.3 | 201

3.3 | 204

3.4 | 206

3.4 | 207

3.4 | 209

3.5 | 210

3.5 | 211

3.5 | 212

3.5 | 213

3.5 | 214

3.5 | 215

3.6 | 219

3.6 | 220

3.7 | 225

3.7 | 226

3.7 | 229

3.8 | 229

3.8 | 230

3.8 | 231

3.8 | 232

3.8 | 234

3.8 | 238

3.9 | 239

3.9 | 240

3.9 | 241

4.0 | 241

4.0 | 242

4.0 | 243

4.0 | 244

4.1 | 250

4.1 | 252

4.2 | 255

4.2 | 258

4.3 | 259

4.3 | 260

4.3 | 262

4.3 | 263

4.3 | 266

4.4 | 266

4.4 | 267

4.4 | 268

4.5 | 273

4.5 | 274

4.5 | 276

4.6 | 278

4.6 | 279

4.6 | 281

4.6 | 283

4.7 | 284

4.7 | 285

4.7 | 287

4.7 | 289

4.8 | 290

4.8 | 292

4.9 | 300

4.9 | 301

4.9 | 302

5.0 | 302

5.0 | 304

5.0 | 305

5.0 | 307

5.1 | 310

5.2 | 315

5.2 | 318

5.3 | 326

5.4 | 327

5.4 | 328

5.4 | 330

5.5 | 334

5.5 | 335

5.6 | 340

5.6 | 343

5.7 | 345

5.7 | 348

5.7 | 350

5.8 | 351

5.8 | 352

5.9 | 359

5.9 | 360

5.9 | 361

5.9 | 362

6.0 | 366

6.0 | 368

6.1 | 370

6.1 | 372

6.2 | 379

6.2 | 381

6.3 | 383

6.4 | 389

6.4 | 390

6.4 | 392

6.5 | 396

6.6 | 400

6.6 | 401

6.6 | 402

6.6 | 403

6.7 | 410

6.8 | 412

6.8 | 413

6.8 | 414

6.8 | 415

6.9 | 420

6.9 | 421

7.0 | 425

7.0 | 426

7.0 | 427

7.0 | 428

7.0 | 429

7.0 | 430

7.1 | 432

7.2 | 440

7.4 | 454

7.5 | 455

7.5 | 460

7.6 | 462

8.0 | 488

8.2 | 500

8.8 | 534

8.8 | 537

8.8 | 538

8.9 | 540

9.0 | 549

9.1 | 555

9.3 | 568

9.3 | 570

9.6 | 588

9.8 | 600

9.9 | 605

10.0 | 611
````

## Chunk 8521: Metric Conversions: Notes

- Title: Metric Conversions: Notes
- Source path: `pages\10919.html`
- Chunk ID: `chunk_728c4748e005`
- Images: none
- Duplicate sources: `pages\20142.html`

### Full Text

````text
# Metric Conversions: Notes

Metric conversions are making life more difficult for the mechanic. In addition to increasing the number of tools required, metric-dimensioned nuts and bolts are used alongside English components in many new vehicles. The mechanic has to decide which tool to use, slowing down the job. The tool problem can be solved by trial and error, but some metric conversions aren't so simple.

Converting temperature, lengths or volumes requires a calculator and conversion charts, or else a very nimble mind. Conversion charts are only part of the answer though, because they don't help you "think" metric, or "visualize" what you are converting. The following examples are intended to help you "see" metric sizes:
````

## Chunk 8522: Metric Conversions: Length

- Title: Metric Conversions: Length
- Source path: `pages\10920.html`
- Chunk ID: `chunk_e70bfa20b2df`
- Images: none
- Duplicate sources: `pages\20143.html`

### Full Text

````text
# Metric Conversions: Length

Meters are the standard unit of length in the metric system. The smaller units are 10ths (decimeter), 100ths (centimeter), and 1000ths (millimeter) of a meter. These common examples might help you to visualize the metric units:

- A meter is slightly longer than a yard (about 40 inches).

- An aspirin tablet is about one centimeter across (.4 inches).

- A millimeter is about the thickness of a dime.
````

## Chunk 8523: Metric Conversions: Volume

- Title: Metric Conversions: Volume
- Source path: `pages\10921.html`
- Chunk ID: `chunk_ce9837404688`
- Images: none
- Duplicate sources: `pages\20144.html`

### Full Text

````text
# Metric Conversions: Volume

The metric weight system is based on the gram, with the most common unit being the kilogram (1000 grams). Our comparable units are ounces and pounds:

- A kilogram is about 2.2 pounds.

- A kilogram is about 2.2 pounds.
````

## Chunk 8524: Metric Conversions: Torque

- Title: Metric Conversions: Torque
- Source path: `pages\10922.html`
- Chunk ID: `chunk_b89dc3fb0b70`
- Images: none
- Duplicate sources: `pages\20145.html`

### Full Text

````text
# Metric Conversions: Torque

Torque is somewhat complicated. The term describes the amount of effort exerted to turn something. A chosen unit of weight or force is applied to a lever of standard length. The resulting leverage is called torque. In our standard system, we use the weight of one pound applied to a lever a foot long, resulting in the unit called a foot-pound. A smaller unit is the inch-pound (the lever is one inch long). Metric units include the meter kilogram (lever one meter long with a kilogram of weight applied) and the Newton-meter (lever one meter long with force of one Newton applied). Some conversions are:

- A meter kilogram is about 7.2 foot pounds.

- A foot pound is about 1.4 Newton-meters.

- A centimeter kilogram (cmkg) is equal to .9 inch pounds.
````

## Chunk 8525: Metric Conversions: Pressure

- Title: Metric Conversions: Pressure
- Source path: `pages\10923.html`
- Chunk ID: `chunk_c676b56519c1`
- Images: none
- Duplicate sources: `pages\20146.html`

### Full Text

````text
# Metric Conversions: Pressure

Pressure is another complicated measurement. Pressure is described as a force or weight applied to a given area. Our common unit is pounds per square inch. Metric units can be expressed in several ways. One is the kilogram per square centimeter (kg/cm 2 ). Another unit of pressure is the Pascal (force of one Newton on an area of one square meter), which equals about 4 ounces on a square yard. Since this is a very small amount of pressure, we usually see the kiloPascal, or kPa (1000 Pascals). Another common automotive term for pressure is the bar (used by German manufacturers), which equals 10 Pascals. Thoroughly confused? Try the examples below:

- Atmospheric pressure at sea level is about 14.7 psi.

- Atmospheric pressure at sea level is about 1 bar.

- Atmospheric pressure at sea level is about 1 kg/cm 2 .

- One pound per square inch is about 7 kPa.
````

## Chunk 8526: Conversion Factors

- Title: Conversion Factors
- Source path: `pages\10924.html`
- Chunk ID: `chunk_2e83056954fa`
- Images: none
- Duplicate sources: `pages\20147.html`

### Full Text

````text
# Conversion Factors

To Convert | To | Multiply By

LENGTH

Millimeters (mm) | Inches | .03937

Inches | Millimeters | 25.4

Meters (M) | Inches | 39.37

Meters (M) | Feet | 3.28084

Feet | Meters | .3048

Kilometers (Km) | Miles | .62137

AREA

Square Centimeters (cm 2 ) | Square Inches | .155

Square Inches | Square Centimeters | 6.45159

VOLUME

Cubic Centimeters | Cubic Inches | .06103

Cubic Inches | Cubic Centimeters | 16.38703

Liters | Cubic Inches | 61.025

Cubic Inches | Liters | .01639

Liters | Quarts | 1.05672

Quarts | Liters | .94633

Liters | Pints | 2.11344

Pints | Liters | .47317

Liters | Ounces | 33.81497

Ounces | Liters | .02957

WEIGHT

Grams | Ounces | .03527

Ounces | Grams | 28.34953

Kilograms | Pounds | 2.20462

Pounds | Kilograms | .45359

WORK

Centimeter Kilograms | Inch Pounds | .8676

Pounds/Sq. Inch | Kilograms/Sq. Centimeter | .07031

Bar | Pounds/Sq. Inch | 14.504

Pounds/Sq. Inch | Bar | .06895

Atmosphere | Pounds/Sq. Inch | 14.696

Pounds/Sq. Inch | Atmosphere | .06805

TEMPERATURE

Centigrade Degrees | Fahrenheit Degrees | (C°x 9 / 5 )+32

Fahrenheit Degrees | Centigrade Degrees | (F°-32)x 5 / 9

Inches | Decimals | mm

1/64 | .016 | .397

1/32 | .031 | .794

3/64 | .047 | 1.191

1/16 | .063 | 1.588

5/64 | .078 | 1.984

3/32 | .094 | 2.381

7/64 | .109 | 2.778

1/8 | .125 | 3.175

9/64 | .141 | 3.572

5/32 | .156 | 3.969

11/64 | .172 | 4.366

3/16 | .188 | 4.763

13/64 | .203 | 5.159

7/32 | .219 | 5.556

15/64 | .234 | 5.953

1/4 | .250 | 6.350

17/64 | .266 | 6.747

9/32 | .281 | 7.144

19/64 | .297 | 7.541

5/16 | .313 | 7.938

21/64 | .328 | 8.334

11/32 | .344 | 8.731

23/64 | .359 | 9.128

3/8 | .375 | 9.525

25/64 | .391 | 9.992

13/32 | .406 | 10.319

27/64 | .422 | 10.716

7/16 | .438 | 11.113

29/64 | .453 | 11.509

15/32 | .469 | 11.906

31/64 | .484 | 12.303

1/2 | .500 | 12.700

33/64 | .516 | 13.097

17/32 | .531 | 13.494

35/64 | .547 | 13.891

9/16 | .563 | 14.288

37/64 | .578 | 14.684

19/32 | .594 | 15.081

39/64 | .609 | 15.478

5/8 | .625 | 15.875

41/64 | .641 | 16.272

21/32 | .656 | 16.669

43/64 | .672 | 17.066

11/16 | .687 | 17.463

45/64 | .703 | 17.859

23/32 | .719 | 18.256

47/64 | .734 | 18.653

3/4 | .750 | 19.050

49/64 | .766 | 19.447

25/32 | .781 | 19.844

51/64 | .797 | 20.241

13/16 | .813 | 20.638

53/64 | .828 | 21.034

27/32 | .844 | 21.431

55/64 | .859 | 21.828

7/8 | .875 | 22.225

57/64 | .891 | 22.622

29/32 | .906 | 23.019

59/64 | .922 | 23.416

15/16 | .938 | 23.813

61/64 | .953 | 24.209

31/32 | .969 | 24.606

63/64 | .984 | 25.003

1 | 1.000 | 25.400
````

## Chunk 8527: Auto Stop/Start Disable: Notes

- Title: Auto Stop/Start Disable: Notes
- Source path: `pages\10929.html`
- Chunk ID: `chunk_a1bc59c5a973`
- Images: none
- Duplicate sources: `pages\20134.html`

### Full Text

````text
# Auto Stop/Start Disable: Notes
````

## Chunk 8528: Disable Conditions

- Title: Disable Conditions
- Source path: `pages\10930.html`
- Chunk ID: `chunk_319ac0a7245a`
- Images: none
- Duplicate sources: `pages\20135.html`

### Full Text

````text
# Disable Conditions

On Honda vehicles equipped with the auto stop/start feature, there may or may not be an auto stop/start off button. For vehicles without the button, any or some of the following conditions may prevent the engine from automatically stopping while parked:

- Transmission is in P position

- Engine compartment hood is open

- Driver's seat belt is unlatched

- Driver's door is open

- Windshield defroster is on

- A/C is set to Manual and is running at Max.
````

## Chunk 8529: Disable Button

- Title: Disable Button
- Source path: `pages\10931.html`
- Chunk ID: `chunk_49b87f3bdc3f`
- Images: `images\G00572186.png`
- Duplicate sources: `pages\20136.html`

### Full Text

````text
# Disable Button

Vehicles with the auto stop/start off button, press the button to switch the system off. The button may illuminate. Deactivation using the button lasts only one key cycle. Press the button again to restore auto stop/start function. See Fig 1 .
````

## Chunk 8530: Torque Specifications (USA/Canada models Type-R/Si) (2017 2018 2019 2020 2021)

- Title: Torque Specifications (USA/Canada models Type-R/Si) (2017 2018 2019 2020 2021)
- Source path: `pages\11014.html`
- Chunk ID: `chunk_13ca729a24d4`
- Images: `images\GHH412691.png`, `images\GHH412692.png`, `images\GHH412693.jpeg`
- Duplicate sources: `pages\15598.html`

### Full Text

````text
# Torque Specifications (USA/Canada models Type-R/Si) (2017 2018 2019 2020 2021)

NOTE:

- Refer to the appropriate portion of the service information for the precautions and complete procedures.

- Refer to the appropriate portion of the service information for the bolts/nuts not indicated here.

- 1: Parts to be tightened in a particular order. 2: Follow the appropriate service information procedures closely for torque, sequence, and special steps.

- 1: Parts to be tightened in a particular order.

- 2: Follow the appropriate service information procedures closely for torque, sequence, and special steps.

- When using some special tools or crowfoot-type wrenches, the torque value changes due to the added leverage. The actual torque applied will be greater than the torque reading shown.

- The torque specification given is the actual torque, not the reading on the torque wrench. To compensate for this additional leverage, use the formula below to calculate the torque value reading on the torque wrench. Always use the special tool or crowfoot-type wrench in a straight line with the torque wrench, or you will apply improper torque.

- The torque specification given is the actual torque, not the reading on the torque wrench.

- To compensate for this additional leverage, use the formula below to calculate the torque value reading on the torque wrench.

- Always use the special tool or crowfoot-type wrench in a straight line with the torque wrench, or you will apply improper torque.

Courtesy of HONDA, U.S.A., INC.

Engine Electrical (L15B7: Si)

Location | Item | Remark | Torque

Starting system | Starter bolt (10 mm) | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Starter bolt (12 mm) | 65 N.m (6.6 kgf.m, 48 lbf.ft)

Positive starter cable nut | 9.0 N.m (0.92 kgf.m, 6.6 lbf.ft)

Ignition system | Spark plugs | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Charging system | Alternator bolts | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Positive alternator cable nut | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Drive belt auto-tensioner bolt (8 mm) | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Drive belt auto-tensioner bolt (10 mm) | 55 N.m (5.6 kgf.m, 41 lbf.ft)

Engine Electrical (K20C1: Type-R)

Location | Item | Remark | Torque

Starting system | Starter bolt (10 mm) | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Starter bolt (12 mm) | 65 N.m (6.6 kgf.m, 48 lbf.ft)

Positive starter cable nut | 9.0 N.m (0.92 kgf.m, 6.6 lbf.ft)

Ignition system | Spark plugs | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Charging system | Alternator bolts (8 mm)*1 | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Alternator bolt (10 mm)*1 | 37 N.m (3.8 kgf.m, 27 lbf.ft)

Positive alternator cable nut | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Drive belt auto-tensioner bolt (8 mm) | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Drive belt auto-tensioner bolt (10 mm) | 55 N.m (5.6 kgf.m, 41 lbf.ft)

Engine Mechanical (L15B7: Si)

Location | Item | Remark | Torque

Engine assembly | Side engine mount bolts (12 mm) | Use new bolts | 49 N.m (5.0 kgf.m, 36 lbf.ft)

Side engine mount bolts (14 mm) | Use new bolts | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Side engine mount nut | Use new nut | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Side engine mount bracket bolts | Use new bolts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Torque rod bolts *2 | Use new bolts | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Torque rod bracket bolts | Use new bolts | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Transmission mount bolts | Use new bolts | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Transmission mount bracket bolts | Use new bolts | 78 N.m (8.0 kgf.m, 58 lbf.ft)

Transmission mount bracket nuts | Use new nuts | 78 N.m (8.0 kgf.m, 58 lbf.ft)

Engine lubrication | Oil pressure switch | Apply liquid gasket on threads | 18 N.m (1.8 kgf.m, 13 lbf.ft)

Oil pan drain bolt | Use new washer | 40 N.m (4.1 kgf.m, 30 lbf.ft)

Oil filter | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Intake manifold and exhaust system | Intake manifold bolts *1 | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Intake manifold nuts *1 | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Exhaust pipe A self-locking nuts | TWC side | Use new gasket and nuts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Muffler self-locking nuts | Use new gasket and nuts | 33 N.m (3.4 kgf.m, 24 lbf.ft)

Turbocharger self-locking nuts*2 | Use new gasket and nuts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Turbocharger bolts*2 | Use new gasket | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Engine Mechanical (K20C1: Type-R)

Location | Item | Remark | Torque

Engine assembly | Side engine mount bolts (12 mm) | Use new bolts | 49 N.m (5.0 kgf.m, 36 lbf.ft)
````

## Chunk 8531: Torque Specifications (USA/Canada models Type-R/Si) (2017 2018 2019 2020 2021)

- Title: Torque Specifications (USA/Canada models Type-R/Si) (2017 2018 2019 2020 2021)
- Source path: `pages\11014.html`
- Chunk ID: `chunk_2055eb3364a5`
- Images: `images\GHH412691.png`, `images\GHH412692.png`, `images\GHH412693.jpeg`
- Duplicate sources: `pages\15598.html`

### Full Text

````text
f.m, 13 lbf.ft)

Oil pan drain bolt | Use new washer | 40 N.m (4.1 kgf.m, 30 lbf.ft)

Oil filter | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Intake manifold and exhaust system | Intake manifold bolts *1 | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Intake manifold nuts *1 | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Exhaust pipe A self-locking nuts | TWC side | Use new gasket and nuts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Muffler self-locking nuts | Use new gasket and nuts | 33 N.m (3.4 kgf.m, 24 lbf.ft)

Turbocharger self-locking nuts*2 | Use new gasket and nuts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Turbocharger bolts*2 | Use new gasket | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Engine Mechanical (K20C1: Type-R)

Location | Item | Remark | Torque

Engine assembly | Side engine mount bolts (12 mm) | Use new bolts | 49 N.m (5.0 kgf.m, 36 lbf.ft)

Side engine mount bolts (14 mm) | Use new bolts | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Side engine mount nut | Use new nut | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Side engine mount bracket bolts | Use new bolts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Torque rod bolts *2 | Use new bolts | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Torque rod bracket bolts | Use new bolts | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Transmission mount bolts | Use new bolts | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Transmission mount bracket bolts | Use new bolts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Transmission mount bracket nuts | Use new nuts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Engine lubrication | Oil pan drain bolt | Use new washer | 40 N.m (4.1 kgf.m, 30 lbf.ft)

Oil filter | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Intake manifold and exhaust system | Intake manifold bolts *1 | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Intake manifold nuts *1 | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Exhaust pipe A self-locking nuts | TWC side | Use new gasket and nuts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Muffler self-locking nuts | Use new gasket and nuts | 33 N.m (3.4 kgf.m, 24 lbf.ft)

Turbocharger self-locking nuts*2 | Use new gasket and nuts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Turbocharger bolts*2 | Use new gasket | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Engine Cooling (L15B7: Si)

Location | Item | Remark | Torque

Cooling system | Water passage bolts | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Water passage nuts | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Thermostat housing bolts | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Thermostat housing nuts | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Engine Cooling (K20C1: Type-R)

Location | Item | Remark | Torque

Cooling system | Water passage bolts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Water passage nuts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Thermostat housing bolts | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Thermostat housing nuts | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Fuel Emissions (L15B7: Si)

Location | Item | Remark | Torque

Fuel and emissions | Accelerator pedal module | 13 N.m (1.3 kgf.m, 10 lbf.ft)

A/F sensor | 45 N.m (4.6 kgf.m, 33 lbf.ft)

ECT Sensor 1/2 | Use new O-ring | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Exhaust chamber cover | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Fuel tank*2 | Fuel tank bolts | 23 N.m (2.3 kgf.m, 17 lbf.ft)

Support strap bolts | 38 N.m (3.9 kgf.m, 28 lbf.ft)

Knock sensor | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Secondary HO2S | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Throttle body bolts*2 | Use new gasket | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Catalytic converter bracket bolts*2 | Catalytic converter side | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Engine side | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Catalytic converter upper bolts | Use new gaskets and nuts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Catalytic converter upper nuts | Use new gaskets and nuts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Fuel Emissions (K20C1: Type-R)

Location | Item | Remark | Torque

Fuel and emissions | Accelerator pedal module | 13 N.m (1.3 kgf.m, 10 lbf.ft)

A/F sensor | 45 N.m (4.6 kgf.m, 33 lbf.ft)

ECT Sensor 1/2 | Use new O-ring | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Exhaust chamber cover | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Fuel tank*2 | Fuel tank bolts | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Support strap bolts | 38 N.m (3.9 kgf.m, 28 lbf.ft)

Knock sensor | 20 N.m (2.0 kgf.m, 15 lbf.ft)

Rocker arm oil pressure switch | Use new O-ring | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Rocker arm oil pressure sensor | Use new O-ring | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Secondary HO2S | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Throttle body bolts*2 | Use new gasket | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Catalytic converter bracket bolts*2 | Catalytic converter side | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Engine side | 45 N.m (4.6 kgf.m, 33 lbf.ft)
````

## Chunk 8532: Torque Specifications (USA/Canada models Type-R/Si) (2017 2018 2019 2020 2021)

- Title: Torque Specifications (USA/Canada models Type-R/Si) (2017 2018 2019 2020 2021)
- Source path: `pages\11014.html`
- Chunk ID: `chunk_27ba2bc9c1fc`
- Images: `images\GHH412691.png`, `images\GHH412692.png`, `images\GHH412693.jpeg`
- Duplicate sources: `pages\15598.html`

### Full Text

````text
erator pedal module | 13 N.m (1.3 kgf.m, 10 lbf.ft)

A/F sensor | 45 N.m (4.6 kgf.m, 33 lbf.ft)

ECT Sensor 1/2 | Use new O-ring | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Exhaust chamber cover | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Fuel tank*2 | Fuel tank bolts | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Support strap bolts | 38 N.m (3.9 kgf.m, 28 lbf.ft)

Knock sensor | 20 N.m (2.0 kgf.m, 15 lbf.ft)

Rocker arm oil pressure switch | Use new O-ring | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Rocker arm oil pressure sensor | Use new O-ring | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Secondary HO2S | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Throttle body bolts*2 | Use new gasket | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Catalytic converter bracket bolts*2 | Catalytic converter side | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Engine side | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Catalytic converter upper bolts | Use new gaskets and nuts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Catalytic converter upper nuts | Use new gaskets and nuts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Clutch

Location | Item | Remark | Torque

Clutch | Clutch master cylinder push rod locknut | 17 N.m (1.7 kgf.m, 13 lbf.ft)

Clutch pedal position switch locknut | 9.4 N.m (0.96 kgf.m, 6.9 lbf.ft)

Clutch pedal adjusting bolt locknut | 9.4 N.m (0.96 kgf.m, 6.9 lbf.ft)

Master cylinder nuts | 13 N.m (1.3 kgf.m, 10 lbf.ft)

Slave cylinder bolts | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Flywheel bolts*1 | L15B7: Si | 118 N.m (12.0 kgf.m, 87 lbf.ft)

K20C1: Type-R | 123 N.m (12.5 kgf.m, 91 lbf.ft)

Pressure plate bolts*1 | 26 N.m (2.7 kgf.m, 19 lbf.ft)

Release fork bolt | 29 N.m (3.0 kgf.m, 21 lbf.ft)

Manual Transmission and M/T Differential

Location | Item | Remark | Torque

Manual transmission | MTF drain plug | Use new sealing washer | 44 N.m (4.5 kgf.m, 32 lbf.ft)

MTF filler plug | L15B7: Si | Use liquid gasket on threads | 44 N.m (4.5 kgf.m, 32 lbf.ft)

K20C1: Type-R | Use new sealing washer | 44 N.m (4.5 kgf.m, 32 lbf.ft)

Back-up light switch | Use liquid gasket on threads | 29 N.m (3.0 kgf.m, 21 lbf.ft)

Transmission assembly mounting bolts (transmission side) | 64 N.m (6.5 kgf.m, 47 lbf.ft)

Transmission assembly mounting bolts (engine side) | 65 N.m (6.6 kgf.m, 48 lbf.ft)

Change wire bracket bolts*2 | L15B7: Si | 27 N.m (2.8 kgf.m, 20 lbf.ft)

Change wire bracket bolts | K20C1: Type-R | 27 N.m (2.8 kgf.m, 20 lbf.ft)

Driveline/Axle

Location | Item | Remark | Torque

Driveline/axle | Driveshaft spindle nut | L15B7: Si | Use oil on the seating surface Use new nut | 245 N.m (25.0 kgf.m, 181 lbf.ft)

- Use oil on the seating surface

- Use new nut

K20C1: Type-R | Use oil on the seating surface Use new nut | 328 N.m (33.4 kgf.m, 242 lbf.ft)

- Use oil on the seating surface

- Use new nut

Intermediate shaft dowel blots | 39 N.m (4.0 kgf.m, 29 lbf.ft)

Intermediate shaft flange bolt | 39 N.m (4.0 kgf.m, 29 lbf.ft)

Steering

Location | Item | Remark | Torque

Steering | Steering wheel bolt | Use new bolt | 49 N.m (5.0 kgf.m, 36 lbf.ft)

Steering joint bolt | 29 N.m (3.0 kgf.m, 21 lbf.ft)

Steering column bolts*1 | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Steering column nuts*1 | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Steering gearbox bolt(s)*1 | Right-front, left-rear | Use new bolts | 85 N.m (8.7 kgf.m, 63 lbf.ft)

Left-front (lower side) | Use new bolt | 105 N.m (10.7 kgf.m, 77 lbf.ft)

Right rear, left-front (upper side) | Use new bolts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Steering gearbox stiffener bolts*1 | Use new bolts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Tie-rod end ball joint nuts | Si | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Tie-rod end ball joint castle nuts | Type-R | 54-64 N.m (5.5-6.4 kgf.m, 40-47 lbf.ft)

Tie-rod end locknuts | 44 N.m (4.5 kgf.m, 32 lbf.ft)

Suspension (Si)

Location | Item | Remark | Torque

Front suspension | Wheel nuts | 108 N.m (11.0 kgf.m, 80 lbf.ft)

Knuckle damper pinch bolts | 79 N.m (8.1 kgf.m, 58 lbf.ft)

Lower arm ball joint castle nut (to knuckle) | Use new nut | 78-88 N.m (8.0-9.0 kgf.m, 58-65 lbf.ft)

Lower arm nuts (to lower ball joint)*1 | Use new nuts | 64 N.m (6.5 kgf.m, 47 lbf.ft)

Lower arm bolt (front side) | Use new bolt | 120 N.m (12.2 kgf.m, 89 lbf.ft)

Lower arm bolts (rear side) | Use new bolts | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Stabilizer bar bushing holders flange bolts*1 | Use new bolts | 75 N.m (7.6 kgf.m, 55 lbf.ft)

Stabilizer link flange nut (to damper) | Use new nut | 64 N.m (6.5 kgf.m, 47 lbf.ft)

Stabilizer link flange nut (to stabilizer bar) | Use new nut | 64 N.m (6.5 kgf.m, 47 lbf.ft)
````

## Chunk 8533: Torque Specifications (USA/Canada models Type-R/Si) (2017 2018 2019 2020 2021)

- Title: Torque Specifications (USA/Canada models Type-R/Si) (2017 2018 2019 2020 2021)
- Source path: `pages\11014.html`
- Chunk ID: `chunk_fca6c1c2259f`
- Images: `images\GHH412691.png`, `images\GHH412692.png`, `images\GHH412693.jpeg`
- Duplicate sources: `pages\15598.html`

### Full Text

````text
ft)

Suspension (Si)

Location | Item | Remark | Torque

Front suspension | Wheel nuts | 108 N.m (11.0 kgf.m, 80 lbf.ft)

Knuckle damper pinch bolts | 79 N.m (8.1 kgf.m, 58 lbf.ft)

Lower arm ball joint castle nut (to knuckle) | Use new nut | 78-88 N.m (8.0-9.0 kgf.m, 58-65 lbf.ft)

Lower arm nuts (to lower ball joint)*1 | Use new nuts | 64 N.m (6.5 kgf.m, 47 lbf.ft)

Lower arm bolt (front side) | Use new bolt | 120 N.m (12.2 kgf.m, 89 lbf.ft)

Lower arm bolts (rear side) | Use new bolts | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Stabilizer bar bushing holders flange bolts*1 | Use new bolts | 75 N.m (7.6 kgf.m, 55 lbf.ft)

Stabilizer link flange nut (to damper) | Use new nut | 64 N.m (6.5 kgf.m, 47 lbf.ft)

Stabilizer link flange nut (to stabilizer bar) | Use new nut | 64 N.m (6.5 kgf.m, 47 lbf.ft)

Damper nuts (to body) | Use new nuts | 75 N.m (7.6 kgf.m, 55 lbf.ft)

Damper self-locking nut | Use new nut | 65 N.m (6.6 kgf.m, 48 lbf.ft)

Rear suspension | Wheel nuts | 108 N.m (11.0 kgf.m, 80 lbf.ft)

Upper arm bolt (to subframe) | Use new bolt | 76 N.m (7.7 kgf.m, 56 lbf.ft)

Upper arm bolt/nut (to knuckle) | Use new bolt/nut | 76 N.m (7.7 kgf.m, 56 lbf.ft)

Lower arm A bolt/nut (to knuckle) | Use new bolt/nut | 76 N.m (7.7 kgf.m, 56 lbf.ft)

Lower arm A bolt (to subframe) | Use new bolt | 76 N.m (7.7 kgf.m, 56 lbf.ft)

Lower arm B bolt (to knuckle) | Use new bolt | 69 N.m (7.0 kgf.m, 51 lbf.ft)

Lower arm B bolt/nut (to subframe) | Use new bolt/nut | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Trailing arm bolts/nuts (to knuckle) | Use new bolts/nuts | 118 N.m (12.0 kgf.m, 87 lbf.ft)

Trailing arm bolts (to body) | Use new bolts | 118 N.m (12.0 kgf.m, 87 lbf.ft)

Stabilizer bar bushing holders flange bolts | Use new bolts | 37 N.m (3.8 kgf.m, 27 lbf.ft)

Stabilizer link flange nut (to stabilizer bar) | Use new nut | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Stabilizer link (to lower arm B) | Use new bolt | 40 N.m (4.1 kgf.m, 30 lbf.ft)

Damper bolt (to knuckle) | Use new bolt | 81 N.m (8.3 kgf.m, 60 lbf.ft)

Damper bolts (to body) | Use new bolts | 40 N.m (4.1 kgf.m, 30 lbf.ft)

Damper self-locking nut | Use new nut | 30 N.m (3.1 kgf.m, 22 lbf.ft)

Suspension (Type-R)

Location | Item | Remark | Torque

Front suspension | Wheel nuts | 127 N.m (13.0 kgf.m, 94 lbf.ft)

Damper fork bolts*1 | Use new bolt | 64 N.m (6.5 kgf.m, 47 lbf.ft)

Housing bracket ball joint castle nut | Use new nut | 103-113 N.m (10.5-11.5 kgf.m, 76-83 lbf.ft)

Housing bracket bolt (to damper fork upper)*1 | Use new bolt | 122 N.m (12.4 kgf.m, 90 lbf.ft)

Housing bracket bolt (to damper fork lower)*1 | Use new bolt | 59 N.m (6.0 kgf.m, 44 lbf.ft)

Housing bracket TORX bolt (to knuckle)*1 | Use new bolt | 83 N.m (8.5 kgf.m, 61 lbf.ft)

Lower arm bolt (front side) | Use new bolt | 172 N.m (17.5 kgf.m, 127 lbf.ft)

Lower arm bolts (rear side) | Use new bolt | 105 N.m (10.7 kgf.m, 77 lbf.ft)

Stabilizer bar bushing holders flange bolts*1 | Use new bolts | 75 N.m (7.6 kgf.m, 55 lbf.ft)

Stabilizer link flange nut (to damper) | Use new nut | 64 N.m (6.5 kgf.m, 47 lbf.ft)

Stabilizer link flange nut (to stabilizer bar) | Use new nut | 35 N.m (3.6 kgf.m, 26 lbf.ft)

Stopper link flange nuts | Use new nuts | 70 N.m (7.1 kgf.m, 52 lbf.ft)

Damper nuts (to body) | Use new nuts | 63 N.m (6.4 kgf.m, 46 lbf.ft)

Damper self-locking nut | Use new nut | 59 N.m (6.0 kgf.m, 44 lbf.ft)

Location | Item | Remark | Torque

Rear suspension | Wheel nuts | 127 N.m (13.0 kgf.m, 94 lbf.ft)

Upper arm bolt (to subframe) | Use new bolt | 76 N.m (7.7 kgf.m, 56 lbf.ft)

Upper arm bolt/nut (to knuckle) | Use new bolt/nut | 76 N.m (7.7 kgf.m, 56 lbf.ft)

Lower arm A bolt/nut (to knuckle) | Use new bolt/nut | 81 N.m (8.3 kgf.m, 60 lbf.ft)

Lower arm A bolt (to subframe) | Use new bolt | 76 N.m (7.7 kgf.m, 56 lbf.ft)

Lower arm B bolt (to knuckle) | Use new bolt | 69 N.m (7.0 kgf.m, 51 lbf.ft)

Lower arm B bolt/nut (to subframe) | Use new bolt/nut | 115 N.m (11.7 kgf.m, 85 lbf.ft)

Trailing arm bolts/nuts (to knuckle) | Use new bolts/nuts | 118 N.m (12.0 kgf.m, 87 lbf.ft)

Trailing arm bolts (to body) | Use new bolts | 157 N.m (16.0 kgf.m, 116 lbf.ft)

Stabilizer bar bushing holders flange bolts | Use new bolts | 37 N.m (3.8 kgf.m, 27 lbf.ft)

Stabilizer link flange nut (to stabilizer bar) | Use new nut | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Stabilizer link (to lower arm B) | Use new bolt | 40 N.m (4.1 kgf.m, 30 lbf.ft)

Damper bolt (to knuckle) | Use new bolt | 87 N.m (8.9 kgf.m, 30 lbf.ft)
````

## Chunk 8534: Torque Specifications (USA/Canada models Type-R/Si) (2017 2018 2019 2020 2021)

- Title: Torque Specifications (USA/Canada models Type-R/Si) (2017 2018 2019 2020 2021)
- Source path: `pages\11014.html`
- Chunk ID: `chunk_1e8ad21a0dff`
- Images: `images\GHH412691.png`, `images\GHH412692.png`, `images\GHH412693.jpeg`
- Duplicate sources: `pages\15598.html`

### Full Text

````text
lt/nut | 81 N.m (8.3 kgf.m, 60 lbf.ft)

Lower arm A bolt (to subframe) | Use new bolt | 76 N.m (7.7 kgf.m, 56 lbf.ft)

Lower arm B bolt (to knuckle) | Use new bolt | 69 N.m (7.0 kgf.m, 51 lbf.ft)

Lower arm B bolt/nut (to subframe) | Use new bolt/nut | 115 N.m (11.7 kgf.m, 85 lbf.ft)

Trailing arm bolts/nuts (to knuckle) | Use new bolts/nuts | 118 N.m (12.0 kgf.m, 87 lbf.ft)

Trailing arm bolts (to body) | Use new bolts | 157 N.m (16.0 kgf.m, 116 lbf.ft)

Stabilizer bar bushing holders flange bolts | Use new bolts | 37 N.m (3.8 kgf.m, 27 lbf.ft)

Stabilizer link flange nut (to stabilizer bar) | Use new nut | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Stabilizer link (to lower arm B) | Use new bolt | 40 N.m (4.1 kgf.m, 30 lbf.ft)

Damper bolt (to knuckle) | Use new bolt | 87 N.m (8.9 kgf.m, 30 lbf.ft)

Damper bolts (to body) | Use new bolts | 40 N.m (4.1 kgf.m, 30 lbf.ft)

Damper self-locking nut | Use new nut | 32 N.m (3.3 kgf.m, 24 lbf.ft)

Brakes

Location | Item | Remark | Torque

Conventional brake | Front brake caliper bracket bolts | Si | 108 N.m (11.0 kgf.m, 80 lbf.ft)

Type-R | 140 N.m (14.3 kgf.m, 103 lbf.ft)

Front brake caliper bolts | Si | 50 N.m (5.1 kgf.m, 37 lbf.ft)

Front brake hose banjo bolt | Si | Use new washers | 35 N.m (3.6 kgf.m, 26 lbf.ft)

Rear brake caliper bracket bolts | 108 N.m (11.0 kgf.m, 80 lbf.ft)

Rear brake caliper pin bolts | 25 N.m (2.5 kgf.m, 18 lbf.ft)

Rear brake hose banjo bolt | Use new washers | 35 N.m (3.6 kgf.m, 26 lbf.ft)

Master cylinder nuts (to brake booster) | Si | 15 N.m (1.5 kgf.m, 11 lbf.ft)

Type-R | 13 N.m (1.3 kgf.m, 10 lbf.ft)

Master cylinder brake line | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Brake booster/brake pedal nuts | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Brake pedal support member bolts/nuts | 22 N.m (2.2 kgf.m, 16 lbf.ft)

VSA | VSA modulator-control unit brake line (10 mm) | 15 N.m (1.5 kgf.m, 11 lbf.ft)

VSA modulator-control unit brake line (12 mm) | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Body

Location | Item | Remark | Torque

Frame | Front subframe bolts | Use new bolts | 103 N.m (10.5 kgf.m, 76 lbf.ft)

Front subframe rear stay bolts | Use new bolts | 91 N.m (9.3 kgf.m, 67 lbf.ft)

Rear subframe bolts | Si | Use new bolts | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Type-R | Use new bolts | 64 N.m (6.5 kgf.m, 47 lbf.ft)

Front brace bolts (10 mm) | Use new bolts | 58 N.m (5.9 kgf.m, 43 lbf.ft)

Front brace bolts (12 mm) | Use new bolts | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Heating, Ventilation, and Air Conditioning

Location | Item | Remark | Torque

A/C compressor | A/C compressor bolts | 22 N.m (2.2 kgf.m, 16 lbf.ft)

A/C compressor center bolt | Use new bolt | 17 N.m (1.7 kgf.m, 13 lbf.ft)

A/C compressor relief valve | Use new O-ring | 8.5 N.m (0.87 kgf.m, 6.3 lbf.ft)

Discharge hose | A/C pressure sensor | Use new O-ring | 11 N.m (1.1 kgf.m, 8 lbf.ft)

Body Electrical

Location | Item | Remark | Torque

Wipers/washers | Windshield wiper arm nut | 29 N.m (3.0 kgf.m, 21 lbf.ft)

Windshield wiper link nut | 31 N.m (3.2 kgf.m, 23 lbf.ft)

Rear wiper arm nut | 9.4 N.m (0.96 kgf.m, 6.9 lbf.ft)
````

## Chunk 8535: Torque Specifications (USA/Canada models except Type-R/Si) (2018 2019 2020 2021)

- Title: Torque Specifications (USA/Canada models except Type-R/Si) (2018 2019 2020 2021)
- Source path: `pages\11015.html`
- Chunk ID: `chunk_a2a2cf9269cd`
- Images: `images\GHH412694.png`, `images\GHH412695.png`, `images\GHH412696.jpeg`
- Duplicate sources: `pages\15599.html`

### Full Text

````text
# Torque Specifications (USA/Canada models except Type-R/Si) (2018 2019 2020 2021)

NOTE:

- Refer to the appropriate portion of the service information for the precautions and complete procedures.

- Refer to the appropriate portion of the service information for the bolts/nuts not indicated here.

- 1: Parts to be tightened in a particular order. 2: Follow the appropriate service information procedures closely for torque, sequence, and special steps.

- 1: Parts to be tightened in a particular order.

- 2: Follow the appropriate service information procedures closely for torque, sequence, and special steps.

- When using some special tools or crowfoot-type wrenches, the torque value changes due to the added leverage. The actual torque applied will be greater than the torque reading shown.

- The torque specification given is the actual torque, not the reading on the torque wrench. To compensate for this additional leverage, use the formula below to calculate the torque value reading on the torque wrench. Always use the special tool or crowfoot-type wrench in a straight line with the torque wrench, or you will apply improper torque.

- The torque specification given is the actual torque, not the reading on the torque wrench.

- To compensate for this additional leverage, use the formula below to calculate the torque value reading on the torque wrench.

- Always use the special tool or crowfoot-type wrench in a straight line with the torque wrench, or you will apply improper torque.

Courtesy of HONDA, U.S.A., INC.

Engine Electrical (1.5L)

Location | Item | Remark | Torque

Starting system | Starter bolt (10 mm) | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Starter bolt (12 mm) | 65 N.m (6.6 kgf.m, 48 lbf.ft)

Positive starter cable nut | 9.0 N.m (0.92 kgf.m, 6.6 lbf.ft)

Ignition system | Spark plugs | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Charging system | Alternator bolts | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Positive alternator cable nut | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Drive belt auto-tensioner bolt (8 mm) | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Drive belt auto-tensioner bolt (10 mm) | 55 N.m (5.6 kgf.m, 41 lbf.ft)

Engine Electrical (2.0L)

Location | Item | Remark | Torque

Starting system | Starter bolts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Positive starter cable nut | 9.0 N.m (0.92 kgf.m, 6.6 lbf.ft)

Ignition system | Spark plugs | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Charging system | Alternator bolts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Positive alternator cable nut | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Drive belt auto-tensioner bolt (8 mm) | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Drive belt auto-tensioner bolt (10 mm) | 55 N.m (5.6 kgf.m, 41 lbf.ft)

Engine Mechanical (1.5L)

Location | Item | Remark | Torque

Engine assembly | Side engine mount bolts (12 mm) | Use new bolts | 49 N.m (5.0 kgf.m, 36 lbf.ft)

Side engine mount bolts (14 mm) | Use new bolts | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Side engine mount nut | Use new nut | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Side engine mount bracket bolts | Use new bolts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Torque rod bolts *2 | Use new bolts | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Torque rod bracket bolts | Use new bolts | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Transmission mount bolts | Use new bolts | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Transmission mount bracket bolt(s) | L15B7 | Use new bolt(s) | 78 N.m (8.0 kgf.m, 58 lbf.ft)

L15BA/L15BY | Use new bolt(s) | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Transmission mount bracket nuts | L15B7 | Use new nuts | 78 N.m (8.0 kgf.m, 58 lbf.ft)

L15BA/L15BY | Use new nuts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Engine lubrication | Oil pressure switch | Apply liquid gasket on threads | 18 N.m (1.8 kgf.m, 13 lbf.ft)

Oil pan drain bolt | Use new washer | 40 N.m (4.1 kgf.m, 30 lbf.ft)

Oil filter | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Intake manifold and exhaust system | Intake manifold bolts *1 | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Intake manifold nuts *1 | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Exhaust pipe A self-locking nuts | TWC side | Use new gasket and nuts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Muffler R self-locking nuts (dual muffler) | Exhaust pipe A side | Use new gasket and nuts | 33 N.m (3.4 kgf.m, 24 lbf.ft)

Muffler L side | Use new gasket and nuts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Muffler self-locking nuts (center muffler) | Use new gasket and nuts | 33 N.m (3.4 kgf.m, 24 lbf.ft)

Turbocharger self-locking nuts*2 | Use new gasket and nuts | 45 N.m (4.6 kgf.m, 33 lbf.ft)
````

## Chunk 8536: Torque Specifications (USA/Canada models except Type-R/Si) (2018 2019 2020 2021)

- Title: Torque Specifications (USA/Canada models except Type-R/Si) (2018 2019 2020 2021)
- Source path: `pages\11015.html`
- Chunk ID: `chunk_0243ab1e09cc`
- Images: `images\GHH412694.png`, `images\GHH412695.png`, `images\GHH412696.jpeg`
- Duplicate sources: `pages\15599.html`

### Full Text

````text
threads | 18 N.m (1.8 kgf.m, 13 lbf.ft)

Oil pan drain bolt | Use new washer | 40 N.m (4.1 kgf.m, 30 lbf.ft)

Oil filter | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Intake manifold and exhaust system | Intake manifold bolts *1 | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Intake manifold nuts *1 | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Exhaust pipe A self-locking nuts | TWC side | Use new gasket and nuts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Muffler R self-locking nuts (dual muffler) | Exhaust pipe A side | Use new gasket and nuts | 33 N.m (3.4 kgf.m, 24 lbf.ft)

Muffler L side | Use new gasket and nuts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Muffler self-locking nuts (center muffler) | Use new gasket and nuts | 33 N.m (3.4 kgf.m, 24 lbf.ft)

Turbocharger self-locking nuts*2 | Use new gasket and nuts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Turbocharger bolts*2 | Use new gasket | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Engine Mechanical (2.0L)

Location | Item | Remark | Torque

Engine assembly | Side engine mount bolts (12 mm) | Use new bolts | 49 N.m (5.0 kgf.m, 36 lbf.ft)

Side engine mount bolts (14 mm) | Use new bolts | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Side engine mount nut | Use new nut | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Side engine mount bracket bolts | Use new bolts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Torque rod bolts *2 | Use new bolts | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Torque rod bracket bolts | Use new bolts | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Transmission mount bolts | Use new bolts | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Transmission mount bracket bolt(s) | Use new bolt(s) | 78 N.m (8.0 kgf.m, 58 lbf.ft)

Transmission mount bracket nuts | Use new nuts | 78 N.m (8.0 kgf.m, 58 lbf.ft)

Engine lubrication | Oil pressure switch | Apply liquid gasket on threads | 17 N.m (1.7 kgf.m, 13 lbf.ft)

Oil pan drain bolt | Use new washer | 40 N.m (4.1 kgf.m, 30 lbf.ft)

Oil filter | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Intake manifold and exhaust system | Intake manifold bolts *1 | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Intake manifold nuts *1 | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Muffler self-locking nuts *1 | Use new gasket and nuts | 33 N.m (3.4 kgf.m, 24 lbf.ft)

Exhaust pipe A self-locking nuts | Use new gasket and nuts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Engine Cooling (1.5L)

Location | Item | Remark | Torque

Cooling system | Water passage bolts | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Water passage nuts | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Thermostat housing bolts | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Thermostat housing nuts | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Engine Cooling (2.0L)

Location | Item | Remark | Torque

Cooling system | Water passage bolts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Water passage nuts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Thermostat housing bolts | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Thermostat housing nuts | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Fuel Emissions (1.5L)

Location | Item | Remark | Torque

Fuel and emissions | Accelerator pedal module | 13 N.m (1.3 kgf.m, 10 lbf.ft)

A/F sensor | 45 N.m (4.6 kgf.m, 33 lbf.ft)

ECT Sensor 1/2 | Use new O-ring | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Exhaust chamber cover | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Fuel tank*2 | Fuel tank bolts (L15B7) | 23 N.m (2.3 kgf.m, 17 lbf.ft)

Fuel tank bolts (L15BA/L15BY) | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Support strap bolts | 38 N.m (3.9 kgf.m, 28 lbf.ft)

Knock sensor | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Secondary HO2S | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Throttle body bolts*2 | Use new gasket | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Catalytic converter bracket bolts*2 | Catalytic converter side | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Engine side | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Catalytic converter upper bolts | Use new gaskets and nuts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Catalytic converter upper nuts | Use new gaskets and nuts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Fuel Emissions (2.0L)

Location | Item | Remark | Torque

Fuel and emissions | Accelerator pedal module | 13 N.m (1.3 kgf.m, 10 lbf.ft)

A/F sensor | 45 N.m (4.6 kgf.m, 33 lbf.ft)

ECT Sensor 1/2 | Use new O-ring | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Exhaust chamber cover | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Fuel tank*2 | Fuel tank bolts | 23 N.m (2.3 kgf.m, 17 lbf.ft)

Support strap bolts | 38 N.m (3.9 kgf.m, 28 lbf.ft)

Knock sensor | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Rocker arm oil pressure switch | Use new O-ring | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Secondary HO2S | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Throttle body bolts*2 | Use new gasket | 22 N.m (2.2 kgf.m, 16 lbf.ft)
````

## Chunk 8537: Torque Specifications (USA/Canada models except Type-R/Si) (2018 2019 2020 2021)

- Title: Torque Specifications (USA/Canada models except Type-R/Si) (2018 2019 2020 2021)
- Source path: `pages\11015.html`
- Chunk ID: `chunk_14dd4a7f8455`
- Images: `images\GHH412694.png`, `images\GHH412695.png`, `images\GHH412696.jpeg`
- Duplicate sources: `pages\15599.html`

### Full Text

````text
kets and nuts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Catalytic converter upper nuts | Use new gaskets and nuts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Fuel Emissions (2.0L)

Location | Item | Remark | Torque

Fuel and emissions | Accelerator pedal module | 13 N.m (1.3 kgf.m, 10 lbf.ft)

A/F sensor | 45 N.m (4.6 kgf.m, 33 lbf.ft)

ECT Sensor 1/2 | Use new O-ring | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Exhaust chamber cover | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Fuel tank*2 | Fuel tank bolts | 23 N.m (2.3 kgf.m, 17 lbf.ft)

Support strap bolts | 38 N.m (3.9 kgf.m, 28 lbf.ft)

Knock sensor | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Rocker arm oil pressure switch | Use new O-ring | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Secondary HO2S | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Throttle body bolts*2 | Use new gasket | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Catalytic converter bracket bolts*2 | Catalytic converter side | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Engine side | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Catalytic converter upper bolts | Use new gaskets and nuts | 32 N.m (3.3 kgf.m, 24 lbf.ft)

Catalytic converter upper nuts | Use new gaskets and nuts | 32 N.m (3.3 kgf.m, 24 lbf.ft)

Clutch

Location | Item | Remark | Torque

Clutch | Clutch master cylinder push rod locknut | 17 N.m (1.7 kgf.m, 13 lbf.ft)

Clutch pedal position switch locknut | 9.4 N.m (0.96 kgf.m, 6.9 lbf.ft)

Clutch pedal adjusting bolt locknut | 9.4 N.m (0.96 kgf.m, 6.9 lbf.ft)

Master cylinder nuts | 13 N.m (1.3 kgf.m, 10 lbf.ft)

Slave cylinder bolts | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Flywheel bolts*1 | 1.5L engine | 118 N.m (12.0 kgf.m, 87 lbf.ft)

2.0L engine | 123 N.m (12.5 kgf.m, 91 lbf.ft)

Pressure plate bolts*1 | 26 N.m (2.7 kgf.m, 19 lbf.ft)

Release fork bolt | 29 N.m (3.0 kgf.m, 21 lbf.ft)

Manual Transmission and M/T Differential

Location | Item | Remark | Torque

Manual transmission | MTF drain plug | Use new sealing washer | 44 N.m (4.5 kgf.m, 32 lbf.ft)

MTF filler plug | Use liquid gasket on threads | 44 N.m (4.5 kgf.m, 32 lbf.ft)

Back-up light switch | Use liquid gasket on threads | 29 N.m (3.0 kgf.m, 21 lbf.ft)

Transmission assembly mounting bolts (transmission side) | 64 N.m (6.5 kgf.m, 47 lbf.ft)

Transmission assembly mounting bolts (engine side) | 65 N.m (6.6 kgf.m, 48 lbf.ft)

Change wire bracket bolts*2 | 27 N.m (2.8 kgf.m, 20 lbf.ft)

CVT and CVT Differential (1.5L)

Location | Item | Remark | Torque

CVT | Transmission fluid check bolt | Use new sealing washer | 20 N.m (2.0 kgf.m, 15 lbf.ft)

Transmission fluid drain plug | Use new sealing washer | 49 N.m (5.0 kgf.m, 36 lbf.ft)

Pressure inspection port sealing bolts (drive pulley, forward clutch, reverse brake) | Use new sealing washer | 20 N.m (2.0 kgf.m, 15 lbf.ft)

Drive plate bolts*2 | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Transmission assembly mounting bolts (transmission side) | 64 N.m (6.5 kgf.m, 47 lbf.ft)

Transmission assembly mounting bolts (engine side) | 65 N.m (6.6 kgf.m, 48 lbf.ft)

Transmission hanger bolt | 44 N.m (4.5 kgf.m, 32 lbf.ft)

CVTF warmer bolts | 27 N.m (2.8 kgf.m, 20 lbf.ft)

Shift cable bracket bolts | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Shift cable end nut | 22 N.m (2.2 kgf.m, 16 lbf.ft)

CVT driven pulley pressure sensor | Use new sealing washer | 20 N.m (2.0 kgf.m, 15 lbf.ft)

CVT and CVT Differential (2.0L)

Location | Item | Remark | Torque

CVT | Transmission fluid filler plug | Use new sealing washer | 44 N.m (4.5 kgf.m, 32 lbf.ft)

Transmission fluid drain plug | Use new sealing washer | 49 N.m (5.0 kgf.m, 36 lbf.ft)

Pressure inspection port sealing bolts (drive pulley, driven pulley, forward clutch) | Use new sealing washer | 18 N.m (1.8 kgf.m, 13 lbf.ft)

Pressure inspection port sealing bolt (reverse brake) | Use new bolt | 20 N.m (2.0 kgf.m, 15 lbf.ft)

Drive plate bolts*2 | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Transmission assembly mounting bolts (transmission side) | 64 N.m (6.5 kgf.m, 47 lbf.ft)

Transmission assembly mounting bolts (engine side) | 65 N.m (6.6 kgf.m, 48 lbf.ft)

Transmission hanger bolt | 44 N.m (4.5 kgf.m, 32 lbf.ft)

CVTF warmer bolts | 27 N.m (2.8 kgf.m, 20 lbf.ft)

Shift cable bracket bolts | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Shift cable end nut | 22 N.m (2.2 kgf.m, 16 lbf.ft)

CVT driven pulley pressure sensor | Use new sealing washer | 20 N.m (2.0 kgf.m, 15 lbf.ft)

Driveline/Axle

Location | Item | Remark | Torque

Driveline/axle | Driveshaft spindle nut (1.5L) | Use oil on the seating surface Use new nut | 245 N.m (25.0 kgf.m, 181 lbf.ft)

- Use oil on the seating surface

- Use new nut
````

## Chunk 8538: Torque Specifications (USA/Canada models except Type-R/Si) (2018 2019 2020 2021)

- Title: Torque Specifications (USA/Canada models except Type-R/Si) (2018 2019 2020 2021)
- Source path: `pages\11015.html`
- Chunk ID: `chunk_b14e6acb509c`
- Images: `images\GHH412694.png`, `images\GHH412695.png`, `images\GHH412696.jpeg`
- Duplicate sources: `pages\15599.html`

### Full Text

````text
| 20 N.m (2.0 kgf.m, 15 lbf.ft)

Drive plate bolts*2 | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Transmission assembly mounting bolts (transmission side) | 64 N.m (6.5 kgf.m, 47 lbf.ft)

Transmission assembly mounting bolts (engine side) | 65 N.m (6.6 kgf.m, 48 lbf.ft)

Transmission hanger bolt | 44 N.m (4.5 kgf.m, 32 lbf.ft)

CVTF warmer bolts | 27 N.m (2.8 kgf.m, 20 lbf.ft)

Shift cable bracket bolts | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Shift cable end nut | 22 N.m (2.2 kgf.m, 16 lbf.ft)

CVT driven pulley pressure sensor | Use new sealing washer | 20 N.m (2.0 kgf.m, 15 lbf.ft)

Driveline/Axle

Location | Item | Remark | Torque

Driveline/axle | Driveshaft spindle nut (1.5L) | Use oil on the seating surface Use new nut | 245 N.m (25.0 kgf.m, 181 lbf.ft)

- Use oil on the seating surface

- Use new nut

Driveshaft spindle nut (2.0L) | Use oil on the seating surface Use new nut | 181 N.m (18.5 kgf.m, 133 lbf.ft)

- Use oil on the seating surface

- Use new nut

Intermediate shaft dowel blots | 39 N.m (4.0 kgf.m, 29 lbf.ft)

Intermediate shaft flange bolt | 39 N.m (4.0 kgf.m, 29 lbf.ft)

Steering

Location | Item | Remark | Torque

Steering | Steering wheel bolt | Use new bolt | 49 N.m (5.0 kgf.m, 36 lbf.ft)

Steering joint bolt | 29 N.m (3.0 kgf.m, 21 lbf.ft)

Steering column bolts*1 | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Steering column nuts*1 | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Steering gearbox bolt(s)*1 | Right-front, left-rear | Use new bolts | 85 N.m (8.7 kgf.m, 63 lbf.ft)

Left-front (lower side) | Use new bolt | 105 N.m (10.7 kgf.m, 77 lbf.ft)

Right-rear, left-front (upper side) | Use new bolts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Steering gearbox stiffener bolts*1 | Use new bolts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Tie-rod end ball joint nuts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Tie-rod end locknuts | 44 N.m (4.5 kgf.m, 32 lbf.ft)

Suspension

Location | Item | Remark | Torque

Front suspension | Wheel nuts | 108 N.m (11.0 kgf.m, 80 lbf.ft)

Knuckle damper pinch bolts | 79 N.m (8.1 kgf.m, 58 lbf.ft)

Lower arm ball joint castle nut (to knuckle) | Use new nut | 78-88 N.m (8.0-9.0 kgf.m, 58-65 lbf.ft)

Lower arm nuts (to lower ball joint)*1 | Use new nuts | 64 N.m (6.5 kgf.m, 47 lbf.ft)

Lower arm bolt (front side) | Use new bolt | 120 N.m (12.2 kgf.m, 89 lbf.ft)

Lower arm bolts (rear side) | Use new bolts | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Stabilizer bar bushing holders flange bolts*1 | Use new bolts | 75 N.m (7.6 kgf.m, 55 lbf.ft)

Stabilizer link flange nut (to damper) | Use new nut | 64 N.m (6.5 kgf.m, 47 lbf.ft)

Stabilizer link flange nut (to stabilizer bar) | 2/4-door | Use new nut | 64 N.m (6.5 kgf.m, 47 lbf.ft)

5-door | Use new nut | 35 N.m (3.6 kgf.m, 26 lbf.ft)

Damper nuts (to body) | 2/4-door | Use new nuts | 75 N.m (7.6 kgf.m, 55 lbf.ft)

5-door | Use new nuts | 63 N.m (6.4 kgf.m, 46 lbf.ft)

Damper self-locking nut | 2/4-door (screw guide pin type) | Use new nut | 54 N.m (5.5 kgf.m, 40 lbf.ft)

2/4-door (hex guide pin type) | Use new nut | 75 N.m (7.6 kgf.m, 55 lbf.ft)

5-door | Use new nut | 68 N.m (6.9 kgf.m, 50 lbf.ft)

Rear suspension | Wheel nuts | 108 N.m (11.0 kgf.m, 80 lbf.ft)

Upper arm bolt (to subframe) | Use new bolt | 76 N.m (7.7 kgf.m, 56 lbf.ft)

Upper arm bolt/nut (to knuckle) | Use new bolt/nut | 76 N.m (7.7 kgf.m, 56 lbf.ft)

Lower arm A bolt/nut (to knuckle) | Use new bolt/nut | 76 N.m (7.7 kgf.m, 56 lbf.ft)

Lower arm A bolt (to subframe) | Use new bolt | 76 N.m (7.7 kgf.m, 56 lbf.ft)

Lower arm B bolt (to knuckle) | Use new bolt | 69 N.m (7.0 kgf.m, 51 lbf.ft)

Lower arm B bolt/nut (to subframe) | Use new bolt/nut | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Trailing arm bolts/nuts (to knuckle) | Use new bolts/nuts | 118 N.m (12.0 kgf.m, 87 lbf.ft)

Trailing arm bolts (to body) | Use new bolts | 118 N.m (12.0 kgf.m, 87 lbf.ft)

Stabilizer bar bushing holders flange bolts | Use new bolts | 37 N.m (3.8 kgf.m, 27 lbf.ft)

Stabilizer link flange nut (to stabilizer bar) | Use new nut | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Stabilizer link (to lower arm B) | Use new bolt | 40 N.m (4.1 kgf.m, 30 lbf.ft)

Damper bolt (to knuckle) | Use new bolt | 81 N.m (8.3 kgf.m, 60 lbf.ft)

Damper bolts (to body) | Use new bolts | 40 N.m (4.1 kgf.m, 30 lbf.ft)

Damper self-locking nut | Use new nut | 30 N.m (3.1 kgf.m, 22 lbf.ft)

Brakes

Location | Item | Remark | Torque

Conventional brake | Front brake caliper bracket bolts | 108 N.m (11.0 kgf.m, 80 lbf.ft)

Front brake caliper bolts | 34 N.m (3.5 kgf.m, 25 lbf.ft)
````

## Chunk 8539: Torque Specifications (USA/Canada models except Type-R/Si) (2018 2019 2020 2021)

- Title: Torque Specifications (USA/Canada models except Type-R/Si) (2018 2019 2020 2021)
- Source path: `pages\11015.html`
- Chunk ID: `chunk_0094e2308078`
- Images: `images\GHH412694.png`, `images\GHH412695.png`, `images\GHH412696.jpeg`
- Duplicate sources: `pages\15599.html`

### Full Text

````text
olts/nuts | 118 N.m (12.0 kgf.m, 87 lbf.ft)

Trailing arm bolts (to body) | Use new bolts | 118 N.m (12.0 kgf.m, 87 lbf.ft)

Stabilizer bar bushing holders flange bolts | Use new bolts | 37 N.m (3.8 kgf.m, 27 lbf.ft)

Stabilizer link flange nut (to stabilizer bar) | Use new nut | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Stabilizer link (to lower arm B) | Use new bolt | 40 N.m (4.1 kgf.m, 30 lbf.ft)

Damper bolt (to knuckle) | Use new bolt | 81 N.m (8.3 kgf.m, 60 lbf.ft)

Damper bolts (to body) | Use new bolts | 40 N.m (4.1 kgf.m, 30 lbf.ft)

Damper self-locking nut | Use new nut | 30 N.m (3.1 kgf.m, 22 lbf.ft)

Brakes

Location | Item | Remark | Torque

Conventional brake | Front brake caliper bracket bolts | 108 N.m (11.0 kgf.m, 80 lbf.ft)

Front brake caliper bolts | 34 N.m (3.5 kgf.m, 25 lbf.ft)

Front brake hose banjo bolt | Use new washers | 35 N.m (3.6 kgf.m, 26 lbf.ft)

Rear brake caliper bracket bolts | 108 N.m (11.0 kgf.m, 80 lbf.ft)

Rear brake caliper pin bolts | 25 N.m (2.5 kgf.m, 18 lbf.ft)

Rear brake hose banjo bolt | Use new washers | 35 N.m (3.6 kgf.m, 26 lbf.ft)

Master cylinder nuts (to brake booster) | 15 N.m (1.5 kgf.m, 11 lbf.ft)

Master cylinder brake line | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Brake booster/brake pedal nuts | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Brake pedal support member bolts/nuts | 22 N.m (2.2 kgf.m, 16 lbf.ft)

VSA | VSA modulator-control unit brake line (10 mm) | 15 N.m (1.5 kgf.m, 11 lbf.ft)

VSA modulator-control unit brake line (12 mm) | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Body

Location | Item | Remark | Torque

Frame | Front subframe bolts | Use new bolts | 103 N.m (10.5 kgf.m, 76 lbf.ft)

Front subframe rear stay bolts | Use new bolts | 91 N.m (9.3 kgf.m, 67 lbf.ft)

Rear subframe bolts | Use new bolts | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Front brace bolts (10 mm) | Use new bolts | 58 N.m (5.9 kgf.m, 43 lbf.ft)

Front brace bolts (12 mm) | Use new bolts | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Heating, Ventilation, and Air Conditioning

Location | Item | Remark | Torque

A/C compressor | A/C compressor bolts | 22 N.m (2.2 kgf.m, 16 lbf.ft)

A/C compressor center bolt | Use new bolt | 17 N.m (1.7 kgf.m, 13 lbf.ft)

A/C compressor relief valve | Use new O-ring | 8.5 N.m (0.87 kgf.m, 6.3 lbf.ft)

Discharge hose | A/C pressure sensor | Use new O-ring | 11 N.m (1.1 kgf.m, 8 lbf.ft)

Body Electrical

Location | Item | Remark | Torque

Wipers/washers | Windshield wiper arm nut | 29 N.m (3.0 kgf.m, 21 lbf.ft)

Windshield wiper link nut | 31 N.m (3.2 kgf.m, 23 lbf.ft)

Rear wiper arm nut | 9.4 N.m (0.96 kgf.m, 6.9 lbf.ft)
````

## Chunk 8540: Torque Specifications (USA/Canada models) (2016)

- Title: Torque Specifications (USA/Canada models) (2016)
- Source path: `pages\11016.html`
- Chunk ID: `chunk_44a5ff073855`
- Images: `images\GHH412697.png`, `images\GHH412698.png`, `images\GHH412699.jpeg`
- Duplicate sources: `pages\15592.html`

### Full Text

````text
# Torque Specifications (USA/Canada models) (2016)

NOTE:

- Refer to the appropriate portion of the service information for the precautions and complete procedures.

- Refer to the appropriate portion of the service information for the bolts/nuts not indicated here.

- 1: Parts to be tightened in a particular order. 2: Follow the appropriate service information procedures closely for torque, sequence, and special steps.

- 1: Parts to be tightened in a particular order.

- 2: Follow the appropriate service information procedures closely for torque, sequence, and special steps.

- When using some special tools or crowfoot-type wrenches, the torque value changes due to the added leverage. The actual torque applied will be greater than the torque reading shown.

- The torque specification given is the actual torque, not the reading on the torque wrench. To compensate for this additional leverage, use the formula below to calculate the torque value reading on the torque wrench. Always use the special tool or crowfoot-type wrench in a straight line with the torque wrench, or you will apply improper torque.

- The torque specification given is the actual torque, not the reading on the torque wrench.

- To compensate for this additional leverage, use the formula below to calculate the torque value reading on the torque wrench.

- Always use the special tool or crowfoot-type wrench in a straight line with the torque wrench, or you will apply improper torque.

Courtesy of HONDA, U.S.A., INC.

Engine Electrical (1.5L)

Location | Item | Remark | Torque

Starting system | Starter bolt (10 mm) | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Starter bolt (12 mm) | 65 N.m (6.6 kgf.m, 48 lbf.ft)

Positive starter cable nut | 9.0 N.m (0.92 kgf.m, 6.6 lbf.ft)

Ignition system | Spark plugs | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Charging system | Alternator bolts | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Positive alternator cable nut | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Drive belt auto-tensioner bolt (8 mm) | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Drive belt auto-tensioner bolt (10 mm) | 55 N.m (5.6 kgf.m, 41 lbf.ft)

Engine Electrical (2.0L)

Location | Item | Remark | Torque

Starting system | Starter bolts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Positive starter cable nut | 9.0 N.m (0.92 kgf.m, 6.6 lbf.ft)

Ignition system | Spark plugs | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Charging system | Alternator bolts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Positive alternator cable nut | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Drive belt auto-tensioner bolt (8 mm) | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Drive belt auto-tensioner bolt (10 mm) | 55 N.m (5.6 kgf.m, 41 lbf.ft)

Engine Mechanical (1.5L)

Location | Item | Remark | Torque

Engine assembly | Side engine mount bolts (12 mm) | Use new bolts | 49 N.m (5.0 kgf.m, 36 lbf.ft)

Side engine mount bolts (14 mm) | Use new bolts | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Side engine mount nut | Use new nut | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Side engine mount bracket bolts | Use new bolts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Torque rod bolts *2 | Use new bolts | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Torque rod bracket bolts | Use new bolts | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Transmission mount bolts | Use new bolts | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Transmission mount bracket bolt | Use new bolt | 78 N.m (8.0 kgf.m, 58 lbf.ft)

Transmission mount bracket nuts | Use new nuts | 78 N.m (8.0 kgf.m, 58 lbf.ft)

Engine lubrication | Oil pressure switch | Apply liquid gasket on threads | 18 N.m (1.8 kgf.m, 13 lbf.ft)

Oil pan drain bolt | Use new washer | 40 N.m (4.1 kgf.m, 30 lbf.ft)

Oil filter | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Intake manifold and exhaust system | Intake manifold bolts *1 | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Intake manifold nuts *1 | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Exhaust pipe A self-locking nuts | TWC side | Use new gasket and nuts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Muffler R self-locking nuts | Exhaust pipe A side | Use new gasket and nuts | 33 N.m (3.4 kgf.m, 24 lbf.ft)

Muffler L side | Use new gasket and nuts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Turbocharger self-locking nuts*2 | Use new gasket and nuts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Turbocharger bolts*2 | Use new gasket | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Engine Mechanical (2.0L)

Location | Item | Remark | Torque

Engine assembly | Side engine mount bolts (12 mm) | Use new bolts | 49 N.m (5.0 kgf.m, 36 lbf.ft)

Side engine mount bolts (14 mm) | Use new bolts | 93 N.m (9.5 kgf.m, 69 lbf.ft)
````

## Chunk 8541: Torque Specifications (USA/Canada models) (2016)

- Title: Torque Specifications (USA/Canada models) (2016)
- Source path: `pages\11016.html`
- Chunk ID: `chunk_bedb2aa00843`
- Images: `images\GHH412697.png`, `images\GHH412698.png`, `images\GHH412699.jpeg`
- Duplicate sources: `pages\15592.html`

### Full Text

````text
ke manifold bolts *1 | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Intake manifold nuts *1 | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Exhaust pipe A self-locking nuts | TWC side | Use new gasket and nuts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Muffler R self-locking nuts | Exhaust pipe A side | Use new gasket and nuts | 33 N.m (3.4 kgf.m, 24 lbf.ft)

Muffler L side | Use new gasket and nuts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Turbocharger self-locking nuts*2 | Use new gasket and nuts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Turbocharger bolts*2 | Use new gasket | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Engine Mechanical (2.0L)

Location | Item | Remark | Torque

Engine assembly | Side engine mount bolts (12 mm) | Use new bolts | 49 N.m (5.0 kgf.m, 36 lbf.ft)

Side engine mount bolts (14 mm) | Use new bolts | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Side engine mount nut | Use new nut | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Side engine mount bracket bolts | Use new bolts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Torque rod bolts *2 | Use new bolts | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Torque rod bracket bolts | Use new bolts | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Transmission mount bolts | Use new bolts | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Transmission mount bracket bolt(s) | Use new bolt(s) | 78 N.m (8.0 kgf.m, 58 lbf.ft)

Transmission mount bracket nuts | Use new nuts | 78 N.m (8.0 kgf.m, 58 lbf.ft)

Engine lubrication | Oil pressure switch | Apply liquid gasket on threads | 17 N.m (1.7 kgf.m, 13 lbf.ft)

Oil pan drain bolt | Use new washer | 40 N.m (4.1 kgf.m, 30 lbf.ft)

Oil filter | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Intake manifold and exhaust system | Intake manifold bolts *1 | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Intake manifold nuts *1 | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Muffler self-locking nuts *1 | Use new gasket and nuts | 33 N.m (3.4 kgf.m, 24 lbf.ft)

Exhaust pipe A self-locking nuts | Use new gasket and nuts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Engine Cooling (1.5L)

Location | Item | Remark | Torque

Cooling system | Water passage bolts | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Water passage nuts | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Thermostat housing bolts | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Thermostat housing nuts | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Engine Cooling (2.0L)

Location | Item | Remark | Torque

Cooling system | Water passage bolts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Water passage nuts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Thermostat housing bolts | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Thermostat housing nuts | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Fuel Emissions (1.5L)

Location | Item | Remark | Torque

Fuel and emissions | Accelerator pedal module | 13 N.m (1.3 kgf.m, 10 lbf.ft)

A/F sensor | 45 N.m (4.6 kgf.m, 33 lbf.ft)

ECT Sensor 1/2 | Use new O-ring | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Exhaust chamber cover | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Fuel tank*2 | Fuel tank bolts | 23 N.m (2.3 kgf.m, 17 lbf.ft)

Support strap bolts | 38 N.m (3.9 kgf.m, 28 lbf.ft)

Knock sensor | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Secondary HO2S | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Throttle body bolts*2 | Use new gasket | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Catalytic converter bracket bolts*2 | Catalytic converter side | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Engine side | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Catalytic converter upper bolts | Use new gaskets and nuts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Catalytic converter upper nuts | Use new gaskets and nuts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Fuel Emissions (2.0L)

Location | Item | Remark | Torque

Fuel and emissions | Accelerator pedal module | 13 N.m (1.3 kgf.m, 10 lbf.ft)

A/F sensor | 45 N.m (4.6 kgf.m, 33 lbf.ft)

ECT Sensor 1/2 | Use new O-ring | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Exhaust chamber cover | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Fuel tank*2 | Fuel tank bolts | 23 N.m (2.3 kgf.m, 17 lbf.ft)

Support strap bolts | 38 N.m (3.9 kgf.m, 28 lbf.ft)

Knock sensor | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Rocker arm oil pressure switch | Use new O-ring | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Secondary HO2S | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Throttle body bolts*2 | Use new gasket | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Catalytic converter bracket bolts*2 | Catalytic converter side | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Engine side | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Catalytic converter upper bolts | Use new gaskets and nuts | 32 N.m (3.3 kgf.m, 24 lbf.ft)

Catalytic converter upper nuts | Use new gaskets and nuts | 32 N.m (3.3 kgf.m, 24 lbf.ft)

Clutch

Location | Item | Remark | Torque

Clutch | Clutch master cylinder push rod locknut | 17 N.m (1.7 kgf.m, 13 lbf.ft)
````

## Chunk 8542: Torque Specifications (USA/Canada models) (2016)

- Title: Torque Specifications (USA/Canada models) (2016)
- Source path: `pages\11016.html`
- Chunk ID: `chunk_b98f64b44353`
- Images: `images\GHH412697.png`, `images\GHH412698.png`, `images\GHH412699.jpeg`
- Duplicate sources: `pages\15592.html`

### Full Text

````text
| Fuel tank bolts | 23 N.m (2.3 kgf.m, 17 lbf.ft)

Support strap bolts | 38 N.m (3.9 kgf.m, 28 lbf.ft)

Knock sensor | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Rocker arm oil pressure switch | Use new O-ring | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Secondary HO2S | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Throttle body bolts*2 | Use new gasket | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Catalytic converter bracket bolts*2 | Catalytic converter side | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Engine side | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Catalytic converter upper bolts | Use new gaskets and nuts | 32 N.m (3.3 kgf.m, 24 lbf.ft)

Catalytic converter upper nuts | Use new gaskets and nuts | 32 N.m (3.3 kgf.m, 24 lbf.ft)

Clutch

Location | Item | Remark | Torque

Clutch | Clutch master cylinder push rod locknut | 17 N.m (1.7 kgf.m, 13 lbf.ft)

Clutch pedal position switch locknut | 9.4 N.m (0.96 kgf.m, 6.9 lbf.ft)

Clutch pedal adjusting bolt locknut | 9.4 N.m (0.96 kgf.m, 6.9 lbf.ft)

Master cylinder nuts | 13 N.m (1.3 kgf.m, 10 lbf.ft)

Slave cylinder bolts | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Flywheel bolts*1 | 1.5L engine | 118 N.m (12.0 kgf.m, 87 lbf.ft)

2.0L engine | 123 N.m (12.5 kgf.m, 91 lbf.ft)

Pressure plate bolts*1 | 26 N.m (2.7 kgf.m, 19 lbf.ft)

Release fork bolt | 29 N.m (3.0 kgf.m, 21 lbf.ft)

Manual Transmission and M/T Differential

Location | Item | Remark | Torque

Manual transmission | MTF drain plug | Use new sealing washer | 44 N.m (4.5 kgf.m, 32 lbf.ft)

MTF filler plug | Use liquid gasket on threads | 44 N.m (4.5 kgf.m, 32 lbf.ft)

Back-up light switch | Use liquid gasket on threads | 29 N.m (3.0 kgf.m, 21 lbf.ft)

Transmission assembly mounting bolts (transmission side) | 64 N.m (6.5 kgf.m, 47 lbf.ft)

Transmission assembly mounting bolts (engine side) | 65 N.m (6.6 kgf.m, 48 lbf.ft)

Change wire bracket bolts*2 | 27 N.m (2.8 kgf.m, 20 lbf.ft)

CVT and CVT Differential (1.5L)

Location | Item | Remark | Torque

CVT | Transmission fluid check bolt | Use new sealing washer | 20 N.m (2.0 kgf.m, 15 lbf.ft)

Transmission fluid drain plug | Use new sealing washer | 49 N.m (5.0 kgf.m, 36 lbf.ft)

Pressure inspection port sealing bolts (drive pulley, forward clutch, reverse brake) | Use new sealing washer | 20 N.m (2.0 kgf.m, 15 lbf.ft)

Drive plate bolts*2 | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Transmission assembly mounting bolts (transmission side) | 64 N.m (6.5 kgf.m, 47 lbf.ft)

Transmission assembly mounting bolts (engine side) | 65 N.m (6.6 kgf.m, 48 lbf.ft)

Transmission hanger bolt | 44 N.m (4.5 kgf.m, 32 lbf.ft)

CVTF warmer bolts | 27 N.m (2.8 kgf.m, 20 lbf.ft)

Shift cable bracket bolts | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Shift cable end nut | 22 N.m (2.2 kgf.m, 16 lbf.ft)

CVT driven pulley pressure sensor | Use new sealing washer | 20 N.m (2.0 kgf.m, 15 lbf.ft)

CVT and CVT Differential (2.0L)

Location | Item | Remark | Torque

CVT | Transmission fluid filler plug | Use new sealing washer | 44 N.m (4.5 kgf.m, 32 lbf.ft)

Transmission fluid drain plug | Use new sealing washer | 49 N.m (5.0 kgf.m, 36 lbf.ft)

Pressure inspection port sealing bolts (drive pulley, driven pulley, forward clutch) | Use new sealing washer | 18 N.m (1.8 kgf.m, 13 lbf.ft)

Pressure inspection port sealing bolt (reverse brake) | Use new bolt | 20 N.m (2.0 kgf.m, 15 lbf.ft)

Drive plate bolts*2 | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Transmission assembly mounting bolts (transmission side) | 64 N.m (6.5 kgf.m, 47 lbf.ft)

Transmission assembly mounting bolts (engine side) | 65 N.m (6.6 kgf.m, 48 lbf.ft)

Transmission hanger bolt | 44 N.m (4.5 kgf.m, 32 lbf.ft)

CVTF warmer bolts | 27 N.m (2.8 kgf.m, 20 lbf.ft)

Shift cable bracket bolts | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Shift cable end nut | 22 N.m (2.2 kgf.m, 16 lbf.ft)

CVT driven pulley pressure sensor | Use new sealing washer | 20 N.m (2.0 kgf.m, 15 lbf.ft)

Driveline/Axle

Location | Item | Remark | Torque

Driveline/axle | Driveshaft spindle nut (1.5L) | Use oil on the seating surface Use new nut | 245 N.m (25.0 kgf.m, 181 lbf.ft)

- Use oil on the seating surface

- Use new nut

Driveshaft spindle nut (2.0L) | Use oil on the seating surface Use new nut | 181 N.m (18.5 kgf.m, 133 lbf.ft)

- Use oil on the seating surface

- Use new nut

Intermediate shaft dowel blots | 39 N.m (4.0 kgf.m, 29 lbf.ft)

Intermediate shaft flange bolt | 39 N.m (4.0 kgf.m, 29 lbf.ft)

Steering

Location | Item | Remark | Torque

Steering | Steering wheel bolt | Use new bolt | 49 N.m (5.0 kgf.m, 36 lbf.ft)
````

## Chunk 8543: Torque Specifications (USA/Canada models) (2016)

- Title: Torque Specifications (USA/Canada models) (2016)
- Source path: `pages\11016.html`
- Chunk ID: `chunk_c58cc7778b4b`
- Images: `images\GHH412697.png`, `images\GHH412698.png`, `images\GHH412699.jpeg`
- Duplicate sources: `pages\15592.html`

### Full Text

````text
.m, 16 lbf.ft)

Shift cable end nut | 22 N.m (2.2 kgf.m, 16 lbf.ft)

CVT driven pulley pressure sensor | Use new sealing washer | 20 N.m (2.0 kgf.m, 15 lbf.ft)

Driveline/Axle

Location | Item | Remark | Torque

Driveline/axle | Driveshaft spindle nut (1.5L) | Use oil on the seating surface Use new nut | 245 N.m (25.0 kgf.m, 181 lbf.ft)

- Use oil on the seating surface

- Use new nut

Driveshaft spindle nut (2.0L) | Use oil on the seating surface Use new nut | 181 N.m (18.5 kgf.m, 133 lbf.ft)

- Use oil on the seating surface

- Use new nut

Intermediate shaft dowel blots | 39 N.m (4.0 kgf.m, 29 lbf.ft)

Intermediate shaft flange bolt | 39 N.m (4.0 kgf.m, 29 lbf.ft)

Steering

Location | Item | Remark | Torque

Steering | Steering wheel bolt | Use new bolt | 49 N.m (5.0 kgf.m, 36 lbf.ft)

Steering joint bolt | 29 N.m (3.0 kgf.m, 21 lbf.ft)

Steering column bolts*1 | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Steering column nuts*1 | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Steering gearbox bolt(s)*1 | Right-front, left-rear | Use new bolts | 85 N.m (8.7 kgf.m, 63 lbf.ft)

Left-front (lower side) | Use new bolt | 105 N.m (10.7 kgf.m, 77 lbf.ft)

Right rear, left-front (upper side) | Use new bolts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Steering gearbox stiffener bolts*1 | Use new bolts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Tie-rod end ball joint nuts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Tie-rod end locknuts | 44 N.m (4.5 kgf.m, 32 lbf.ft)

Suspension

Location | Item | Remark | Torque

Front suspension | Wheel nuts | 108 N.m (11.0 kgf.m, 80 lbf.ft)

Knuckle damper pinch bolts | 79 N.m (8.1 kgf.m, 58 lbf.ft)

Lower arm ball joint castle nut (to knuckle) | Use new nut | 78-88 N.m (8.0-9.0 kgf.m, 58-65 lbf.ft)

Lower arm nuts (to lower ball joint)*1 | Use new nuts | 64 N.m (6.5 kgf.m, 47 lbf.ft)

Lower arm bolt (front side) | Use new bolt | 120 N.m (12.2 kgf.m, 89 lbf.ft)

Lower arm bolts (rear side) | Use new bolts | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Stabilizer bar bushing holders flange bolts*1 | Use new bolts | 75 N.m (7.6 kgf.m, 55 lbf.ft)

Stabilizer link flange nut (to damper) | Use new nut | 64 N.m (6.5 kgf.m, 47 lbf.ft)

Stabilizer link flange nut (to stabilizer bar) | Use new nut | 64 N.m (6.5 kgf.m, 47 lbf.ft)

Damper nuts (to body) | Use new nuts | 75 N.m (7.6 kgf.m, 55 lbf.ft)

Damper self-locking nut | Use new nut | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Location | Item | Remark | Torque

Rear suspension | Wheel nuts | 108 N.m (11.0 kgf.m, 80 lbf.ft)

Upper arm bolt (to subframe) | Use new bolt | 76 N.m (7.7 kgf.m, 56 lbf.ft)

Upper arm bolt/nut (to knuckle) | Use new bolt/nut | 76 N.m (7.7 kgf.m, 56 lbf.ft)

Lower arm A bolt/nut (to knuckle) | Use new bolt/nut | 76 N.m (7.7 kgf.m, 56 lbf.ft)

Lower arm A bolt (to subframe) | Use new bolt | 76 N.m (7.7 kgf.m, 56 lbf.ft)

Lower arm B bolt (to knuckle) | Use new bolt | 69 N.m (7.0 kgf.m, 51 lbf.ft)

Lower arm B bolt/nut (to subframe) | Use new bolt/nut | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Trailing arm bolts/nuts (to knuckle) | Use new bolts/nuts | 118 N.m (12.0 kgf.m, 87 lbf.ft)

Trailing arm bolts (to body) | Use new bolts | 118 N.m (12.0 kgf.m, 87 lbf.ft)

Stabilizer bar bushing holders flange bolts | Use new bolts | 37 N.m (3.8 kgf.m, 27 lbf.ft)

Stabilizer link flange nut (to stabilizer bar) | Use new nut | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Stabilizer link (to lower arm B) | Use new bolt | 40 N.m (4.1 kgf.m, 30 lbf.ft)

Damper bolt (to knuckle) | Use new bolt | 81 N.m (8.3 kgf.m, 60 lbf.ft)

Damper bolts (to body) | Use new bolts | 40 N.m (4.1 kgf.m, 30 lbf.ft)

Damper self-locking nut | Use new nut | 30 N.m (3.1 kgf.m, 22 lbf.ft)

Brakes

Location | Item | Remark | Torque

Conventional brake | Front brake caliper bracket bolts | 108 N.m (11.0 kgf.m, 80 lbf.ft)

Front brake caliper bolts | 34 N.m (3.5 kgf.m, 25 lbf.ft)

Front brake hose banjo bolt | Use new washers | 35 N.m (3.6 kgf.m, 26 lbf.ft)

Rear brake caliper bracket bolts | 108 N.m (11.0 kgf.m, 80 lbf.ft)

Rear brake caliper pin bolts | 25 N.m (2.5 kgf.m, 18 lbf.ft)

Rear brake hose banjo bolt | Use new washers | 35 N.m (3.6 kgf.m, 26 lbf.ft)

Master cylinder nuts (to brake booster) | 15 N.m (1.5 kgf.m, 11 lbf.ft)

Master cylinder brake line | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Brake booster/brake pedal nuts | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Brake pedal support member bolts/nuts | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Location | Item | Remark | Torque

VSA | VSA modulator-control unit brake line (10 mm) | 15 N.m (1.5 kgf.m, 11 lbf.ft)
````

## Chunk 8544: Torque Specifications (USA/Canada models) (2016)

- Title: Torque Specifications (USA/Canada models) (2016)
- Source path: `pages\11016.html`
- Chunk ID: `chunk_0e463ef01480`
- Images: `images\GHH412697.png`, `images\GHH412698.png`, `images\GHH412699.jpeg`
- Duplicate sources: `pages\15592.html`

### Full Text

````text
ront brake caliper bracket bolts | 108 N.m (11.0 kgf.m, 80 lbf.ft)

Front brake caliper bolts | 34 N.m (3.5 kgf.m, 25 lbf.ft)

Front brake hose banjo bolt | Use new washers | 35 N.m (3.6 kgf.m, 26 lbf.ft)

Rear brake caliper bracket bolts | 108 N.m (11.0 kgf.m, 80 lbf.ft)

Rear brake caliper pin bolts | 25 N.m (2.5 kgf.m, 18 lbf.ft)

Rear brake hose banjo bolt | Use new washers | 35 N.m (3.6 kgf.m, 26 lbf.ft)

Master cylinder nuts (to brake booster) | 15 N.m (1.5 kgf.m, 11 lbf.ft)

Master cylinder brake line | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Brake booster/brake pedal nuts | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Brake pedal support member bolts/nuts | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Location | Item | Remark | Torque

VSA | VSA modulator-control unit brake line (10 mm) | 15 N.m (1.5 kgf.m, 11 lbf.ft)

VSA modulator-control unit brake line (12 mm) | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Body

Location | Item | Remark | Torque

Frame | Front subframe bolts | Use new bolts | 103 N.m (10.5 kgf.m, 76 lbf.ft)

Front subframe rear stay bolts | Use new bolts | 91 N.m (9.3 kgf.m, 67 lbf.ft)

Rear subframe bolts | Use new bolts | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Front brace bolts (10 mm) | Use new bolts | 58 N.m (5.9 kgf.m, 43 lbf.ft)

Front brace bolts (12 mm) | Use new bolts | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Heating, Ventilation, and Air Conditioning

Location | Item | Remark | Torque

A/C compressor | A/C compressor bolts | 22 N.m (2.2 kgf.m, 16 lbf.ft)

A/C compressor center bolt | Use new bolt | 17 N.m (1.7 kgf.m, 13 lbf.ft)

A/C compressor relief valve | Use new O-ring | 8.5 N.m (0.87 kgf.m, 6.3 lbf.ft)

Discharge hose | A/C pressure sensor | Use new O-ring | 11 N.m (1.1 kgf.m, 8 lbf.ft)

Body Electrical

Location | Item | Remark | Torque

Wipers/washers | Windshield wiper arm nut | 29 N.m (3.0 kgf.m, 21 lbf.ft)

Windshield wiper link nut | 31 N.m (3.2 kgf.m, 23 lbf.ft)
````

## Chunk 8545: Torque Specifications (USA/Canada models except Type-R/Si) (2017)

- Title: Torque Specifications (USA/Canada models except Type-R/Si) (2017)
- Source path: `pages\11017.html`
- Chunk ID: `chunk_a01c6260728b`
- Images: `images\GHH412700.png`, `images\GHH412701.png`, `images\GHH412702.jpeg`
- Duplicate sources: `pages\15600.html`

### Full Text

````text
# Torque Specifications (USA/Canada models except Type-R/Si) (2017)

NOTE:

- Refer to the appropriate portion of the service information for the precautions and complete procedures.

- Refer to the appropriate portion of the service information for the bolts/nuts not indicated here.

- 1: Parts to be tightened in a particular order. 2: Follow the appropriate service information procedures closely for torque, sequence, and special steps.

- 1: Parts to be tightened in a particular order.

- 2: Follow the appropriate service information procedures closely for torque, sequence, and special steps.

- When using some special tools or crowfoot-type wrenches, the torque value changes due to the added leverage. The actual torque applied will be greater than the torque reading shown.

- The torque specification given is the actual torque, not the reading on the torque wrench. To compensate for this additional leverage, use the formula below to calculate the torque value reading on the torque wrench. Always use the special tool or crowfoot-type wrench in a straight line with the torque wrench, or you will apply improper torque.

- The torque specification given is the actual torque, not the reading on the torque wrench.

- To compensate for this additional leverage, use the formula below to calculate the torque value reading on the torque wrench.

- Always use the special tool or crowfoot-type wrench in a straight line with the torque wrench, or you will apply improper torque.

Courtesy of HONDA, U.S.A., INC.

Engine Electrical (1.5L)

Location | Item | Remark | Torque

Starting system | Starter bolt (10 mm) | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Starter bolt (12 mm) | 65 N.m (6.6 kgf.m, 48 lbf.ft)

Positive starter cable nut | 9.0 N.m (0.92 kgf.m, 6.6 lbf.ft)

Ignition system | Spark plugs | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Charging system | Alternator bolts | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Positive alternator cable nut | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Drive belt auto-tensioner bolt (8 mm) | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Drive belt auto-tensioner bolt (10 mm) | 55 N.m (5.6 kgf.m, 41 lbf.ft)

Engine Electrical (2.0L)

Location | Item | Remark | Torque

Starting system | Starter bolts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Positive starter cable nut | 9.0 N.m (0.92 kgf.m, 6.6 lbf.ft)

Ignition system | Spark plugs | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Charging system | Alternator bolts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Positive alternator cable nut | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Drive belt auto-tensioner bolt (8 mm) | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Drive belt auto-tensioner bolt (10 mm) | 55 N.m (5.6 kgf.m, 41 lbf.ft)

Engine Mechanical (1.5L)

Location | Item | Remark | Torque

Engine assembly | Side engine mount bolts (12 mm) | Use new bolts | 49 N.m (5.0 kgf.m, 36 lbf.ft)

Side engine mount bolts (14 mm) | Use new bolts | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Side engine mount nut | Use new nut | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Side engine mount bracket bolts | Use new bolts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Torque rod bolts *2 | Use new bolts | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Torque rod bracket bolts | Use new bolts | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Transmission mount bolts | Use new bolts | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Transmission mount bracket bolt(s) | 2/4-door | Use new bolt(s) | 78 N.m (8.0 kgf.m, 58 lbf.ft)

5-door | Use new bolt(s) | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Transmission mount bracket nuts | 2/4-door | Use new nuts | 78 N.m (8.0 kgf.m, 58 lbf.ft)

5-door | Use new nuts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Engine lubrication | Oil pressure switch | Apply liquid gasket on threads | 18 N.m (1.8 kgf.m, 13 lbf.ft)

Oil pan drain bolt | Use new washer | 40 N.m (4.1 kgf.m, 30 lbf.ft)

Oil filter | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Intake manifold and exhaust system | Intake manifold bolts *1 | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Intake manifold nuts *1 | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Exhaust pipe A self-locking nuts | TWC side | Use new gasket and nuts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Muffler R self-locking nuts (dual muffler) | Exhaust pipe A side | Use new gasket and nuts | 33 N.m (3.4 kgf.m, 24 lbf.ft)

Muffler L side | Use new gasket and nuts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Muffler self-locking nuts (center muffler) | Use new gasket and nuts | 33 N.m (3.4 kgf.m, 24 lbf.ft)

Turbocharger self-locking nuts*2 | Use new gasket and nuts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Turbocharger bolts*2 | Use new gasket | 45 N.m (4.6 kgf.m, 33 lbf.ft)
````

## Chunk 8546: Torque Specifications (USA/Canada models except Type-R/Si) (2017)

- Title: Torque Specifications (USA/Canada models except Type-R/Si) (2017)
- Source path: `pages\11017.html`
- Chunk ID: `chunk_1c82ad0ad383`
- Images: `images\GHH412700.png`, `images\GHH412701.png`, `images\GHH412702.jpeg`
- Duplicate sources: `pages\15600.html`

### Full Text

````text
washer | 40 N.m (4.1 kgf.m, 30 lbf.ft)

Oil filter | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Intake manifold and exhaust system | Intake manifold bolts *1 | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Intake manifold nuts *1 | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Exhaust pipe A self-locking nuts | TWC side | Use new gasket and nuts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Muffler R self-locking nuts (dual muffler) | Exhaust pipe A side | Use new gasket and nuts | 33 N.m (3.4 kgf.m, 24 lbf.ft)

Muffler L side | Use new gasket and nuts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Muffler self-locking nuts (center muffler) | Use new gasket and nuts | 33 N.m (3.4 kgf.m, 24 lbf.ft)

Turbocharger self-locking nuts*2 | Use new gasket and nuts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Turbocharger bolts*2 | Use new gasket | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Engine Mechanical (2.0L)

Location | Item | Remark | Torque

Engine assembly | Side engine mount bolts (12 mm) | Use new bolts | 49 N.m (5.0 kgf.m, 36 lbf.ft)

Side engine mount bolts (14 mm) | Use new bolts | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Side engine mount nut | Use new nut | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Side engine mount bracket bolts | Use new bolts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Torque rod bolts *2 | Use new bolts | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Torque rod bracket bolts | Use new bolts | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Transmission mount bolts | Use new bolts | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Transmission mount bracket bolt(s) | Use new bolt(s) | 78 N.m (8.0 kgf.m, 58 lbf.ft)

Transmission mount bracket nuts | Use new nuts | 78 N.m (8.0 kgf.m, 58 lbf.ft)

Engine lubrication | Oil pressure switch | Apply liquid gasket on threads | 17 N.m (1.7 kgf.m, 13 lbf.ft)

Oil pan drain bolt | Use new washer | 40 N.m (4.1 kgf.m, 30 lbf.ft)

Oil filter | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Intake manifold and exhaust system | Intake manifold bolts *1 | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Intake manifold nuts *1 | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Muffler self-locking nuts *1 | Use new gasket and nuts | 33 N.m (3.4 kgf.m, 24 lbf.ft)

Exhaust pipe A self-locking nuts | Use new gasket and nuts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Engine Cooling (1.5L)

Location | Item | Remark | Torque

Cooling system | Water passage bolts | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Water passage nuts | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Thermostat housing bolts | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Thermostat housing nuts | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Engine Cooling (2.0L)

Location | Item | Remark | Torque

Cooling system | Water passage bolts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Water passage nuts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Thermostat housing bolts | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Thermostat housing nuts | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Fuel Emissions (1.5L)

Location | Item | Remark | Torque

Fuel and emissions | Accelerator pedal module | 13 N.m (1.3 kgf.m, 10 lbf.ft)

A/F sensor | 45 N.m (4.6 kgf.m, 33 lbf.ft)

ECT Sensor 1/2 | Use new O-ring | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Exhaust chamber cover | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Fuel tank*2 | Fuel tank bolts (2/4-door) | 23 N.m (2.3 kgf.m, 17 lbf.ft)

Fuel tank bolts (5-door) | 24 N.m (2.4 kgf.m, 18 lbf.ft)

Support strap bolts | 38 N.m (3.9 kgf.m, 28 lbf.ft)

Knock sensor | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Secondary HO2S | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Throttle body bolts*2 | Use new gasket | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Catalytic converter bracket bolts*2 | Catalytic converter side | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Engine side | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Catalytic converter upper bolts | Use new gaskets and nuts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Catalytic converter upper nuts | Use new gaskets and nuts | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Fuel Emissions (2.0L)

Location | Item | Remark | Torque

Fuel and emissions | Accelerator pedal module | 13 N.m (1.3 kgf.m, 10 lbf.ft)

A/F sensor | 45 N.m (4.6 kgf.m, 33 lbf.ft)

ECT Sensor 1/2 | Use new O-ring | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Exhaust chamber cover | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Fuel tank*2 | Fuel tank bolts | 23 N.m (2.3 kgf.m, 17 lbf.ft)

Support strap bolts | 38 N.m (3.9 kgf.m, 28 lbf.ft)

Knock sensor | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Rocker arm oil pressure switch | Use new O-ring | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Secondary HO2S | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Throttle body bolts*2 | Use new gasket | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Catalytic converter bracket bolts*2 | Catalytic converter side | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Engine side | 45 N.m (4.6 kgf.m, 33 lbf.ft)
````

## Chunk 8547: Torque Specifications (USA/Canada models except Type-R/Si) (2017)

- Title: Torque Specifications (USA/Canada models except Type-R/Si) (2017)
- Source path: `pages\11017.html`
- Chunk ID: `chunk_5110f755a961`
- Images: `images\GHH412700.png`, `images\GHH412701.png`, `images\GHH412702.jpeg`
- Duplicate sources: `pages\15600.html`

### Full Text

````text
l Emissions (2.0L)

Location | Item | Remark | Torque

Fuel and emissions | Accelerator pedal module | 13 N.m (1.3 kgf.m, 10 lbf.ft)

A/F sensor | 45 N.m (4.6 kgf.m, 33 lbf.ft)

ECT Sensor 1/2 | Use new O-ring | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Exhaust chamber cover | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Fuel tank*2 | Fuel tank bolts | 23 N.m (2.3 kgf.m, 17 lbf.ft)

Support strap bolts | 38 N.m (3.9 kgf.m, 28 lbf.ft)

Knock sensor | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Rocker arm oil pressure switch | Use new O-ring | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Secondary HO2S | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Throttle body bolts*2 | Use new gasket | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Catalytic converter bracket bolts*2 | Catalytic converter side | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Engine side | 45 N.m (4.6 kgf.m, 33 lbf.ft)

Catalytic converter upper bolts | Use new gaskets and nuts | 32 N.m (3.3 kgf.m, 24 lbf.ft)

Catalytic converter upper nuts | Use new gaskets and nuts | 32 N.m (3.3 kgf.m, 24 lbf.ft)

Clutch

Location | Item | Remark | Torque

Clutch | Clutch master cylinder push rod locknut | 17 N.m (1.7 kgf.m, 13 lbf.ft)

Clutch pedal position switch locknut | 9.4 N.m (0.96 kgf.m, 6.9 lbf.ft)

Clutch pedal adjusting bolt locknut | 9.4 N.m (0.96 kgf.m, 6.9 lbf.ft)

Master cylinder nuts | 13 N.m (1.3 kgf.m, 10 lbf.ft)

Slave cylinder bolts | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Flywheel bolts*1 | 1.5L engine | 118 N.m (12.0 kgf.m, 87 lbf.ft)

2.0L engine | 123 N.m (12.5 kgf.m, 91 lbf.ft)

Pressure plate bolts*1 | 26 N.m (2.7 kgf.m, 19 lbf.ft)

Release fork bolt | 29 N.m (3.0 kgf.m, 21 lbf.ft)

Manual Transmission and M/T Differential

Location | Item | Remark | Torque

Manual transmission | MTF drain plug | Use new sealing washer | 44 N.m (4.5 kgf.m, 32 lbf.ft)

MTF filler plug | Use liquid gasket on threads | 44 N.m (4.5 kgf.m, 32 lbf.ft)

Back-up light switch | Use liquid gasket on threads | 29 N.m (3.0 kgf.m, 21 lbf.ft)

Transmission assembly mounting bolts (transmission side) | 64 N.m (6.5 kgf.m, 47 lbf.ft)

Transmission assembly mounting bolts (engine side) | 65 N.m (6.6 kgf.m, 48 lbf.ft)

Change wire bracket bolts*2 | 27 N.m (2.8 kgf.m, 20 lbf.ft)

CVT and CVT Differential (1.5L)

Location | Item | Remark | Torque

CVT | Transmission fluid check bolt | Use new sealing washer | 20 N.m (2.0 kgf.m, 15 lbf.ft)

Transmission fluid drain plug | Use new sealing washer | 49 N.m (5.0 kgf.m, 36 lbf.ft)

Pressure inspection port sealing bolts (drive pulley, forward clutch, reverse brake) | Use new sealing washer | 20 N.m (2.0 kgf.m, 15 lbf.ft)

Drive plate bolts*2 | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Transmission assembly mounting bolts (transmission side) | 64 N.m (6.5 kgf.m, 47 lbf.ft)

Transmission assembly mounting bolts (engine side) | 65 N.m (6.6 kgf.m, 48 lbf.ft)

Transmission hanger bolt | 44 N.m (4.5 kgf.m, 32 lbf.ft)

CVTF warmer bolts | 27 N.m (2.8 kgf.m, 20 lbf.ft)

Shift cable bracket bolts | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Shift cable end nut | 22 N.m (2.2 kgf.m, 16 lbf.ft)

CVT driven pulley pressure sensor | Use new sealing washer | 20 N.m (2.0 kgf.m, 15 lbf.ft)

CVT and CVT Differential (2.0L)

Location | Item | Remark | Torque

CVT | Transmission fluid filler plug | Use new sealing washer | 44 N.m (4.5 kgf.m, 32 lbf.ft)

Transmission fluid drain plug | Use new sealing washer | 49 N.m (5.0 kgf.m, 36 lbf.ft)

Pressure inspection port sealing bolts (drive pulley, driven pulley, forward clutch) | Use new sealing washer | 18 N.m (1.8 kgf.m, 13 lbf.ft)

Pressure inspection port sealing bolt (reverse brake) | Use new bolt | 20 N.m (2.0 kgf.m, 15 lbf.ft)

Drive plate bolts*2 | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Transmission assembly mounting bolts (transmission side) | 64 N.m (6.5 kgf.m, 47 lbf.ft)

Transmission assembly mounting bolts (engine side) | 65 N.m (6.6 kgf.m, 48 lbf.ft)

Transmission hanger bolt | 44 N.m (4.5 kgf.m, 32 lbf.ft)

CVTF warmer bolts | 27 N.m (2.8 kgf.m, 20 lbf.ft)

Shift cable bracket bolts | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Shift cable end nut | 22 N.m (2.2 kgf.m, 16 lbf.ft)

CVT driven pulley pressure sensor | Use new sealing washer | 20 N.m (2.0 kgf.m, 15 lbf.ft)

Driveline/Axle

Location | Item | Remark | Torque

Driveline/axle | Driveshaft spindle nut (1.5L) | Use oil on the seating surface Use new nut | 245 N.m (25.0 kgf.m, 181 lbf.ft)

- Use oil on the seating surface

- Use new nut

Driveshaft spindle nut (2.0L) | Use oil on the seating surface Use new nut | 181 N.m (18.5 kgf.m, 133 lbf.ft)

- Use oil on the seating surface
````

## Chunk 8548: Torque Specifications (USA/Canada models except Type-R/Si) (2017)

- Title: Torque Specifications (USA/Canada models except Type-R/Si) (2017)
- Source path: `pages\11017.html`
- Chunk ID: `chunk_9261b3f1c9e8`
- Images: `images\GHH412700.png`, `images\GHH412701.png`, `images\GHH412702.jpeg`
- Duplicate sources: `pages\15600.html`

### Full Text

````text
64 N.m (6.5 kgf.m, 47 lbf.ft)

Transmission assembly mounting bolts (engine side) | 65 N.m (6.6 kgf.m, 48 lbf.ft)

Transmission hanger bolt | 44 N.m (4.5 kgf.m, 32 lbf.ft)

CVTF warmer bolts | 27 N.m (2.8 kgf.m, 20 lbf.ft)

Shift cable bracket bolts | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Shift cable end nut | 22 N.m (2.2 kgf.m, 16 lbf.ft)

CVT driven pulley pressure sensor | Use new sealing washer | 20 N.m (2.0 kgf.m, 15 lbf.ft)

Driveline/Axle

Location | Item | Remark | Torque

Driveline/axle | Driveshaft spindle nut (1.5L) | Use oil on the seating surface Use new nut | 245 N.m (25.0 kgf.m, 181 lbf.ft)

- Use oil on the seating surface

- Use new nut

Driveshaft spindle nut (2.0L) | Use oil on the seating surface Use new nut | 181 N.m (18.5 kgf.m, 133 lbf.ft)

- Use oil on the seating surface

- Use new nut

Intermediate shaft dowel blots | 39 N.m (4.0 kgf.m, 29 lbf.ft)

Intermediate shaft flange bolt | 39 N.m (4.0 kgf.m, 29 lbf.ft)

Steering

Location | Item | Remark | Torque

Steering | Steering wheel bolt | Use new bolt | 49 N.m (5.0 kgf.m, 36 lbf.ft)

Steering joint bolt | 29 N.m (3.0 kgf.m, 21 lbf.ft)

Steering column bolts*1 | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Steering column nuts*1 | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Steering gearbox bolt(s)*1 | Right-front, left-rear | Use new bolts | 85 N.m (8.7 kgf.m, 63 lbf.ft)

Left-front (lower side) | Use new bolt | 105 N.m (10.7 kgf.m, 77 lbf.ft)

Right rear, left-front (upper side) | Use new bolts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Steering gearbox stiffener bolts*1 | Use new bolts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Tie-rod end ball joint nuts | 54 N.m (5.5 kgf.m, 40 lbf.ft)

Tie-rod end locknuts | 44 N.m (4.5 kgf.m, 32 lbf.ft)

Suspension

Location | Item | Remark | Torque

Front suspension | Wheel nuts | 108 N.m (11.0 kgf.m, 80 lbf.ft)

Knuckle damper pinch bolts | 79 N.m (8.1 kgf.m, 58 lbf.ft)

Lower arm ball joint castle nut (to knuckle) | Use new nut | 78-88 N.m (8.0-9.0 kgf.m, 58-65 lbf.ft)

Lower arm nuts (to lower ball joint)*1 | Use new nuts | 64 N.m (6.5 kgf.m, 47 lbf.ft)

Lower arm bolt (front side) | Use new bolt | 120 N.m (12.2 kgf.m, 89 lbf.ft)

Lower arm bolts (rear side) | Use new bolts | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Stabilizer bar bushing holders flange bolts*1 | Use new bolts | 75 N.m (7.6 kgf.m, 55 lbf.ft)

Stabilizer link flange nut (to damper) | Use new nut | 64 N.m (6.5 kgf.m, 47 lbf.ft)

Stabilizer link flange nut (to stabilizer bar) | 2/4-door | Use new nut | 64 N.m (6.5 kgf.m, 47 lbf.ft)

5-door | Use new nut | 35 N.m (3.6 kgf.m, 26 lbf.ft)

Damper nuts (to body) | 2/4-door | Use new nuts | 75 N.m (7.6 kgf.m, 55 lbf.ft)

5-door | Use new nuts | 63 N.m (6.4 kgf.m, 46 lbf.ft)

Damper self-locking nut | 2/4-door (screw guide pin type) | Use new nut | 54 N.m (5.5 kgf.m, 40 lbf.ft)

2/4-door (hex guide pin type) | Use new nut | 68 N.m (6.9 kgf.m, 50 lbf.ft)

5-door | Use new nut | 75 N.m (7.6 kgf.m, 55 lbf.ft)

Rear suspension | Wheel nuts | 108 N.m (11.0 kgf.m, 80 lbf.ft)

Upper arm bolt (to subframe) | Use new bolt | 76 N.m (7.7 kgf.m, 56 lbf.ft)

Upper arm bolt/nut (to knuckle) | Use new bolt/nut | 76 N.m (7.7 kgf.m, 56 lbf.ft)

Lower arm A bolt/nut (to knuckle) | Use new bolt/nut | 76 N.m (7.7 kgf.m, 56 lbf.ft)

Lower arm A bolt (to subframe) | Use new bolt | 76 N.m (7.7 kgf.m, 56 lbf.ft)

Lower arm B bolt (to knuckle) | Use new bolt | 69 N.m (7.0 kgf.m, 51 lbf.ft)

Lower arm B bolt/nut (to subframe) | Use new bolt/nut | 93 N.m (9.5 kgf.m, 69 lbf.ft)

Trailing arm bolts/nuts (to knuckle) | Use new bolts/nuts | 118 N.m (12.0 kgf.m, 87 lbf.ft)

Trailing arm bolts (to body) | Use new bolts | 118 N.m (12.0 kgf.m, 87 lbf.ft)

Stabilizer bar bushing holders flange bolts | Use new bolts | 37 N.m (3.8 kgf.m, 27 lbf.ft)

Stabilizer link flange nut (to stabilizer bar) | Use new nut | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Stabilizer link (to lower arm B) | Use new bolt | 40 N.m (4.1 kgf.m, 30 lbf.ft)

Damper bolt (to knuckle) | Use new bolt | 81 N.m (8.3 kgf.m, 60 lbf.ft)

Damper bolts (to body) | Use new bolts | 40 N.m (4.1 kgf.m, 30 lbf.ft)

Damper self-locking nut | Use new nut | 30 N.m (3.1 kgf.m, 22 lbf.ft)

Brakes

Location | Item | Remark | Torque

Conventional brake | Front brake caliper bracket bolts | 108 N.m (11.0 kgf.m, 80 lbf.ft)

Front brake caliper bolts | 34 N.m (3.5 kgf.m, 25 lbf.ft)

Front brake hose banjo bolt | Use new washers | 35 N.m (3.6 kgf.m, 26 lbf.ft)

Rear brake caliper bracket bolts | 108 N.m (11.0 kgf.m, 80 lbf.ft)
````

## Chunk 8549: Torque Specifications (USA/Canada models except Type-R/Si) (2017)

- Title: Torque Specifications (USA/Canada models except Type-R/Si) (2017)
- Source path: `pages\11017.html`
- Chunk ID: `chunk_b0402be1649f`
- Images: `images\GHH412700.png`, `images\GHH412701.png`, `images\GHH412702.jpeg`
- Duplicate sources: `pages\15600.html`

### Full Text

````text
holders flange bolts | Use new bolts | 37 N.m (3.8 kgf.m, 27 lbf.ft)

Stabilizer link flange nut (to stabilizer bar) | Use new nut | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Stabilizer link (to lower arm B) | Use new bolt | 40 N.m (4.1 kgf.m, 30 lbf.ft)

Damper bolt (to knuckle) | Use new bolt | 81 N.m (8.3 kgf.m, 60 lbf.ft)

Damper bolts (to body) | Use new bolts | 40 N.m (4.1 kgf.m, 30 lbf.ft)

Damper self-locking nut | Use new nut | 30 N.m (3.1 kgf.m, 22 lbf.ft)

Brakes

Location | Item | Remark | Torque

Conventional brake | Front brake caliper bracket bolts | 108 N.m (11.0 kgf.m, 80 lbf.ft)

Front brake caliper bolts | 34 N.m (3.5 kgf.m, 25 lbf.ft)

Front brake hose banjo bolt | Use new washers | 35 N.m (3.6 kgf.m, 26 lbf.ft)

Rear brake caliper bracket bolts | 108 N.m (11.0 kgf.m, 80 lbf.ft)

Rear brake caliper pin bolts | 25 N.m (2.5 kgf.m, 18 lbf.ft)

Rear brake hose banjo bolt | Use new washers | 35 N.m (3.6 kgf.m, 26 lbf.ft)

Master cylinder nuts (to brake booster) | 15 N.m (1.5 kgf.m, 11 lbf.ft)

Master cylinder brake line | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Brake booster/brake pedal nuts | 12 N.m (1.2 kgf.m, 9 lbf.ft)

Brake pedal support member bolts/nuts | 22 N.m (2.2 kgf.m, 16 lbf.ft)

VSA | VSA modulator-control unit brake line (10 mm) | 15 N.m (1.5 kgf.m, 11 lbf.ft)

VSA modulator-control unit brake line (12 mm) | 22 N.m (2.2 kgf.m, 16 lbf.ft)

Body

Location | Item | Remark | Torque

Frame | Front subframe bolts | Use new bolts | 103 N.m (10.5 kgf.m, 76 lbf.ft)

Front subframe rear stay bolts | Use new bolts | 91 N.m (9.3 kgf.m, 67 lbf.ft)

Rear subframe bolts | Use new bolts | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Front brace bolts (10 mm) | Use new bolts | 58 N.m (5.9 kgf.m, 43 lbf.ft)

Front brace bolts (12 mm) | Use new bolts | 74 N.m (7.5 kgf.m, 55 lbf.ft)

Heating, Ventilation, and Air Conditioning

Location | Item | Remark | Torque

A/C compressor | A/C compressor bolts | 22 N.m (2.2 kgf.m, 16 lbf.ft)

A/C compressor center bolt | Use new bolt | 17 N.m (1.7 kgf.m, 13 lbf.ft)

A/C compressor relief valve | Use new O-ring | 8.5 N.m (0.87 kgf.m, 6.3 lbf.ft)

Discharge hose | A/C pressure sensor | Use new O-ring | 11 N.m (1.1 kgf.m, 8 lbf.ft)

Body Electrical

Location | Item | Remark | Torque

Wipers/washers | Windshield wiper arm nut | 29 N.m (3.0 kgf.m, 21 lbf.ft)

Windshield wiper link nut | 31 N.m (3.2 kgf.m, 23 lbf.ft)

Rear wiper arm nut | 9.4 N.m (0.96 kgf.m, 6.9 lbf.ft)
````

## Chunk 8550: ATEQ TPMS Reset Procedure

- Title: ATEQ TPMS Reset Procedure
- Source path: `pages\11020.html`
- Chunk ID: `chunk_8dd913ad958e`
- Images: `images\G00561416.png`
- Duplicate sources: `pages\20050.html`

### Full Text

````text
# ATEQ TPMS Reset Procedure

- Adjust the pressure in one or more tires.

- Rotate the tires.

- Replace one or more tires.

- Adjust the pressure in one or more tires.

- The vehicle is at a complete stop.

- Manual Transmission models: The shift lever is in (N).

- Automatic Transmission models (CVT): The shift lever is in (P).

Calibration Procedure

- TPMS cannot be calibrated if a compact spare tire is installed.

- The calibration process requires approximately 30 minutes of cumulative driving at speeds between 30-60 mph (48-97 km/h).

- During the calibration process, if the ignition is turned on and the vehicle is not moved within 45 seconds, the low tire pressure indicator comes on briefly. This is normal and indicates that the calibration process is not yet complete.

- If snow chains are installed, remove them before calibrating the TPMS.

- Turn the ignition switch to ON.

- Press the MENU button (left side of steering wheel) to go to the Vehicle Menu screen.

- Select Customize Settings with the (+/-) button, then press the SOURCE button.

- Select TPMS Calibration with the (+/-) button, then press the SOURCE button.

- The display switches to the Customization setup screen, select Initialize. Select Yes with the (+/-) button, then press the SOURCE button.

When the calibration is complete, the TPMS has been initialized. A message appears, and the display returns to the customization menu screen.

- If the "Unable To Initialize TPMS" message appears, repeat steps 4 and 5.

- The calibration process finishes automatically.
````

## Chunk 8551: Emissions Maintenance Reminder: Notes

- Title: Emissions Maintenance Reminder: Notes
- Source path: `pages\11021.html`
- Chunk ID: `chunk_389f192cb4ef`
- Images: none
- Duplicate sources: `pages\11505.html`, `pages\19986.html`, `pages\17653.html`

### Full Text

````text
# Emissions Maintenance Reminder: Notes

Model & Year | Reset Procedure

Passport DX

1994-95 | Emissions Maintenance Reminder Reset Procedure
````

## Chunk 8552: Emissions Maintenance Reminder Reset Procedure

- Title: Emissions Maintenance Reminder Reset Procedure
- Source path: `pages\11022.html`
- Chunk ID: `chunk_6d1adadbd1ed`
- Images: `images\G00293479.gif`, `images\G93J44841.gif`
- Duplicate sources: `pages\11506.html`, `pages\19987.html`, `pages\17654.html`

### Full Text

````text
# Emissions Maintenance Reminder Reset Procedure

- Heated Oxygen Sensor (HO2S) must be replaced every 90, 000 miles. When odometer reaches 90, 000 miles, O2S indicator light on dash will illuminate, and then every subsequent 90, 000 miles. After servicing, turn off or reset warning light.

- To reset warning light, remove instrument cluster. Remove masking tape from hole "B". See Fig 1 or Fig 2 . Remove screw from hole "A" and insert into hole "B". Apply new masking tape to hole "A".
````

## Chunk 8553: Engine Oil Replacement Reminder: Notes

- Title: Engine Oil Replacement Reminder: Notes
- Source path: `pages\11023.html`
- Chunk ID: `chunk_fbd72f14fa4d`
- Images: none
- Duplicate sources: `pages\11507.html`, `pages\19988.html`, `pages\17655.html`

### Full Text

````text
# Engine Oil Replacement Reminder: Notes

Model & Year | Reset Procedure

Accord

2006-16 | Engine Oil Replacement Reminder Reset - Procedure 01

2017 | Engine Oil Replacement Reminder Reset - Procedure 17

2019-25 | Engine Oil Replacement Reminder Reset - Procedure 19

Accord Hybrid

2014-25 | Engine Oil Replacement Reminder Reset - Procedure 19

Civic

2006-12 | Engine Oil Replacement Reminder Reset - Procedure 01

2013-15 | With Information Display: Engine Oil Replacement Reminder Reset - Procedure 01 With i-MID: Engine Oil Replacement Reminder Reset - Procedure 11

2016 | Engine Oil Replacement Reminder Reset - Procedure 13

2017-25 | Engine Oil Replacement Reminder Reset - Procedure 23

Civic Hybrid

2012-15 | Engine Oil Replacement Reminder Reset - Procedure 23

Clarity

2017-21 | Engine Oil Replacement Reminder Reset - Procedure 23

CR-V

2007-11 | Engine Oil Replacement Reminder Reset - Procedure 02

2012-16 | Engine Oil Replacement Reminder Reset - Procedure 23

2017-25 | Engine Oil Replacement Reminder Reset - Procedure 18

CR-Z

2011-16 | Engine Oil Replacement Reminder Reset - Procedure 06

Crosstour

2012-15 | Engine Oil Replacement Reminder Reset - Procedure 06

Element

2007-11 | Engine Oil Replacement Reminder Reset - Procedure 06

Fit

2007-20 | Engine Oil Replacement Reminder Reset - Procedure 06

HR-V

2016-25 | Engine Oil Replacement Reminder Reset - Procedure 06

Insight

2010-14 | Engine Oil Replacement Reminder Reset - Procedure 06

2019-22 | Engine Oil Replacement Reminder Reset - Procedure 24

Odyssey (1)

2005-10 | Engine Oil Replacement Reminder Reset - Procedure 06

2012-15 | Engine Oil Replacement Reminder Reset - Procedure 10

2018-25 | Engine Oil Replacement Reminder Reset - Procedure 24

Passport

2019-25 | Engine Oil Replacement Reminder Reset - Procedure 13

Pilot (1)

2006-13 | Engine Oil Replacement Reminder Reset - Procedure 06

2014-23 | Engine Oil Replacement Reminder Reset - Procedure 06

2016-18 | Engine Oil Replacement Reminder Reset - Procedure 06

2019-25 | Engine Oil Replacement Reminder Reset - Procedure 19

Ridgeline

2007-08 | Engine Oil Replacement Reminder Reset - Procedure 04

2009-14 | Engine Oil Replacement Reminder Reset - Procedure 06

2017-25 | Engine Oil Replacement Reminder Reset - Procedure 03

S2000

2006-09 | Engine Oil Replacement Reminder Reset - Procedure 05

(1) Beginning with 2012 models, Honda no longers indicates whether the higher-end Multi-Information Display, that was previously only installed in the Touring models, continues to be available only in Touring. If you find a non-Touring model with a Multi-Information Display (identified by the steering wheel controls), use the Touring reset procedure. | (1) | Beginning with 2012 models, Honda no longers indicates whether the higher-end Multi-Information Display, that was previously only installed in the Touring models, continues to be available only in Touring. If you find a non-Touring model with a Multi-Information Display (identified by the steering wheel controls), use the Touring reset procedure.

(1) | Beginning with 2012 models, Honda no longers indicates whether the higher-end Multi-Information Display, that was previously only installed in the Touring models, continues to be available only in Touring. If you find a non-Touring model with a Multi-Information Display (identified by the steering wheel controls), use the Touring reset procedure.
````

## Chunk 8554: Engine Oil Replacement Reminder Reset - Procedure 01

- Title: Engine Oil Replacement Reminder Reset - Procedure 01
- Source path: `pages\11024.html`
- Chunk ID: `chunk_ea6a7088fbac`
- Images: `images\G00525201.png`, `images\G00572140.png`
- Duplicate sources: `pages\11508.html`, `pages\19989.html`, `pages\17656.html`

### Full Text

````text
# Engine Oil Replacement Reminder Reset - Procedure 01

- Turn ignition switch to ON (II).

- Press SELECT/RESET knob repeatedly until engine oil life indicator is displayed. See Fig 1 or Fig 2 .

- Press SELECT/RESET knob for 10 seconds, until the Engine oil life indicator and the Maintenance item codes blink, then release the button.

- Press SELECT/RESET knob again for 5 seconds. Maintenance items codes will disappear and engine oil life indicator will reset to 100%.
````

## Chunk 8555: Engine Oil Replacement Reminder Reset - Procedure 02

- Title: Engine Oil Replacement Reminder Reset - Procedure 02
- Source path: `pages\11025.html`
- Chunk ID: `chunk_720cb8dae1c7`
- Images: `images\G06608881.png`, `images\G06608882.png`
- Duplicate sources: `pages\11509.html`, `pages\19990.html`, `pages\17657.html`

### Full Text

````text
# Engine Oil Replacement Reminder Reset - Procedure 02

- The vehicle must be stopped to reset the display. If a required service is done and the display is not reset, or if the maintenance display is reset without doing the service, the system will not show the proper maintenance timing. This can lead to serious mechanical problems because there will be no accurate record of when the required maintenance is needed.

- The engine oil life and the maintenance items can be reset independently only with the HDS.

- Turn the ignition switch to ON (II).

- Push and release the Select/Reset knob repeatedly until the engine oil life indicator is displayed.

- Press and hold the Select/Reset knob for about 10 seconds. The information display shows the reset mode display. NOTE: If you are resetting the display when the engine oil life is more than 15%, make sure any maintenance items requiring service are done before resetting the display.

- Twist the Select/Reset knob to select OIL LIFE, the display will begin to blink.

- Push in on the Select/Reset knob to enter this selection, the OIL LIFE and the maintenance item codes will begin to blink.

- Press and hold the Select/Reset knob again for about 5 seconds. The maintenance item codes will disappear, and the engine oil life will reset to 100%.
````

## Chunk 8556: Engine Oil Replacement Reminder Reset - Procedure 03: Notes

- Title: Engine Oil Replacement Reminder Reset - Procedure 03: Notes
- Source path: `pages\11026.html`
- Chunk ID: `chunk_103f313d5325`
- Images: none
- Duplicate sources: `pages\11510.html`, `pages\19991.html`, `pages\17658.html`

### Full Text

````text
# Engine Oil Replacement Reminder Reset - Procedure 03: Notes

- The vehicle must be stopped to reset the Maintenance Minder.

- If a required service is done and the Maintenance Minder is not reset, or if the Maintenance Minder is reset without doing the service, the system will not show the proper maintenance timing. This can lead to serious mechanical problems because there will be no accurate record of when the next required maintenance is needed.

- The engine oil life and maintenance item(s) can be independently reset with the HDS.

- Turn the vehicle to the ON mode.

- Push the INFO button repeatedly until the engine oil life indicator is displayed.

- Press and hold the SEL/RESET button for about 10 seconds. The Maintenance Reset screen appears on the multi-information display. NOTE: If you are resetting the Maintenance Minder when the engine oil life is more than 15 %, make sure any maintenance item(s) requiring service are done before resetting the display. To cancel the Maintenance Reset mode, press the INFO button to select the Cancel, then press the SEL/RESET button.

- If you are resetting the Maintenance Minder when the engine oil life is more than 15 %, make sure any maintenance item(s) requiring service are done before resetting the display.

- To cancel the Maintenance Reset mode, press the INFO button to select the Cancel, then press the SEL/RESET button.

- Press the INFO button to select Reset, then press the SEL/RESET button. The "Reset Completed" message appears. The maintenance item code(s) will disappear and the engine oil life will be reset to 100%.
````

## Chunk 8557: Resetting Individual Maintenance Items

- Title: Resetting Individual Maintenance Items
- Source path: `pages\11027.html`
- Chunk ID: `chunk_eedcead511d9`
- Images: none
- Duplicate sources: `pages\11511.html`, `pages\19992.html`, `pages\17659.html`

### Full Text

````text
# Resetting Individual Maintenance Items

- Connect the HDS.

- Select GAUGES in the BODY ELECTRICAL with the HDS.

- Select ADJUSTMENT in the GAUGES with the HDS.

- Select MAINTENANCE INFORMATION in the ADJUSTMENT with the HDS.

- Select MAINTENANCE MINDER in the MAINTENANCE INFORMATION with the HDS.

- Select the individual maintenance item you wish to reset with the HDS.
````

## Chunk 8558: Engine Oil Replacement Reminder Reset - Procedure 04

- Title: Engine Oil Replacement Reminder Reset - Procedure 04
- Source path: `pages\11028.html`
- Chunk ID: `chunk_13f9be049bfc`
- Images: none
- Duplicate sources: `pages\11512.html`, `pages\19993.html`, `pages\17660.html`

### Full Text

````text
# Engine Oil Replacement Reminder Reset - Procedure 04

- Turn ignition switch to ON (II) position.

- Press SELECT button repeatedly until engine oil life display or service message is displayed.

- Press the RESET button for about 10 seconds. A "MAINT RESET" message will appear.

- Select appropriate answer - "MAINT RESET >N" (NO) or "MAINT RESET >Y" (YES) by pressing the select button. ">N" or ">Y" is displayed on the outside temperature display.

- Select the "MAINT RESET >Y" (YES), and press and hold RESET button again to reset engine oil life to 100%.
````

## Chunk 8559: Engine Oil Replacement Reminder Reset - Procedure 05

- Title: Engine Oil Replacement Reminder Reset - Procedure 05
- Source path: `pages\11029.html`
- Chunk ID: `chunk_3eea8c222eb9`
- Images: none
- Duplicate sources: `pages\11513.html`, `pages\19994.html`, `pages\17661.html`

### Full Text

````text
# Engine Oil Replacement Reminder Reset - Procedure 05

- The vehicle must be stopped to reset the display.

- If a required service is done and the display is not reset, or if the maintenance display is reset without doing the service, the system will not show the proper maintenance timing. This can lead to serious mechanical problems because there will be no accurate record of when the required maintenance is needed.

- The engine oil life and maintenance item(s) can be reset independently only with the HDS.

- Turn the ignition switch to ON (II).

- Press release the trip button repeatedly until the engine oil life indicator is displayed.

- Press and hold the trip button for about 10 seconds. The engine oil life indicator and the maintenance item code(s) will blink. NOTE: If you are resetting the display when the engine oil life is more than 15 %, make sure any maintenance item(s) requiring service are done before resetting the display.

The engine oil life indicator and the maintenance item code(s) will blink.

If you are resetting the display when the engine oil life is more than 15 %, make sure any maintenance item(s) requiring service are done before resetting the display.

- Press and hold the trip button for another 5 seconds. The maintenance item cods(s) will disappear, and the engine oil life will reset to "100".
````

## Chunk 8560: Engine Oil Replacement Reminder Reset - Procedure 06

- Title: Engine Oil Replacement Reminder Reset - Procedure 06
- Source path: `pages\11030.html`
- Chunk ID: `chunk_0766ceefbb95`
- Images: `images\G00530786.png`, `images\G00611083.png`, `images\G00611084.png`
- Duplicate sources: `pages\11514.html`, `pages\19995.html`, `pages\17662.html`

### Full Text

````text
# Engine Oil Replacement Reminder Reset - Procedure 06

- The vehicle must be stopped to reset the Maintenance Minder.

- If a required service is done and the Maintenance Minder is not reset, or if the Maintenance Minder is reset without doing the service, the system will not show the proper maintenance timing. This can lead to serious mechanical problems because there will be no accurate record of when the required maintenance is needed.

- The engine oil life and maintenance item(s) can be independently reset with the HDS.

- Turn the ignition switch to ON (II).

- If system message(s) are displayed, press the INFO button to cancel the display.

- Push the SEL/RESET button repeatedly until the engine oil life indicator is displayed.

- Press and hold the SEL/RESET button for about 10 seconds, the OIL LIFE RESET" mode display appears. NOTE: If you are resetting the Maintenance Minder when the engine oil life is more than 15 %, make sure any maintenance item(s) requiring service are done before resetting the display. To cancel the OIL LIFE RESET" mode, press the INFO button repeatedly until the CANCEL" indicator is displayed, then press the SEL/RESET button.

- If you are resetting the Maintenance Minder when the engine oil life is more than 15 %, make sure any maintenance item(s) requiring service are done before resetting the display.

- To cancel the OIL LIFE RESET" mode, press the INFO button repeatedly until the CANCEL" indicator is displayed, then press the SEL/RESET button.

- Press the INFO button repeatedly until the RESET" indicator is displayed, then press the SEL/RESET button. The maintenance item code(s) will disappear, and the engine oil life will reset to 100 %."
````

## Chunk 8561: Engine Oil Replacement Reminder Reset - Procedure 07

- Title: Engine Oil Replacement Reminder Reset - Procedure 07
- Source path: `pages\11031.html`
- Chunk ID: `chunk_3d15085fb14f`
- Images: none
- Duplicate sources: `pages\11515.html`, `pages\19996.html`, `pages\17663.html`

### Full Text

````text
# Engine Oil Replacement Reminder Reset - Procedure 07

- Turn ignition switch to ON (II) position.

- Press the SELECT button repeatedly until the engine oil life is displayed.

- Press the TRIP/RESET button for about 10 seconds. The engine oil life and the maintenance item codes will blink.

- Press the TRIP/RESET button again for 5 seconds. The maintenance item codes will disappear, and the engine oil life will reset to 100%.
````

## Chunk 8562: Engine Oil Replacement Reminder Reset - Procedure 08

- Title: Engine Oil Replacement Reminder Reset - Procedure 08
- Source path: `pages\11032.html`
- Chunk ID: `chunk_ff88019b7a20`
- Images: none
- Duplicate sources: `pages\11516.html`, `pages\19997.html`, `pages\17664.html`

### Full Text

````text
# Engine Oil Replacement Reminder Reset - Procedure 08

- Turn ignition switch to ON (II) position.

- Press the SEL/RESET button on the dashboard until you see the engine oil life display.

- Press and hold the SEL/RESET button for 10 seconds. The multi-information display will ask for a confirmation. If you are sure you want to reset the display, press SEL/RESET button to select OK. If you do not want to reset the display, press the INFO (ARROW) button to select CANCEL.

- If you are sure you want to reset the display, press SEL/RESET button to select OK.

- If you do not want to reset the display, press the INFO (ARROW) button to select CANCEL.
````

## Chunk 8563: Engine Oil Replacement Reminder Reset - Procedure 09

- Title: Engine Oil Replacement Reminder Reset - Procedure 09
- Source path: `pages\11033.html`
- Chunk ID: `chunk_bbc93712055e`
- Images: `images\G06949198.png`
- Duplicate sources: `pages\11517.html`, `pages\19998.html`, `pages\17665.html`

### Full Text

````text
# Engine Oil Replacement Reminder Reset - Procedure 09

- Turn the ignition switch to ON (II). NOTE: If system messages are displayed, press the INFO button to cancel the display.

- Push the ARROW buttons repeatedly until the engine oil life indicator is displayed. See Fig 1 .

- Select RESET with the ARROW buttons

- Press the SEL/RESET button for 10 seconds. The service code will disappear and the engine oil life display will return to 100%.

- To cancel the oil life reset mode, select CANCEL, then press the SEL/RESET button.
````

## Chunk 8564: Engine Oil Replacement Reminder Reset - Procedure 10

- Title: Engine Oil Replacement Reminder Reset - Procedure 10
- Source path: `pages\11034.html`
- Chunk ID: `chunk_3166a6ee1801`
- Images: `images\G00611087.png`
- Duplicate sources: `pages\11518.html`, `pages\19999.html`, `pages\17666.html`

### Full Text

````text
# Engine Oil Replacement Reminder Reset - Procedure 10

- The vehicle must be stopped to reset the Maintenance Minder.

- If a required service is done and the Maintenance Minder is not reset, or if the Maintenance Minder is reset without doing the service, the system will not show the proper maintenance timing. This can lead to serious mechanical problems because there will be no accurate record of when the required maintenance is needed.

- The engine oil life and the maintenance item(s) can be independently reset with the HDS.

- Turn the ignition switch to ON (II).

- Push the SEL/RESET knob repeatedly until the engine oil life indicator is displayed.

- Press and hold the SEL/RESET knob for about 10 seconds. The engine oil life indicator and the maintenance item code(s) will be blink, then release the knob. NOTE: If you are resetting the Maintenance Minder when the engine oil life is more than 15 %, make sure any maintenance item(s) requiring service are done before resetting the display.

- Push the SEL/RESET knob to select OIL LIFE, the display will begin to blink.

- Push in on the SEL/RESET knob to enter this selection, the OIL LIFE and the maintenance item code(s) will begin to blink.

- Press and hold the SEL/RESET knob for another 5 seconds. The maintenance item code(s) will disappear, and the engine oil life will reset to 100."
````

## Chunk 8565: Engine Oil Replacement Reminder Reset - Procedure 11

- Title: Engine Oil Replacement Reminder Reset - Procedure 11
- Source path: `pages\11035.html`
- Chunk ID: `chunk_c8ed7429321f`
- Images: `images\G00525200.png`
- Duplicate sources: `pages\11519.html`, `pages\20000.html`, `pages\17667.html`

### Full Text

````text
# Engine Oil Replacement Reminder Reset - Procedure 11

Maintenance Minder messages begin appearing on the i-MID when engine oil life is less than 15%. The system message indicator comes on along with the Maintenance Minder message.

- Turn the ignition switch to ON (II).

- Press the MENU button to go to VEHICLE INFORMATION. See Fig 1 .

- Select VEHICLE INFORMATION with the PLUS (+) button, then press the SOURCE button.

- Press the SOURCE button again to go to the MAINTENANCE INFO screen. The engine oil life appears on the i-MID.

- Select YES with the MINUS (-) button, then press the SOURCE button. The displayed maintenance items disappear, and the engine oil life display returns to 100%. Any maintenance items that are necessary for this vehicle at the next maintenance service will appear.

- To cancel the oil life reset mode, select No, then press the SOURCE button.
````

## Chunk 8566: Engine Oil Replacement Reminder Reset - Procedure 12

- Title: Engine Oil Replacement Reminder Reset - Procedure 12
- Source path: `pages\11036.html`
- Chunk ID: `chunk_df74a420f6ca`
- Images: none
- Duplicate sources: `pages\11520.html`, `pages\20001.html`, `pages\17668.html`

### Full Text

````text
# Engine Oil Replacement Reminder Reset - Procedure 12

- Set the power mode to ON.

- Press ARROWS button (right side of steering wheel) to select VEHICLE SETTINGS, then press the SEL/RESET button.

- Press ARROWS button until MAINTENANCE MINDER RESET appears on the display.

- Press the SEL/RESET button. The MAINTENANCE MINDER reset mode is displayed on the multi-information display.

- To Reset All Due Items At Once : Select ALL DUE ITEMS with the ARROWS button, then press the SEL/RESET button. The displayed maintenance items disappear. To Reset Each Item Separately : Select ITEM # ONLY with the ARROWS button, then press the SEL/RESET button. The displayed maintenance item (i.e. #) disappears. NOTE: To cancel the Maintenance Minder reset mode, select CANCEL, then press the SEL/ RESET button.

- To Reset All Due Items At Once : Select ALL DUE ITEMS with the ARROWS button, then press the SEL/RESET button. The displayed maintenance items disappear.

- To Reset Each Item Separately : Select ITEM # ONLY with the ARROWS button, then press the SEL/RESET button. The displayed maintenance item (i.e. #) disappears.

You can also reset the Maintenance Minder display using the audio/information screen. With the power mode in ON, press the SETTINGS button. Rotate to select: Vehicle Settings > Maintenance Info. > Maintenance Minder Reset.
````

## Chunk 8567: Engine Oil Replacement Reminder Reset - Procedure 13

- Title: Engine Oil Replacement Reminder Reset - Procedure 13
- Source path: `pages\11037.html`
- Chunk ID: `chunk_3b93b1f43ff6`
- Images: `images\G00525240.png`
- Duplicate sources: `pages\11521.html`, `pages\20002.html`, `pages\17669.html`

### Full Text

````text
# Engine Oil Replacement Reminder Reset - Procedure 13

- Turn the ignition switch to ON (II). NOTE: Models with the smart entry system have an ENGINE START/STOP button instead of an ignition switch.

- Press the DISPLAY/INFORMATION button repeatedly until the Wrench Icon appears. See Fig 1 .

- Press the ENTER button.

- Press and hold the ENTER button for about 10 seconds to enter the reset mode.

- Press the UP/DOWN ARROW buttons to select a maintenance item to reset, or to select ALL DUE ITEMS (You can also select CANCEL to end the process).

- Press the ENTER button to reset the selected item.
````

## Chunk 8568: Engine Oil Replacement Reminder Reset - Procedure 14

- Title: Engine Oil Replacement Reminder Reset - Procedure 14
- Source path: `pages\11038.html`
- Chunk ID: `chunk_39c67c2c38c4`
- Images: `images\G00525241.png`
- Duplicate sources: `pages\11522.html`, `pages\20003.html`, `pages\17670.html`

### Full Text

````text
# Engine Oil Replacement Reminder Reset - Procedure 14

- Turn ignition switch to ON (II). NOTE: Models with the smart entry system have an ENGINE START/STOP button instead of an ignition switch.

- Press and hold the SELECT/RESET knob for 10 seconds or more The information display shows the reset mode initial display. See Fig 1 .

- Select oil life with the SELECT/RESET knob.

- Press and hold the SELECT/RESET knob for a few seconds to enter the oil life reset mode.

- Press and hold the SELECT/RESET knob for five seconds or more. The displayed maintenance items disappear and the engine oil life display will return to 100%.
````

## Chunk 8569: Engine Oil Replacement Reminder Reset - Procedure 15

- Title: Engine Oil Replacement Reminder Reset - Procedure 15
- Source path: `pages\11039.html`
- Chunk ID: `chunk_baad90e9ff1c`
- Images: `images\G00525242.png`
- Duplicate sources: `pages\11523.html`, `pages\20004.html`, `pages\17671.html`

### Full Text

````text
# Engine Oil Replacement Reminder Reset - Procedure 15

- Turn ignition switch to ON (II). NOTE: Models with the smart entry system have an ENGINE START/STOP button instead of an ignition switch.

- If system messages are displayed, press the INFO button to cancel the display.

- Display the engine oil life by repeatedly pressing the SEL/RESET button. See Fig 1 .

- Press and hold the SEL/RESET button for 10 seconds or more. The oil life reset mode is displayed on the multi-information display.

- Select RESET with the INFORMATION button, then press the SEL/RESET button. The service code will disappear and the engine oil life display will return to 100%.

- To cancel the oil life reset mode, select CANCEL, then press the SEL/RESET button.
````

## Chunk 8570: Engine Oil Replacement Reminder Reset - Procedure 16

- Title: Engine Oil Replacement Reminder Reset - Procedure 16
- Source path: `pages\11040.html`
- Chunk ID: `chunk_e48f9ae09bcb`
- Images: `images\G00525243.png`
- Duplicate sources: `pages\11524.html`, `pages\20005.html`, `pages\17672.html`

### Full Text

````text
# Engine Oil Replacement Reminder Reset - Procedure 16

- The vehicle must be stopped to reset the Maintenance Minder.

- If a required service is done and the Maintenance Minder is not reset, or if the Maintenance Minder is reset without doing the service, the system will not show the proper maintenance timing. This can lead to serious mechanical problems because there will be no accurate record of when the next required maintenance is needed.

- Turn ignition switch to ON (II). NOTE: Models with the smart entry system have an ENGINE START/STOP button instead of an ignition switch.

- In the Multi-Information Display (MID), go to the Maintenance Info. group. > Customized Features.

- Press and hold the RESET button. The oil life reset mode is displayed on the MID. See Fig 1 .

- Select Reset with the INFORMATION button, then push the RESET button. The displayed maintenance items disappear, and the engine oil life display returns to 100%.

- To cancel the oil life reset mode, select CANCEL, then press the RESET button.
````

## Chunk 8571: Engine Oil Replacement Reminder Reset - Procedure 17: Notes

- Title: Engine Oil Replacement Reminder Reset - Procedure 17: Notes
- Source path: `pages\11041.html`
- Chunk ID: `chunk_6890717d8714`
- Images: none
- Duplicate sources: `pages\11525.html`, `pages\20006.html`, `pages\17673.html`

### Full Text

````text
# Engine Oil Replacement Reminder Reset - Procedure 17: Notes
````

## Chunk 8572: Information Display Select/Reset Knob Method

- Title: Information Display Select/Reset Knob Method
- Source path: `pages\11042.html`
- Chunk ID: `chunk_2cdb731c30dc`
- Images: none
- Duplicate sources: `pages\11526.html`, `pages\20007.html`, `pages\17674.html`

### Full Text

````text
# Information Display Select/Reset Knob Method

- Turn ignition switch to ON (II).

- Press SELECT/RESET knob (right side of instrument cluster) repeatedly until engine oil life indicator is displayed.

- Press SELECT/RESET knob for 10 seconds. Engine oil life indicator and the maintenance item codes will blink.

- Press SELECT/RESET knob again for 5 seconds. Maintenance items codes will disappear and engine oil life indicator will reset to "100%"
````

## Chunk 8573: Multi-Information Display Screen Method

- Title: Multi-Information Display Screen Method
- Source path: `pages\11043.html`
- Chunk ID: `chunk_cd6b8d0299a5`
- Images: none
- Duplicate sources: `pages\11527.html`, `pages\20008.html`, `pages\17675.html`

### Full Text

````text
# Multi-Information Display Screen Method

- Press the engine start/stop button to select the ON mode.

- Press INFO button (right-side steering wheel controls) to select VEHICLE SETTINGS, then press the SEL/RESET button.

- Press the INFO button until MAINTENANCE RESET appears on the display, then press the SEL/RESET button. The oil life reset mode is displayed on the multi-information display. NOTE: To cancel the oil life mode, press the INFO button to select CANCEL, then press the SEL/RESET button.

- Press the INFO button to select RESET, then press the SEL/RESET button. The maintenance item codes will disappear, and the engine oil life will reset to 100%.
````

## Chunk 8574: Audio/Infomation Screen Method

- Title: Audio/Infomation Screen Method
- Source path: `pages\11044.html`
- Chunk ID: `chunk_183d2dfe7249`
- Images: none
- Duplicate sources: `pages\11528.html`, `pages\20009.html`, `pages\17676.html`

### Full Text

````text
# Audio/Infomation Screen Method

- Turn the ignition switch to ON (II), or press the engine start/stop button to select the ON mode

- Press the SETTINGS button, then rotate the Selector Knob to select vehicle settings, then select maintence items.

- Follow the screen prompts to reset the engine oil life.
````

## Chunk 8575: Engine Oil Replacement Reminder Reset - Procedure 18: Notes

- Title: Engine Oil Replacement Reminder Reset - Procedure 18: Notes
- Source path: `pages\11045.html`
- Chunk ID: `chunk_d4760220f06c`
- Images: none
- Duplicate sources: `pages\11529.html`, `pages\20010.html`, `pages\17677.html`

### Full Text

````text
# Engine Oil Replacement Reminder Reset - Procedure 18: Notes
````

## Chunk 8576: With Information Display

- Title: With Information Display
- Source path: `pages\11046.html`
- Chunk ID: `chunk_baabe7d521b5`
- Images: none
- Duplicate sources: `pages\11530.html`, `pages\20011.html`, `pages\17678.html`

### Full Text

````text
# With Information Display

- Turn the ignition switch to the ON (II) position.

- Press the SELECT/RESET knob (on instrument cluster - right side) repeatedly until the engine oil life is displayed

- Press and hold the SELECT/RESET knob for about 10 seconds. The engine oil life and the maintenance item codes will blink to show it is in reset mode.

- If you wish to reset all the maintenance items shown on the display, press and hold the SEL/RESET knob for 5 seconds or more. If you reset each maintenance item individually, select an item (complete list of maintenance main items and sub items) you wish to reset by rotating the SEL/RESET knob, and press and hold the knob for 5 seconds or more.

- The maintenance item codes will disappear and the engine oil life will reset to 100%.
````

## Chunk 8577: With Multi-Information Display

- Title: With Multi-Information Display
- Source path: `pages\11047.html`
- Chunk ID: `chunk_71ae0e53af32`
- Images: `images\G00561384.png`
- Duplicate sources: `pages\11531.html`, `pages\20012.html`, `pages\17679.html`

### Full Text

````text
# With Multi-Information Display

- Turn the vehicle to the ON mode.

- If system messages are displayed, press the INFOMATION switch (see Fig 1 ) or Audio Remote/Multi-Information Display Switch to cancel the display until the MAINTENANCE MINDER icon is displayed, then press the SOURCE/ENTER button.

- Display shows the remaining engine oil life, and then press and hold the SOURCE/ENTER button for 10 seconds or more. The MAINTENANCE RESET mode appears on the multi-information display. NOTE: To cancel the MAINTENANCE RESET mode, press the Audio Remote/Multi-Information Display Switch to select CANCEL, then press the SOURCE/ENTER button.

- If you wish to reset all the maintenance items shown on the display, select "All Due Items" by pressing the Audio Remote/Multi-Information Display Switch and press the SOURCE/ENTER button. If you reset each maintenance item individually, select an item (complete list of maintenance main items and sub items) you wish to reset by pressing the Audio Remote/Multi-Information Display Switch and press the SOURCE/ENTER button.

- The maintenance item codes will disappear, and the engine oil life will reset to 100%.
````

## Chunk 8578: Engine Oil Replacement Reminder Reset - Procedure 19

- Title: Engine Oil Replacement Reminder Reset - Procedure 19
- Source path: `pages\11048.html`
- Chunk ID: `chunk_a58ae4f490de`
- Images: `images\G00611085.png`, `images\G00611086.png`
- Duplicate sources: `pages\11532.html`, `pages\20013.html`, `pages\17680.html`

### Full Text

````text
# Engine Oil Replacement Reminder Reset - Procedure 19

- The vehicle must be stopped to reset the Maintenance Minder.

- If a required service is done and the Maintenance Minder is not reset, or if the Maintenance Minder is reset without doing the service, the system will not show the proper maintenance timing. This can lead to serious mechanical problems because there will be no accurate record of when the required maintenance is needed.

- You can reset all maintenance items by batch, or you can select and reset each maintenance item individually on the display.

- The engine oil life and maintenance item(s) can be independently reset with the HDS.

- Turn the vehicle to the ON mode.

- Press the HOME button and select "Maintenance" application by pushing repeatedly the Audio Remote/Multi-Information Display switch. Press and hold the ENTER button more than 10 seconds, and then display will change to Maintenance mode. Select "Oil Life" by pushing the Audio Remote/Multi-Information Display switch and press and hold the ENTER button more than 10 seconds to show the reset mode.

- If you reset all the maintenance items shown on the display, select "All Due Items" by pressing the Audio Remote/Multi-Information Display switch and press the ENTER button. If you reset each maintenance item individually, select an item (complete list of maintenance main item(s) and sub item(s) ) you wish to reset by pressing the Audio Remote/Multi-Information Display switch and press the ENTER button. NOTE: If you are resetting the Maintenance Minder when the engine oil life is more than 15 %, make sure any maintenance item(s) requiring service are done before resetting the display. To cancel the reset mode, select "Cancel," then push the ENTER button.

- If you are resetting the Maintenance Minder when the engine oil life is more than 15 %, make sure any maintenance item(s) requiring service are done before resetting the display.

- To cancel the reset mode, select "Cancel," then push the ENTER button.

- "Reset Completed" appears on the display and maintenance item code(s) will disappear. The engine oil life will reset to "100 %."
````

## Chunk 8579: Engine Oil Replacement Reminder Reset - Procedure 20

- Title: Engine Oil Replacement Reminder Reset - Procedure 20
- Source path: `pages\11049.html`
- Chunk ID: `chunk_49180eaa9e79`
- Images: none
- Duplicate sources: `pages\11533.html`, `pages\20014.html`, `pages\17681.html`

### Full Text

````text
# Engine Oil Replacement Reminder Reset - Procedure 20

- Connect the Honda Diagnostic System (HDS) to the data link connector (DLC).

- Turn the vehicle to the ON mode.

- Make sure the HDS communicates with the vehicle and the powertrain control module (PCM). If it doesn't communicate, troubleshoot the DLC circuit.

- Select GAUGES in BODY ELECTRICAL with the HDS.

- Select ADJUSTMENT in GAUGES.

- Select MAINTENANCE INFORMATION in ADJUSTMENT.

- Select MAINTENANCE MINDER in MAINTENANCE INFORMATION.

- Select the individual maintenance item you wish to reset.
````

## Chunk 8580: Engine Oil Replacement Reminder Reset - Procedure 21

- Title: Engine Oil Replacement Reminder Reset - Procedure 21
- Source path: `pages\11050.html`
- Chunk ID: `chunk_200cf0997113`
- Images: `images\G00572139.png`
- Duplicate sources: `pages\11534.html`, `pages\20015.html`, `pages\17682.html`

### Full Text

````text
# Engine Oil Replacement Reminder Reset - Procedure 21

- The vehicle must be stopped to reset the Maintenance Minder.

- If a required service is done and the Maintenance Minder is not reset, or if the Maintenance Minder is reset without doing the service, the system will not show the proper maintenance timing. This can lead to serious mechanical problems because there will be no accurate record of when the required maintenance is needed.

- With the vehicle stationary and the power mode ON, press the INFO button and then select the smart maintenance icon (wrench icon) using the right/left buttons. See Fig 1 .

- After the smart maintenance screen is shown, press and hold the ENTER button for 10 seconds. The reset mode screen will appear.

- Select the item you want to reset by pressing the up/down buttons, and then press the ENTER button. There are "All Due Items", "Item 1 only", "Item 2 only", and so on. NOTE: If you are resetting the Maintenance Minder, make sure that any maintenance items to service are done. To cancel the "Maintenance Reset" mode, press the up/down buttons to select the "Cancel," and then press the ENTER button.

- If you are resetting the Maintenance Minder, make sure that any maintenance items to service are done.

- To cancel the "Maintenance Reset" mode, press the up/down buttons to select the "Cancel," and then press the ENTER button.

- The "Reset Completed" message will appear. The maintenance items are reset and the maintenance item code(s) will disappear.
````

## Chunk 8581: Engine Oil Replacement Reminder Reset - Procedure 22

- Title: Engine Oil Replacement Reminder Reset - Procedure 22
- Source path: `pages\11051.html`
- Chunk ID: `chunk_bf0e2dbc2d84`
- Images: `images\G00572141.png`
- Duplicate sources: `pages\11535.html`, `pages\20016.html`, `pages\17683.html`

### Full Text

````text
# Engine Oil Replacement Reminder Reset - Procedure 22

- The vehicle must be stopped to reset the Maintenance Minder.

- If a required service is done and the Maintenance Minder is not reset, or if the Maintenance Minder is reset without doing the service, the system will not show the proper maintenance timing. This can lead to serious mechanical problems because there will be no accurate record of when the required maintenance is needed.

- You can reset all maintenance items by batch, or you can select and reset each maintenance item individually on the display.

- The engine oil life and maintenance item(s) can be independently reset with the HDS.

- Turn the vehicle to the ON mode.

- Press the HOME button and select "Maintenance" application by pushing repeatedly the Audio Remote/Multi-Information Display switch. See Fig 1 . Press and hold the ENTER button more than 10 seconds, and then display will change to Maintenance mode. Select "Oil Life" by pushing the Audio Remote/Multi-Information Display switch and press and hold the ENTER button more than 10 seconds to show the reset mode.

- If you wish to reset all the maintenance items shown on the display, select "All Due Items" by pressing the Audio Remote/Multi-Information Display switch and press the ENTER button. If you reset each maintenance item individually, select an item (complete list of maintenance main item(s) and sub item(s)) you wish to reset by pressing the Audio Remote/Multi-Information Display switch and press the ENTER button. NOTE: If you are resetting the Maintenance Minder when the engine oil life is more than 15 %, make sure any maintenance item(s) requiring service are done before resetting the display. To cancel the reset mode, select "Cancel," then push the ENTER button.

- If you are resetting the Maintenance Minder when the engine oil life is more than 15 %, make sure any maintenance item(s) requiring service are done before resetting the display.

- To cancel the reset mode, select "Cancel," then push the ENTER button.

- "Reset Completed" appears on the display and maintenance item code(s) will disappear. The engine oil life will reset to "100 %."
````

## Chunk 8582: Engine Oil Replacement Reminder Reset - Procedure 23

- Title: Engine Oil Replacement Reminder Reset - Procedure 23
- Source path: `pages\11052.html`
- Chunk ID: `chunk_89fd1868dc2a`
- Images: `images\G00611080.png`
- Duplicate sources: `pages\11536.html`, `pages\20017.html`, `pages\17684.html`

### Full Text

````text
# Engine Oil Replacement Reminder Reset - Procedure 23

- The vehicle must be stopped to reset the Maintenance Minder.

- If a required service is done and the Maintenance Minder is not reset, or if the Maintenance Minder is reset without doing the service, the system will not show the proper maintenance timing. This can lead to serious mechanical problems because there will be no accurate record of when the required maintenance is needed.

- You can reset all maintenance items by batch, or you can select and reset each maintenance item individually on the display.

- Turn the vehicle to the ON mode.

- Refer to the "How to access the current engine oil life," display the engine oil life on the multi-information display.

- Press and hold the multi-function steering wheel controller for 10 seconds or more to show the reset mode.

- If you reset all the maintenance items shown on the display "A23 (for example)", select "All due items" by rolling the multi-function steering wheel controller and press it. If you reset each maintenance item individually, select an item (complete list of maintenance main item(s) and sub item(s)) you wish to reset by rolling the multi-function steering wheel controller and press it. NOTE: If you are resetting the Maintenance Minder when the engine oil life is more than 15 %, make sure any maintenance item(s) requiring service are done before resetting the display. To cancel the reset mode, toggle the multi-function steering wheel controller to the left.

- If you are resetting the Maintenance Minder when the engine oil life is more than 15 %, make sure any maintenance item(s) requiring service are done before resetting the display.

- To cancel the reset mode, toggle the multi-function steering wheel controller to the left.

- "Reset completed" appears on the display and maintenance item code(s) will disappear. The engine oil life will reset to "100 %."
````

## Chunk 8583: Engine Oil Replacement Reminder Reset - Procedure 24

- Title: Engine Oil Replacement Reminder Reset - Procedure 24
- Source path: `pages\11053.html`
- Chunk ID: `chunk_6151c708faee`
- Images: `images\G00611081.png`, `images\G00611082.png`
- Duplicate sources: `pages\11537.html`, `pages\20018.html`, `pages\17685.html`

### Full Text

````text
# Engine Oil Replacement Reminder Reset - Procedure 24

- The vehicle must be stopped to reset the Maintenance Minder.

- If a required service is done and the Maintenance Minder is not reset, or if the Maintenance Minder is reset without doing the service, the system will not show the proper maintenance timing. This can lead to serious mechanical problems because there will be no accurate record of when the required maintenance is needed.

- You can reset all maintenance items by batch, or you can select and reset each maintenance item individually on the display.

- The engine oil life and maintenance item(s) can be independently reset with the HDS.

- Turn the vehicle to the ON mode.

- If system message(s) are displayed to the multi-Information display, press the Left Selector Wheel to cancel the display. Press the HOME button, then select the "Maintenance" by rolling the Left Selector Wheel, and press that wheel.

- Display shows the remaining engine oil life, and then press the Left Selector Wheel for 10 seconds or more. The "Maintenance Reset" mode appears on the multi-information display. NOTE: If you are resetting the Maintenance Minder when the engine oil life is more than 15 %, make sure any maintenance item(s) requiring service are done before resetting the display. To cancel the "Maintenance Reset" mode, rolling the Left Selector Wheel to select the "Cancel", and press that wheel.

- If you are resetting the Maintenance Minder when the engine oil life is more than 15 %, make sure any maintenance item(s) requiring service are done before resetting the display.

- To cancel the "Maintenance Reset" mode, rolling the Left Selector Wheel to select the "Cancel", and press that wheel.

- If you reset all the maintenance items shown on the display "A23 (for example)", select "All Due Items" by rolling the Left Selector Wheel, and press that wheel. If you reset each maintenance item individually, select an item (complete list of maintenance main item(s) and sub item(s)) you wish to reset by rolling the Left Selector Wheel, and press that wheel.

- "Reset Completed" appears on the display and maintenance item code(s) will disappear. The engine oil life will reset to "100 %."
````

## Chunk 8584: Maintenance Service Reminder: Notes

- Title: Maintenance Service Reminder: Notes
- Source path: `pages\11054.html`
- Chunk ID: `chunk_453dbe8c9b61`
- Images: none
- Duplicate sources: `pages\11538.html`, `pages\20019.html`, `pages\17686.html`

### Full Text

````text
# Maintenance Service Reminder: Notes

Model & Year | Reset Procedure

Accord

1982-85 | Maintenance Service Reminder Reset - Procedure 05

1991-97 | Maintenance Service Reminder Reset - Procedure 01

1998-05 | Maintenance Service Reminder Reset - Procedure 02

Civic

1996-00 | Maintenance Service Reminder Reset - Procedure 02

2001-05 | Maintenance Service Reminder Reset - Procedure 03

CR-V

1998-01 | Maintenance Service Reminder Reset - Procedure 01

2002-05 | Maintenance Service Reminder Reset - Procedure 02

Element

2003-05 | Maintenance Service Reminder Reset - Procedure 03

Insight

2000-05 | Maintenance Service Reminder Reset - Procedure 04

Odyssey

1996-97 | Maintenance Service Reminder Reset - Procedure 01

1998-04 | Maintenance Service Reminder Reset - Procedure 02

Pilot

2003-06 | Maintenance Service Reminder Reset - Procedure 02

Prelude

1998-01 | Maintenance Service Reminder Reset - Procedure 01

S2000

2000-05 | Maintenance Service Reminder Reset - Procedure 02
````

## Chunk 8585: Maintenance Service Reminder Reset - Procedure 01

- Title: Maintenance Service Reminder Reset - Procedure 01
- Source path: `pages\11055.html`
- Chunk ID: `chunk_b779eb5f1a2c`
- Images: `images\G98I64764.gif`
- Duplicate sources: `pages\11539.html`, `pages\20020.html`, `pages\17687.html`

### Full Text

````text
# Maintenance Service Reminder Reset - Procedure 01

- At each 7500 mile service interval, the MAINTENANCE REQUIRED light will change from Green to Yellow. If service is not performed (and light is not reset), the MAINTENANCE REQUIRED light will change from Yellow to Red.

- When service has been completed, reset MAINTENANCE REQUIRED reminder light. To reset reminder light, turn ignition off. Insert ignition key in slot provided to the right of tachometer (or beside the indicator). See Fig 1 .
````

## Chunk 8586: Maintenance Service Reminder Reset - Procedure 02

- Title: Maintenance Service Reminder Reset - Procedure 02
- Source path: `pages\11056.html`
- Chunk ID: `chunk_7688d3ff3419`
- Images: none
- Duplicate sources: `pages\11540.html`, `pages\20021.html`, `pages\17688.html`

### Full Text

````text
# Maintenance Service Reminder Reset - Procedure 02

To reset MAINT REQ'D indicator light, turn ignition switch to OFF position. Push and hold the SELECT/RESET button and turn ignition switch to ON (II) position. Continue to hold button for more than 10 seconds or until MAINT REQ'D light goes out.
````

## Chunk 8587: Maintenance Service Reminder Reset - Procedure 03

- Title: Maintenance Service Reminder Reset - Procedure 03
- Source path: `pages\11057.html`
- Chunk ID: `chunk_e5270b2fe659`
- Images: none
- Duplicate sources: `pages\11541.html`, `pages\20022.html`, `pages\17689.html`

### Full Text

````text
# Maintenance Service Reminder Reset - Procedure 03

- For the first 8000 miles after maintenance required indicator is reset, the MAINT REQ'D indicator light illuminates when the ignition is turned on, then will go out after 2 seconds. When mileage is 8000-10, 000 miles, the MAINT REQ'D reminder light will illuminate for 2 seconds, then blink for 10 seconds, and then go out. When mileage exceeds 10, 000 miles, MAINT REQ'D indicator light illuminates and stays on while ignition switch is in ON (II) position.

- To reset the MAINT REQ'D indicator light, turn ignition switch to OFF position. Press and hold the SELECT/RESET button. While still holding button, turn ignition switch to ON position, with engine off. Hold SELECT/RESET button for about 10 seconds until indicator resets.

- If MAINT REQ'D reminder light does not reset, ensure headlights, parking lights, or both are turned off when resetting reminder light. The MAINT REQ'D indicator cannot be reset if any of these lights are on. If vehicle is equipped with daytime running lights and lights come on when ignition switch is turned to ON (II) position, daytime running lights must be disabled before indicator light can be reset.
````

## Chunk 8588: Maintenance Service Reminder Reset - Procedure 04

- Title: Maintenance Service Reminder Reset - Procedure 04
- Source path: `pages\11058.html`
- Chunk ID: `chunk_c6cee50045cd`
- Images: none
- Duplicate sources: `pages\11542.html`, `pages\20023.html`, `pages\17690.html`

### Full Text

````text
# Maintenance Service Reminder Reset - Procedure 04

- When distance driven since maintenance required indicator was reset is 6000 miles, the MAINT REQ'D reminder light will start to blink. After exceeding 7500 miles without having scheduled maintenance performed and MAINT REQ'D reminder light reset, light will remain on until it is reset.

- To reset the light, turn ignition switch to OFF position. Press and hold TRIP button, located on lower right side of instrument cluster. While still holding TRIP button, turn ignition switch to ON position with engine off. Hold button for about 10 seconds until indicator resets.
````

## Chunk 8589: Maintenance Service Reminder Reset - Procedure 05

- Title: Maintenance Service Reminder Reset - Procedure 05
- Source path: `pages\11059.html`
- Chunk ID: `chunk_44c72546f168`
- Images: none
- Duplicate sources: `pages\11543.html`, `pages\20024.html`, `pages\17691.html`

### Full Text

````text
# Maintenance Service Reminder Reset - Procedure 05

Oil, filter and service interval indicator flags/lights activate every 7500 miles. To reset indicators, insert ignition key into appropriate slot below glowing indicator flags/lights at lower right corner of instrument cluster. Push key in until reminder window changes from Red to Green.
````

## Chunk 8590: Tire Pressure Monitor System Reminder: Notes

- Title: Tire Pressure Monitor System Reminder: Notes
- Source path: `pages\11060.html`
- Chunk ID: `chunk_88c9e75b9fbe`
- Images: none
- Duplicate sources: `pages\11544.html`, `pages\20025.html`, `pages\17648.html`

### Full Text

````text
# Tire Pressure Monitor System Reminder: Notes

Model & Year | Reset Procedure

Accord

2008-12 | (1) TPMS Reminder Reset - Procedure 01

2013-16 | (2) TPMS Reminder Reset - Procedure 03

2017-25 | (2) TPMS Reminder Reset - Procedure 07

Civic

2006-13 | (1) TPMS Reminder Reset - Procedure 01

2014-16 | TPMS Reminder Reset - Procedure 04

2017-25 | (2) TPMS Reminder Reset - Procedure 08

Clarity

2017-21 | (2) TPMS Reminder Reset - Procedure 09

Crosstour

2010-15 | (1) TPMS Reminder Reset - Procedure 01

CR-V

2007-13 | (1) TPMS Reminder Reset - Procedure 01

2014 | (2) TPMS Reminder Reset - Procedure 03

2015-16 | TPMS Reminder Reset - Procedure 05

2017-25 | (2) TPMS Reminder Reset - Procedure 09

CR-Z

2011-15 | (1) TPMS Reminder Reset - Procedure 01

2016 | TPMS Reminder Reset - Procedure 06

Element

2007-11 | (1) TPMS Reminder Reset - Procedure 01

Fit

2007-13 | (1) TPMS Reminder Reset - Procedure 01

2015-24 | (2) TPMS Reminder Reset - Procedure 03

Fit EV

2013-14 | (1) TPMS Reminder Reset - Procedure 01

HR-V

2016 | TPMS Reminder Reset - Procedure 02

2017-25 | (2) TPMS Reminder Reset - Procedure 03

Insight

2010-14 | (1) TPMS Reminder Reset - Procedure 01

Odyssey (Except Touring)

2005-06 | TPMS Reminder Reset - Procedure 02

2007-10 | (1) TPMS Reminder Reset - Procedure 01

Odyssey (Touring)

2007-10 | TPMS Reminder Reset - Procedure 02

Odyssey (All Models)

2011-25 | (1) TPMS Reminder Reset - Procedure 01

Pilot

2005-21 | TPMS Reminder Reset - Procedure 02

Prologue

2024-25 | (1) TPMS Reminder Reset - Procedure 09

Ridgeline

2006-25 | TPMS Reminder Reset - Procedure 02

S2000

2007-09 | (1) TPMS Reminder Reset - Procedure 01

(1) There are no TPMS reset procedures required for these models. Ensure tires are inflated to recommend pressure. Tire pressure sensor IDs need to be memorized if new sensor or TPMS control unit is installed. (2) This vehicle is equipped with an Indirect TPMS that does not use tire-mounted pressure sensors. | (1) | There are no TPMS reset procedures required for these models. Ensure tires are inflated to recommend pressure. Tire pressure sensor IDs need to be memorized if new sensor or TPMS control unit is installed. | (2) | This vehicle is equipped with an Indirect TPMS that does not use tire-mounted pressure sensors.

(1) | There are no TPMS reset procedures required for these models. Ensure tires are inflated to recommend pressure. Tire pressure sensor IDs need to be memorized if new sensor or TPMS control unit is installed.

(2) | This vehicle is equipped with an Indirect TPMS that does not use tire-mounted pressure sensors.
````

## Chunk 8591: TPMS Reminder Reset - Procedure 01

- Title: TPMS Reminder Reset - Procedure 01
- Source path: `pages\11061.html`
- Chunk ID: `chunk_4ebd09740742`
- Images: `images\G05794879.png`, `images\G05794880.png`
- Duplicate sources: `pages\11545.html`, `pages\20026.html`, `pages\17649.html`

### Full Text

````text
# TPMS Reminder Reset - Procedure 01

All four tire pressure sensor IDs must be memorized to the TPMS control unit whenever you do any of these actions:

- Replace the TPMS control unit.

- Replace the tire pressure sensor

- Substitute a known-good wheel with tire pressure sensor

When doing a tire rotation, memorizing the sensors in not needed.

Memorizing The Tire Pressure Sensor IDs

- Crosstour, CR-V (2007-12), CR-Z, Fit (2009 & later): Only use the TPMS Sensor Activation Tool ATEQ VT55

- All Other Models: Can use either TPMS Sensor Initializer Tool AKS0620006 or TPMS Sensor Activation Tool Bartec Wheelrite Tech 300-J-48714

- With the ignition switch in LOCK (0), connect the HDS to the data link connector (DLC) located under the driver's side of the dashboard.

- Turn the ignition switch to ON (II)

- Make sure the HDS communicates with the vehicle and the TPMS control unit. If it doesn't, troubleshoot the DLC circuit.

- Select Sensor ID Learning from the mode menu on the HDS.

- Follow HDS screen prompts to turn on the TPMS sensor initializer tool. NOTE: On the TPMS Sensor Initializer Tool (AKS0620006), verify that the power switch (B) is in the "Low" position. See Fig 1 . If the power switch is in the "High" position, more than one sensor or sensors on other vehicles may be activated. Make sure the power switch is in the "Low" position.

- Hold the TPMS sensor initializer tool near one wheel, memorize the pressure sensor ID by following the screen prompts on the HDS. See Fig 2 . NOTE: If you turn the ignition switch to LOCK (0) before memorizing all four sensor IDs, the memorizing ID is cancelled. If more than one sensor ID is displayed on the HDS, verify that the power switch is in the "LOW" position, the vehicle has not been driven for 5 minutes, and there are no other vehicles within 10 ft (3 m). See the HDS Help menu for specific instructions.

- If you turn the ignition switch to LOCK (0) before memorizing all four sensor IDs, the memorizing ID is cancelled.

- If more than one sensor ID is displayed on the HDS, verify that the power switch is in the "LOW" position, the vehicle has not been driven for 5 minutes, and there are no other vehicles within 10 ft (3 m).

- See the HDS Help menu for specific instructions.

- Repeat step 6 for each wheel until all four sensor IDs are memorized. When all four IDs are memorized, the low tire pressure indicator blinks

- Turn the ignition switch to LOCK (0).

- Disconnect the HDS from the DLC.

- Test-drive the vehicle at 28 mph (45 km/h) or more for at least 1 minute.

- Make sure the low tire pressure indicator does not blink.

- Make sure the tires are inflated to the specified tire pressure listed on the doorjamb sticker.
````

## Chunk 8592: TPMS Reminder Reset - Procedure 02: Notes

- Title: TPMS Reminder Reset - Procedure 02: Notes
- Source path: `pages\11062.html`
- Chunk ID: `chunk_fa181f67c80d`
- Images: none
- Duplicate sources: `pages\11546.html`, `pages\20027.html`, `pages\17692.html`

### Full Text

````text
# TPMS Reminder Reset - Procedure 02: Notes
````

## Chunk 8593: Memorizing a Sensor ID Automatically

- Title: Memorizing a Sensor ID Automatically
- Source path: `pages\11063.html`
- Chunk ID: `chunk_778a26567191`
- Images: none
- Duplicate sources: `pages\11547.html`, `pages\20028.html`, `pages\17693.html`

### Full Text

````text
# Memorizing a Sensor ID Automatically

After rotating the tires or replacing a tire pressure sensor, drive the vehicle for at least 40 seconds at a speed of 15 mph (24 km/h) or more, and all the sensor IDs will be memorized automatically.
````

## Chunk 8594: Memorizing a Sensor ID with the HDS

- Title: Memorizing a Sensor ID with the HDS
- Source path: `pages\11064.html`
- Chunk ID: `chunk_70c67eb5c578`
- Images: none
- Duplicate sources: `pages\11548.html`, `pages\20029.html`, `pages\17694.html`

### Full Text

````text
# Memorizing a Sensor ID with the HDS

The HDS can memorize the ID of a new tire pressure sensor or a previously memorized ID.

- With the ignition switch OFF, connect the HDS to the data link connector (DLC) located under the left side of the dashboard.

- Turn the ignition switch ON (II), and memorize the ID of the tire pressure sensor by following the screen prompts on the HDS. NOTE: See the HDS Help menu for specific instructions. When replacing the TPMS control unit, use the HDS to memorize IDs. After the IDs are memorized, reduce the pressure in all four tires to less than the appropriate specification, and check to see that the four tire indicators come on.an indirect TPMS that doesnt use tire pressure sensors mounted inside the tires. It uses the existing VSA wheel speed sensors to monitor and compare tire characteristics while driving.

- See the HDS Help menu for specific instructions.

- When replacing the TPMS control unit, use the HDS to memorize IDs.

- After the IDs are memorized, reduce the pressure in all four tires to less than the appropriate specification, and check to see that the four tire indicators come on.an indirect TPMS that doesnt use tire pressure sensors mounted inside the tires. It uses the existing VSA wheel speed sensors to monitor and compare tire characteristics while driving.

- Turn the vehicle to the OFF (LOCK) mode.
````

## Chunk 8595: TPMS Reminder Reset - Procedure 03: Notes

- Title: TPMS Reminder Reset - Procedure 03: Notes
- Source path: `pages\11065.html`
- Chunk ID: `chunk_16c4c75c2d7a`
- Images: none
- Duplicate sources: `pages\11549.html`, `pages\20030.html`, `pages\17695.html`

### Full Text

````text
# TPMS Reminder Reset - Procedure 03: Notes

This vehicle is equipped with an indirect TPMS that doesn't use tire pressure sensors mounted inside the tires. It uses the existing VSA wheel speed sensors to monitor and compare tire characteristics while driving.

TPMS calibration is required after performing any of the following actions:

- Adjusting tire pressures

- Rotating the tires

- Replacing the tires

- Updating/replacing the VSA modulator-control unit

Calibration begins when TPMS switch is pressed or Calibration is selected through the Multi-information display (MID). The process finishes automatically as the customer drives the vehicle. This takes about 30 minutes of cumulative driving at 30 to 60 mph.
````

## Chunk 8596: Calibration - Models With TPMS Switch

- Title: Calibration - Models With TPMS Switch
- Source path: `pages\11066.html`
- Chunk ID: `chunk_b8746cba16fe`
- Images: none
- Duplicate sources: `pages\11550.html`, `pages\20031.html`, `pages\17696.html`

### Full Text

````text
# Calibration - Models With TPMS Switch

- Make sure the tires are inflated to the specified tire pressure listed on the doorjamb label. Vehicle must be stopped with the transmission in neutral (M/T) or P or N (A/T, CVT).

- Turn the ignition switch to ON (II), or press the engine start/stop button to select the ON mode.

- Press the TPMS switch (lower dash, left of steering wheel) for 3 seconds.

- When the calibration successfully begins, the TPMS indicator (instrument cluster, center left) blinks twice.

- Calibration is completed after driving 31 to 62 mph (50 to 100 km/h), steadily without much acceleration or deceleration for about 30 minutes.
````

## Chunk 8597: Calibration - Models Without TPMS Switch

- Title: Calibration - Models Without TPMS Switch
- Source path: `pages\11067.html`
- Chunk ID: `chunk_aaeaaf7af7ae`
- Images: none
- Duplicate sources: `pages\11551.html`, `pages\20032.html`, `pages\17697.html`

### Full Text

````text
# Calibration - Models Without TPMS Switch

- Make sure the tires are inflated to the specified tire pressure listed on the doorjamb label. Vehicle must be stopped with the transmission in neutral (M/T) or P or N (A/T, CVT).

- Turn the ignition switch to ON (II), or press the engine start/stop button to select the ON mode.

- Use ARROW buttons (right side of steering wheel) to select VEHICLE SETTINGS, then press the SEL/RESET button. TPMS CALIBRATION appears on the display.

- Press the SEL/RESET button. The display switches to the customization setup screen, where you can select CANCEL or CALIBRATE.

- Use ARROW buttons to select CALIBRATE, then press the SEL/RESET button. CALIBRATION STARTED screen appears, then the display returns to the customization menu screen NOTE: If the CALIBRATION FAILED TO START message appears, repeat steps 4 and 5.

- Calibration is completed after driving 31 to 62 mph (50 to 100 km/h), steadily without much acceleration or deceleration for about 30 minutes.
````

## Chunk 8598: TPMS Reminder Reset - Procedure 04

- Title: TPMS Reminder Reset - Procedure 04
- Source path: `pages\11068.html`
- Chunk ID: `chunk_7bc2f7121bc3`
- Images: none
- Duplicate sources: `pages\11552.html`, `pages\20033.html`, `pages\17651.html`

### Full Text

````text
# TPMS Reminder Reset - Procedure 04

Do the TPMS calibration after doing the following items:

- Adjust the tire pressure

- Rotating the tires

- Replacing the tires

- Update/replace the VSA modulator-control unit

The calibration begins when the calibration is selected through the MID (multi-information display). The calibration is completed after driving in an ideal driving condition (28 to 65 mph (45 to 105 km/h), driving steadily without much acceleration or deceleration) for about 19 minutes. Full functionality of the system cannot be performed properly if the calibration is not completed.

- Turn the ignition switch to ON (II), or the engine start/stop button is pressed to select the ON mode. NOTE: Vehicle must be stopped with the transmission in neutral (M/T) or P or N (A/T and CVT).

- Press the MENU button (left side of steering wheel) to enter the customizing mode.

- Press the AUDIO REMOTE + or - button to select CUSTOMIZE SETTINGS > TPMS CALIBRATION > INITIALIZE.

- Press the AUDIO REMOTE + or - button to select YES.

- When the calibration successfully begins, "TPMS CALIBRATION HAS BEEN INITIALIZED" gets displayed on MID when the system received the calibration.
````

## Chunk 8599: TPMS Reminder Reset - Procedure 05: Notes

- Title: TPMS Reminder Reset - Procedure 05: Notes
- Source path: `pages\11069.html`
- Chunk ID: `chunk_8ef989c7df6b`
- Images: none
- Duplicate sources: `pages\11553.html`, `pages\20034.html`, `pages\17698.html`

### Full Text

````text
# TPMS Reminder Reset - Procedure 05: Notes

The calibration begins when the calibration is selected through the Multi-Information display. The calibration is completed after driving in an ideal driving condition 28 to 65 mph (45 to 105 km/h), driving steadily without much acceleration or deceleration for about 19 minutes. Full functionality of the system cannot be performed properly if the calibration is not completed.

Do the TPMS calibration after doing the following items.

- Adjust the tire pressure.

- Rotating the tires.

- Replacing the tires.

- Update/replace the VSA modulator-control unit.
````

## Chunk 8600: Calibrate TPMS (Without TPMS Switch)

- Title: Calibrate TPMS (Without TPMS Switch)
- Source path: `pages\11070.html`
- Chunk ID: `chunk_b6babcce1566`
- Images: `images\G00530817.png`
- Duplicate sources: `pages\11554.html`, `pages\20035.html`, `pages\17699.html`

### Full Text

````text
# Calibrate TPMS (Without TPMS Switch)

- Make sure the tires are inflated to the specified tire pressure listed on the doorjamb label.

- Turn the vehicle to the ON mode. NOTE: Vehicle must be stopped with the shift lever in P or N position.

- Press and hold the INFORMATION button for at least 3 seconds to enter the customizing mode. See Fig 1 .

- Press the SEL/RESET button to select TPMS CALIBRATION.

- Press the SEL/RESET button to select CALIBRATE.

- When the calibration successfully begins, "CALIBRATION STARTED" is shown on the Multi-Information display.
````

## Chunk 8601: Calibrate TPMS (With TPMS Switch)

- Title: Calibrate TPMS (With TPMS Switch)
- Source path: `pages\11071.html`
- Chunk ID: `chunk_bba2ea1ddc01`
- Images: `images\G00530818.png`
- Duplicate sources: `pages\11555.html`, `pages\20036.html`, `pages\17700.html`

### Full Text

````text
# Calibrate TPMS (With TPMS Switch)

- Make sure the tires are inflated to the specified tire pressure listed on the doorjamb label.

- Turn the vehicle to the ON mode. NOTE: Vehicle must be stopped with the transmission in P or N position.

- Press the TPMS switch for 3 seconds. See Fig 1 .

- When the calibration successfully begins, the indicator blinks twice.
````

## Chunk 8602: Calibration Check Method

- Title: Calibration Check Method
- Source path: `pages\11072.html`
- Chunk ID: `chunk_9e5b96ba2850`
- Images: none
- Duplicate sources: `pages\11556.html`, `pages\20037.html`, `pages\17701.html`

### Full Text

````text
# Calibration Check Method

The calibration check process gets interrupted if the vehicle moves. Do the troubleshooting if the indicator does not go off after 2 seconds, keeps blinking or stays on when the vehicle is in the ON mode.

Check if calibration is completed by following these procedures:

- Stop the vehicle and shift into P or N position.

- Turn the vehicle to the OFF (LOCK) mode.

- Turn the vehicle to the ON mode and wait to see the low pressure indicator come on for 2 seconds and then off.

- Do not drive the vehicle and wait for 45 seconds as is.

- If the calibration is completed, the indicator does not come on. If the calibration is not yet completed, then the indicator comes on for 2 seconds and then goes off.
````

## Chunk 8603: TPMS Reminder Reset - Procedure 06

- Title: TPMS Reminder Reset - Procedure 06
- Source path: `pages\11073.html`
- Chunk ID: `chunk_1a839c6d4667`
- Images: `images\G00525244.png`
- Duplicate sources: `pages\11557.html`, `pages\20038.html`, `pages\17652.html`

### Full Text

````text
# TPMS Reminder Reset - Procedure 06

Set the tire pressure of all wheels to pressure specified on the tire and loading information label. Make sure the vehicle is at a complete stop.

- For Manual transmission models: The shift lever is in "N".

- For CVT models: The shift lever is in "P".

- The power mode is ON.

Calibrate the system from the CUSTOMIZE SETTINGS menu on the multi-information display:

- Press the UP/DOWN ARROW buttons on the right side of steering wheel to select CUSTOMIZE SETTINGS, then press the SEL/RESET button to see TPMS CALIBRATION appears on the display. See Fig 1 .

- Press the SEL/RESET button. The display switches to the customization setup screen to select CALIBRATE.

- Press the ARROW buttons and select CALIBRATE, then press the SEL/RESET button to see CALIBRATION STARTED screen appears, then the display returns to the customization menu screen.

- The calibration process finishes automatically.
````

## Chunk 8604: TPMS Reminder Reset - Procedure 07: Notes

- Title: TPMS Reminder Reset - Procedure 07: Notes
- Source path: `pages\11074.html`
- Chunk ID: `chunk_c330ce111a94`
- Images: none
- Duplicate sources: `pages\11558.html`, `pages\20039.html`, `pages\17702.html`

### Full Text

````text
# TPMS Reminder Reset - Procedure 07: Notes

This vehicle is equipped with an indirect TPMS that doesn't use tire pressure sensors mounted inside the tires. It uses the existing VSA wheel speed sensors to monitor and compare tire characteristics while driving.

The calibration begins when the TPMS switch is pressed or the calibration is selected through the Multi-information display. The calibration is completed after driving 31 to 62 mph (50 to 100 km/h), steadily without much acceleration or deceleration for about 19 minutes.

TPMS calibration is required after performing any of the following actions:

- Adjusting tire pressures

- Rotating the tires

- Replacing the tires

- Updating/replacing the VSA modulator-control unit

Calibration begins when TPMS switch is pressed (Models Without ACC) or Calibration is selected through the Multi-information display (Models With ACC). The process finishes automatically as the vehicle is driven. This takes about 30 minutes of cumulative driving at 30 to 60 mph.
````

## Chunk 8605: Calibration - Models Without ACC

- Title: Calibration - Models Without ACC
- Source path: `pages\11075.html`
- Chunk ID: `chunk_455a3432a791`
- Images: none
- Duplicate sources: `pages\11559.html`, `pages\20040.html`, `pages\17703.html`

### Full Text

````text
# Calibration - Models Without ACC

- Make sure the tires are inflated to the specified tire pressure listed on the doorjamb label. Vehicle must be stopped with the transmission in neutral (M/T) or P or N (A/T, CVT).

- Turn the ignition switch to ON (II), or press the engine start/stop button to select the ON mode.

- Press the TPMS switch (lower dash, left of steering wheel) for 3 seconds.

- When the calibration successfully begins, the TPMS indicator (instrument cluster, center left) blinks twice.

- Calibration is completed after driving 31 to 62 mph (50 to 100 km/h), steadily without much acceleration or deceleration for about 30 minutes.
````

## Chunk 8606: Calibration - Models With ACC

- Title: Calibration - Models With ACC
- Source path: `pages\11076.html`
- Chunk ID: `chunk_8d57875cfb80`
- Images: none
- Duplicate sources: `pages\11560.html`, `pages\20041.html`, `pages\17704.html`

### Full Text

````text
# Calibration - Models With ACC

- Make sure the tires are inflated to the specified tire pressure listed on the doorjamb label. Vehicle must be stopped with the transmission in neutral (M/T) or P or N (A/T, CVT).

- Turn the ignition switch to ON (II), or press the engine start/stop button to select the ON mode.

- Press and hold the INFORMATION button (right side of steering wheel) to enter the VEHICLE SETTINGS mode.

- Press the SEL/RESET button to select TPMS CALIBRATION.

- When the calibration successfully begins, "Calibration Started" gets displayed on Multi-information display when the system received the calibration. NOTE: If the CALIBRATION FAILED TO START message appears, repeat steps 3 and 4.

- Calibration is completed after driving 31 to 62 mph (50 to 100 km/h), steadily without much acceleration or deceleration for about 30 minutes.
````

## Chunk 8607: TPMS Reminder Reset - Procedure 08: Notes

- Title: TPMS Reminder Reset - Procedure 08: Notes
- Source path: `pages\11077.html`
- Chunk ID: `chunk_67685924467c`
- Images: none
- Duplicate sources: `pages\11561.html`, `pages\20042.html`, `pages\17705.html`

### Full Text

````text
# TPMS Reminder Reset - Procedure 08: Notes

This vehicle is equipped with an indirect TPMS that doesn't use tire pressure sensors mounted inside the tires. It uses the existing VSA wheel speed sensors to monitor and compare tire characteristics while driving.

Calibration begins when it is selected through the Multi-information display (7-inch screen) or the TPMS switch is pressed (5-inch screen). Calibration is completed after driving 28 to 65 mph (50 to 100 km/h), steadily without much acceleration or deceleration for about 20 minutes.

TPMS calibration is required after performing any of the following actions:

- Adjusting tire pressures

- Rotating the tires

- Replacing the tires

- Updating/replacing the VSA modulator-control unit
````

## Chunk 8608: With Display Audio Type (7-Inch Screen)

- Title: With Display Audio Type (7-Inch Screen)
- Source path: `pages\11078.html`
- Chunk ID: `chunk_0cefa643373e`
- Images: `images\G00561385.png`
- Duplicate sources: `pages\11562.html`, `pages\20043.html`, `pages\17706.html`

### Full Text

````text
# With Display Audio Type (7-Inch Screen)

- Make sure the tires are inflated to the specified tire pressure listed on the doorjamb label.

- Turn the vehicle to the ON mode.

- Press the INFORMATION button (left side of steering wheel - See Fig 1 ), then press the AUDIO REMOTE button to select the VEHICLE SETTINGS.

- Press the AUDIO REMOTE button to select TPMS CALIBRATION.

- Press the AUDIO REMOTE button to select CALIBRATE.

- When the calibration successfully begins, CALIBRATION STARTED is displayed on Multi-information display when the system receives the calibration.
````

## Chunk 8609: With Display Audio Type (5-Inch Screen)

- Title: With Display Audio Type (5-Inch Screen)
- Source path: `pages\11079.html`
- Chunk ID: `chunk_fadae452e5b3`
- Images: none
- Duplicate sources: `pages\11563.html`, `pages\20044.html`, `pages\17707.html`

### Full Text

````text
# With Display Audio Type (5-Inch Screen)

- Make sure the tires are inflated to the specified tire pressure listed on the doorjamb label.

- Turn the vehicle to the ON mode.

- Press and hold the TPMS switch (lower left dash) for 3 seconds.

- When the calibration successfully begins, the indicator blinks twice.
````

## Chunk 8610: TPMS Reminder Reset - Procedure 09: Notes

- Title: TPMS Reminder Reset - Procedure 09: Notes
- Source path: `pages\11080.html`
- Chunk ID: `chunk_ff9ba67a46b9`
- Images: none
- Duplicate sources: `pages\11564.html`, `pages\20045.html`, `pages\17708.html`

### Full Text

````text
# TPMS Reminder Reset - Procedure 09: Notes

This vehicle is equipped with an indirect TPMS that doesn't use tire pressure sensors mounted inside the tires. It uses the existing VSA wheel speed sensors to monitor and compare tire characteristics while driving.

Calibration begins when it is selected through the Multi-information display (7-inch screen) or the TPMS switch is pressed (5-inch screen). Calibration is completed after driving 28 to 65 mph (50 to 100 km/h), steadily without much acceleration or deceleration for about 20 minutes.

TPMS calibration is required after performing any of the following actions:

- Adjusting tire pressures

- Rotating the tires

- Replacing the tires

- Updating/replacing the VSA modulator-control unit
````

## Chunk 8611: With Display Audio Type (7-Inch Screen)

- Title: With Display Audio Type (7-Inch Screen)
- Source path: `pages\11081.html`
- Chunk ID: `chunk_2434d356dd93`
- Images: none
- Duplicate sources: `pages\11565.html`, `pages\20046.html`, `pages\17709.html`

### Full Text

````text
# With Display Audio Type (7-Inch Screen)

- Make sure the tires are inflated to the specified tire pressure listed on the doorjamb label.

- Turn the vehicle to the ON mode.

- Select the HOME button on the screen.

- Select SETTINGS.

- Select VEHICLE.

- Select TPMS CALIBRATION.

- Select CALIBRATION.

- When the calibration successfully begins, CALIBRATION STARTED is displayed on Multi-information display when the system receives the calibration.
````

## Chunk 8612: With Display Audio Type (5-Inch Screen)

- Title: With Display Audio Type (5-Inch Screen)
- Source path: `pages\11082.html`
- Chunk ID: `chunk_50d2f6a86e22`
- Images: `images\G00561385.png`
- Duplicate sources: `pages\11566.html`, `pages\20047.html`, `pages\17710.html`

### Full Text

````text
# With Display Audio Type (5-Inch Screen)

- Make sure the tires are inflated to the specified tire pressure listed on the doorjamb label.

- Turn the vehicle to the ON mode.

- Press the INFORMATION button (left side of steering wheel - See Fig 1 ), then press the AUDIO REMOTE button to select the VEHICLE SETTINGS.

- Press the AUDIO REMOTE button to select TPMS CALIBRATION.

- Press the AUDIO REMOTE button to select CALIBRATE.

- When calibration successfully begins, CALIBRATION STARTED is displayed on Multi-information display when the system receives the calibration.
````

## Chunk 8613: With TPMS Switch

- Title: With TPMS Switch
- Source path: `pages\11083.html`
- Chunk ID: `chunk_95d199e9a3bf`
- Images: none
- Duplicate sources: `pages\11567.html`, `pages\20048.html`, `pages\17711.html`

### Full Text

````text
# With TPMS Switch

- Make sure the tires are inflated to the specified tire pressure listed on the doorjamb label.

- Turn the vehicle to the ON mode.

- Press and hold the TPMS switch (lower left dash) for 3 seconds.

- When the calibration successfully begins, the indicator blinks twice.
````

## Chunk 8614: TPMS Sensor Matching Process - Auto Learn Function

- Title: TPMS Sensor Matching Process - Auto Learn Function
- Source path: `pages\11084.html`
- Chunk ID: `chunk_6ea07267a043`
- Images: none
- Duplicate sources: `pages\11568.html`, `pages\20049.html`, `pages\17712.html`

### Full Text

````text
# TPMS Sensor Matching Process - Auto Learn Function

Each TPMS sensor has a unique identification code. The identification code needs to be matched to a new tire/wheel position after rotating the tires or replacing one or more of the TPMS sensors.

When a tire is installed, the vehicle must be stationary for about 20 minutes before the system recalculates. The following relearn process takes up to 10 minutes, driving at a minimum speed of 20 km/h (12 mph). A dash (-) or pressure value will display in the DIC.
````

## Chunk 8615: Description & Operation: Notes

- Title: Description & Operation: Notes
- Source path: `pages\11085.html`
- Chunk ID: `chunk_db44a5e802c4`
- Images: none
- Duplicate sources: `pages\17743.html`

### Full Text

````text
# Description & Operation: Notes
````

## Chunk 8616: Tire Pressure Monitor System (TPMS)

- Title: Tire Pressure Monitor System (TPMS)
- Source path: `pages\11086.html`
- Chunk ID: `chunk_c1caef9a506b`
- Images: none
- Duplicate sources: `pages\17744.html`

### Full Text

````text
# Tire Pressure Monitor System (TPMS)

Instead of directly measuring the pressure in each tire, the TPMS on this vehicle monitors and compares the rolling radius and rotational characteristics of each wheel and tire while you are driving to determine if one or more tires are significantly under-inflated.
````

## Chunk 8617: Tire Pressure Monitor Warning Indicators

- Title: Tire Pressure Monitor Warning Indicators
- Source path: `pages\11087.html`
- Chunk ID: `chunk_f3549f517666`
- Images: none
- Duplicate sources: `pages\17745.html`

### Full Text

````text
# Tire Pressure Monitor Warning Indicators

- A compact spare tire is used.

- There is a heavier and uneven load on the tires, such as when towing a trailer, than the condition at calibration.

- Snow chains are used.

If the system detects low tire pressure in any of the four tires, the low tire pressure/TPMS indicator comes on, as well as the message indicator. It will keep being turned on until calibration starts.

If a problem in the system is detected, the VSA indicator comes on, and CHECK SYSTEM message (TPMS) on the i-MID is displayed, and the low tire pressure/TPMS indicator comes on after blinking for about 75 seconds.
````

## Chunk 8618: TPMS Reset Procedures: Notes

- Title: TPMS Reset Procedures: Notes
- Source path: `pages\11088.html`
- Chunk ID: `chunk_f6b9eb698369`
- Images: none
- Duplicate sources: `pages\17746.html`

### Full Text

````text
# TPMS Reset Procedures: Notes
````

## Chunk 8619: Models With TPMS Reset Button

- Title: Models With TPMS Reset Button
- Source path: `pages\11089.html`
- Chunk ID: `chunk_b7a50d016041`
- Images: `images\G00561403.png`
- Duplicate sources: `pages\17747.html`

### Full Text

````text
# Models With TPMS Reset Button

You can calibrate the system from the customized features on the i-MID. See Fig 1 .

TPMS cannot be calibrated if a compact spare tire is installed.

- Press and hold the TPMS button until the low tire pressure/TPMS indicator blinks twice, indicating the calibration process has begun.

- If the low tire pressure/TPMS indicator does not blink, confirm the above conditions then press and hold the TPMS button again.

- The calibration process finishes automatically. It requires approximately 30 minutes of cumulative driving at speeds between 30-60 mph (48-97 km/h).
````

## Chunk 8620: Models With Driver Information Interface

- Title: Models With Driver Information Interface
- Source path: `pages\11090.html`
- Chunk ID: `chunk_f6605a9788c2`
- Images: `images\G00561404.png`
- Duplicate sources: `pages\17748.html`

### Full Text

````text
# Models With Driver Information Interface

You can calibrate the system from the customized features on the driver information interface.

- Press the INFORMATION (i icon) button then use the ARROW buttons to select Vehicle Settings (gear icon), then press the ENTER button. TPMS CALIBRATION appears on the display.

- Press the ENTER button. The display switches to the Customization Setup screen, where you can select CANCEL or CALIBRATE.

- Press the ARROW buttons and select CALIBRATE, then press the ENTER button. The CALIBRATION STARTED screen appears, then the display returns to the customization menu screen.

- The calibration process finishes automatically. It requires approximately 30 minutes of cumulative driving at speeds between 30-65 mph (48-105 km/h).
````

## Chunk 8621: Models with Display Audio or Center Display

- Title: Models with Display Audio or Center Display
- Source path: `pages\11091.html`
- Chunk ID: `chunk_4a29240e2231`
- Images: `images\G00561405.png`, `images\G00561420.png`
- Duplicate sources: `pages\17749.html`

### Full Text

````text
# Models with Display Audio or Center Display

You can calibrate the system from the customized feature on the audio/information screen.

- Turn the ignition switch to ON.

- Select HOME.

- Select SETTINGS.

- Select VEHICLE.

- Select TPMS CALIBRATION.

- Select CALIBRATE. When the calibration is complete, the display returns to the customization menu screen.

- The calibration process finishes automatically. It requires approximately 30 minutes of cumulative driving at speeds between 30-65 mph (48-105 km/h).
````

## Chunk 8622: Torque Specifications

- Title: Torque Specifications
- Source path: `pages\11093.html`
- Chunk ID: `chunk_5f23226a2b5a`
- Images: none
- Duplicate sources: `pages\17751.html`

### Full Text

````text
# Torque Specifications

Component | Ft. Lbs. (N.m)

Wheel Nut | 80 (108)
````

## Chunk 8623: Steering & Suspension Systems: Notes

- Title: Steering & Suspension Systems: Notes
- Source path: `pages\11095.html`
- Chunk ID: `chunk_b88cfd03d144`
- Images: none
- Duplicate sources: `pages\19868.html`

### Full Text

````text
# Steering & Suspension Systems: Notes

These materials are confidential and are not to be disclosed to, or utilized by, any individual or entity other than participants of the Motorist Assurance Program (MAP).

The Automotive Maintenance and Repair Association (AMRA) and MAP do not warrant these materials or guarantee their accuracy, and AMRA and MAP assume no liability for errors.
````

## Chunk 8624: Wheel And Tire: Notes

- Title: Wheel And Tire: Notes
- Source path: `pages\11099.html`
- Chunk ID: `chunk_88b656d33706`
- Images: none
- Duplicate sources: `pages\19872.html`

### Full Text

````text
# Wheel And Tire: Notes

Steering and suspension are complex systems made up of a variety of interdependent components. For proper vehicle handling, ride, and tire wear, a thorough inspection is required whenever suspension work is being performed. Conditions listed assume that the problem has been isolated to the specific component by proper testing procedures.
````

## Chunk 8625: Wheel And Tire: Tires

- Title: Wheel And Tire: Tires
- Source path: `pages\11100.html`
- Chunk ID: `chunk_ef973e1e16d6`
- Images: none
- Duplicate sources: `pages\19873.html`

### Full Text

````text
# Wheel And Tire: Tires

When replacing tires, it is suggested that the replacement tires match or exceed the OEM speed rating designation. If tires of different speed rating designations are mixed on the same vehicle, the tires may vary in handling characteristics. Do not mix different speed rating designations on the same axle.

Consult the vehicle owner's manual or vehicle placard for correct tire size, service description, load index, speed rating and cold inflation pressure of the original tires. Do not exceed the maximum load or inflation capacity of the tire specified by the Tire and Rim Association (www.us-tra.org)

When replacing fewer than ALL tires on a vehicle, follow the vehicle manufacturer's recommendations as to the placement of the new tires. If it is not possible to follow the vehicle manufacturer's tire replacement recommendations, remember to replace tires on the same axle with the same size, construction, speed rating, and, if possible, similar tread pattern.

Do not mix radials with non-radial tires on the same axle, as this may affect vehicle handling and stability. If radial tires and non-radial tires are mixed on the same vehicle, the radials must be on the rear. If radial and non-radial tires are used on a vehicle equipped with dual rear tires, radial tires may be used on either axle. High-pressure temporary compact spare tires are exempt from this rule.

Do not mix size or type (all season, performance, mud and snow) of tires on the same axle. When replacing only two tires on front or rear drive vehicles, follow the vehicle manufacturer's recommendations concerning placement. If it is not possible to follow OE recommendations, it is preferable to place the two new tires on the rear for greater stability, greater adhesion affecting steering -- on other than dry pavement -- and overall safety, regardless of whether the vehicle is front or rear wheel drive.

It is particularly important to match all tire sizes and constructions on 4-wheel (4x4) and all-wheel (AWD) drive vehicles unless otherwise specified by vehicle manufacturer. Ideally, all four tires should be replaced at the same time. Some vehicle manufacturers restrict replacement of tires to specific brands, types, or sizes.
````

## Chunk 8626: Active Suspension Control Modules

- Title: Active Suspension Control Modules
- Source path: `pages\11112.html`
- Chunk ID: `chunk_1666f4905bb6`
- Images: none
- Duplicate sources: `pages\19885.html`

### Full Text

````text
# Active Suspension Control Modules

Condition | Code | Procedure

Application incorrect | B | Require replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Connector broken | A | Require repair or replacement

Connector melted | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector missing | C | Require repair

Contaminated | A | Require repair or replacement

NOTE: Determine source of contamination, such as engine coolant, fuel, metal particles, or water. Require repair or replacement.

Inoperative | B | Require repair or replacement

NOTE: Inoperative includes intermittent operation. Some components may be serviceable; check for accepted cleaning procedure.

Leaking | B | Require repair or replacement

Malfunctioning | A | Require replacement

NOTE: Includes inoperative, intermittent operation, failure to perform all functions, out of OEM specifications, or out of range.

Missing | C | Require replacement

Terminal broken | A | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead corroded | A | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8627: Active Variable Ratio Steering

- Title: Active Variable Ratio Steering
- Source path: `pages\11113.html`
- Chunk ID: `chunk_0f74e3083772`
- Images: none
- Duplicate sources: `pages\19886.html`

### Full Text

````text
# Active Variable Ratio Steering

Condition | Code | Procedure

Improper Operation

NOTE: Refer to manufacturers' service information.
````

## Chunk 8628: Air Bags

- Title: Air Bags
- Source path: `pages\11117.html`
- Chunk ID: `chunk_fe32469bc143`
- Images: none
- Duplicate sources: `pages\19890.html`

### Full Text

````text
# Air Bags

Condition | Code | Procedure

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Collar cracked | A | Require replacement

End cap cracked | A | Require replacement

Inner fabric of bag damaged | A | Require replacement

Leaking | A | Require repair or replacement

Outer covering of air bag is cracked to the extent that inner fabric of air bag is visible | 1 | Suggest replacement

Piston cracked | A | Require replacement
````

## Chunk 8629: Air Ride Control Modules

- Title: Air Ride Control Modules
- Source path: `pages\11118.html`
- Chunk ID: `chunk_a5806305b67e`
- Images: none
- Duplicate sources: `pages\19891.html`

### Full Text

````text
# Air Ride Control Modules

Condition | Code | Procedure

Application incorrect | B | Require replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Connector broken | A | Require repair or replacement

Connector melted | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector missing | C | Require repair

Contaminated | A | Require repair or replacement

NOTE: Determine source of contamination, such as engine coolant, fuel, metal particles, or water. Require repair or replacement.

Inoperative | A | Require repair or replacement

NOTE: Inoperative includes intermittent operation. Some components may be serviceable; check for accepted cleaning procedure.

Leaking | B | Require repair or replacement

Malfunctioning | A | Require replacement

NOTE: Includes inoperative, intermittent operation, failure to perform all functions, out of OEM specifications, or out of range.

Missing | C | Require replacement

Terminal broken | A | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead corroded | A | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8630: Air Ride Suspension Torsion Springs (Counter Balancing)

- Title: Air Ride Suspension Torsion Springs (Counter Balancing)
- Source path: `pages\11119.html`
- Chunk ID: `chunk_058a017289e9`
- Images: none
- Duplicate sources: `pages\19892.html`

### Full Text

````text
# Air Ride Suspension Torsion Springs (Counter Balancing)

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Broken | A | Require replacement

Missing | C | Require replacement
````

## Chunk 8631: Air Ride Tubes

- Title: Air Ride Tubes
- Source path: `pages\11121.html`
- Chunk ID: `chunk_8edfc9a9743e`
- Images: none
- Duplicate sources: `pages\19894.html`

### Full Text

````text
# Air Ride Tubes

Condition | Code | Procedure

Application incorrect | B | Require replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Connected incorrectly | A | Require repair

Insufficient clamping force, allowing hose to leak | A | Require repair or replacement

Leaking | A | Require repair or replacement

Melted | 1 | Suggest repair or replacement

Missing | C | Require replacement

Protective sleeves damaged | 2 | Suggest replacement of sleeves

Protective sleeves missing | C | Require replacement of sleeves

Restricted, affecting performance | A | Require repair or replacement

Restricted, not affecting performance | 2 | Suggest repair or replacement

Routed incorrectly (where failure is likely to occur) | B | Require repair or replacement

Safety clip missing | C | Require replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

Type incorrect | 2 | Suggest repair or replacement
````

## Chunk 8632: Air Shocks And Air Struts

- Title: Air Shocks And Air Struts
- Source path: `pages\11122.html`
- Chunk ID: `chunk_7a55c61fc8ca`
- Images: none
- Duplicate sources: `pages\19895.html`

### Full Text

````text
# Air Shocks And Air Struts

Condition | Code | Procedure

Inner fabric of air bag damaged | A | Require replacement

Leaking | A | Require repair or replacement

Outer covering of air bag is cracked to the extent that inner fabric of air bag is visible | 1 | Suggest replacement
````

## Chunk 8633: Air Spring Valves

- Title: Air Spring Valves
- Source path: `pages\11123.html`
- Chunk ID: `chunk_ee4a7b7b1c70`
- Images: none
- Duplicate sources: `pages\19896.html`

### Full Text

````text
# Air Spring Valves

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Blocked | A | Require repair or replacement

Connector bent | A | Require repair or replacement

Connector broken | A | Require replacement

Connector loose | A | Require repair or replacement

Inoperative | A | Require repair or replacement

Leaking | B | Require repair or replacement

Restricted | A | Require repair or replacement
````

## Chunk 8634: Air Springs

- Title: Air Springs
- Source path: `pages\11124.html`
- Chunk ID: `chunk_ad7dc60d253a`
- Images: none
- Duplicate sources: `pages\19897.html`

### Full Text

````text
# Air Springs

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Collar cracked | A | Require replacement

End cap cracked | A | Require replacement

Inner fabric of bag damaged | A | Require replacement

Leaking | A | Require repair or replacement

Outer covering of air bag is cracked to the extent that inner fabric of air bag is visible | 1 | Suggest replacement

Piston cracked | A | Require replacement
````

## Chunk 8635: Air Suspension Control Valves

- Title: Air Suspension Control Valves
- Source path: `pages\11125.html`
- Chunk ID: `chunk_8a33cd226fbf`
- Images: none
- Duplicate sources: `pages\19898.html`

### Full Text

````text
# Air Suspension Control Valves

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted | A | Require replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector missing | C | Require replacement

Leaking | B | Require repair or replacement

Output incorrect | B | Require replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

Wire lead burned | A | Require repair or replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8636: Air Suspension DRIERS

- Title: Air Suspension DRIERS
- Source path: `pages\11126.html`
- Chunk ID: `chunk_f4510426696e`
- Images: none
- Duplicate sources: `pages\19899.html`

### Full Text

````text
# Air Suspension DRIERS

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Contaminated, affecting performance | A | Require replacement

Desiccant bag deteriorated | A | Require replacement

NOTE: Inspect system to determine effects of desiccant bag deterioration.

Leaking | B | Require replacement

Restricted | A | Require repair or replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

Tubing connection leaking | A | Require repair or replacement
````

## Chunk 8637: Axle Acceleration Sensor

- Title: Axle Acceleration Sensor
- Source path: `pages\11127.html`
- Chunk ID: `chunk_b572cf02de71`
- Images: none
- Duplicate sources: `pages\19900.html`

### Full Text

````text
# Axle Acceleration Sensor

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware corroded, affecting structural integrity | A | Require replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted | A | Require replacement

Connector missing | C | Require replacement

NOTE: Determine cause and correct prior to replacement of part.

Dust boot missing | C | Require replacement of boot

Dust boot split | A | Require replacement of boot

NOTE: If boot is not available separately, suggest replacement of sensor (reason code 2). This condition can lead to damage of the sliding magnet, which, in turn, causes premature sensor failure

Dust boot torn | A | Require replacement of boot

NOTE: If boot is not available separately, suggest replacement of sensor (reason code 2). This condition can lead to damage of the sliding magnet, which, in turn, causes premature sensor failure.

Housing cracked | B | Require replacement

NOTE: If boot is not available separately, suggest replacement of sensor (reason code 2). This condition can lead to damage of the sliding magnet, which, in turn, causes premature sensor failure.

Lead routing incorrect | B | Require rerouting according to vehicle manufacturer's specifications

Loose | B | Require adjustment to vehicle manufacturer's specifications

Missing | C | Require replacement

Output signal incorrect | B | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Wire lead burned | A | Require repair or replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8638: Ball Joints

- Title: Ball Joints
- Source path: `pages\11128.html`
- Chunk ID: `chunk_a7dbb3226bac`
- Images: none
- Duplicate sources: `pages\19901.html`

### Full Text

````text
# Ball Joints

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware corroded, affecting structural integrity | A | Require replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Binding | A | Further inspection required

NOTE: If greaseable, grease ball joint. If problem persists or joint is non-greaseable, require replacement.

Grease boot cracked | 2 | Suggest replacement

NOTE: Cracked grease boot will allow contaminants to enter the ball joint and will accelerate wear.

Grease boot missing | C | Require replacement

NOTE: Lack of grease boot will allow contaminants to enter the ball joint and will accelerate wear.

Grease boot torn | A | Require replacement

NOTE: Torn grease boot will allow contaminants to enter the ball joint and will accelerate wear.

Grease fitting broken | A | Require replacement of grease fitting

NOTE: Some vehicles come from the factory with broken fittings. No service is suggested or required on these vehicles.

Grease fitting missing | C | Require replacement of grease fitting

Grease fitting won't seal | A | Require replacement of grease fitting

Greaseable ball joint will not take grease | 2 | Suggest replacement of grease fitting

NOTE: If the greaseable ball joint still will not take grease after replacing the grease fitting, suggest replacement of ball joint.

Nut on ball joint loose | A | Require repair or replacement

NOTE: Check for bent stud or damaged taper hole.

Pre-load adjustment incorrect | B | Require repair or replacement

Seized | A | Require replacement

Stud bent | B | Require replacement

NOTE: Check for damaged taper hole.

Stud broken | A | Require replacement

NOTE: Check for damaged taper hole.

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

NOTE: Check for damaged taper hole.

Wear exceeds manufacturer's specifications | B | Require replacement
````

## Chunk 8639: Body Acceleration Sensor

- Title: Body Acceleration Sensor
- Source path: `pages\11129.html`
- Chunk ID: `chunk_754a3ee14fe7`
- Images: none
- Duplicate sources: `pages\19902.html`

### Full Text

````text
# Body Acceleration Sensor

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware corroded, affecting structural integrity | A | Require replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted | A | Require replacement

Connector missing | C | Require replacement

NOTE: Determine cause and correct prior to replacement of part.

Dust boot missing | C | Require replacement of boot

Dust boot split | A | Require replacement of boot

NOTE: If boot is not available separately, suggest replacement of sensor (reason code 2). This condition can lead to damage of the sliding magnet, which, in turn, causes premature sensor failure

Dust boot torn | A | Require replacement of boot

NOTE: If boot is not available separately, suggest replacement of sensor (reason code 2). This condition can lead to damage of the sliding magnet, which, in turn, causes premature sensor failure.

Housing cracked | B | Require replacement

NOTE: If boot is not available separately, suggest replacement of sensor (reason code 2). This condition can lead to damage of the sliding magnet, which, in turn, causes premature sensor failure.

Lead routing incorrect | B | Require rerouting according to vehicle manufacturer's specifications

Loose | B | Require adjustment to vehicle manufacturer's specifications

Missing | C | Require replacement

Output signal incorrect | B | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Wire lead burned | A | Require repair or replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8640: Steering And Suspension, Wheel Alignment, Wheels And Tires: Bushings

- Title: Steering And Suspension, Wheel Alignment, Wheels And Tires: Bushings
- Source path: `pages\11130.html`
- Chunk ID: `chunk_ca674116729f`
- Images: none
- Duplicate sources: `pages\19903.html`

### Full Text

````text
# Steering And Suspension, Wheel Alignment, Wheels And Tires: Bushings

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Binding | A | Require repair or replacement

Deteriorated, affecting performance | A | Require repair or replacement

NOTE: If condition is caused by oil-soaking, further inspection is required to determine source of oil.

Distorted, affecting performance | A | Require repair or replacement

Leaking (fluid-filled type) | A | Require replacement

Missing | C | Require replacement

Noisy | 2 | Further inspection required

NOTE: If noise isolated to bushing, suggest repair or replacement. Use only approved lubricant on rubber bushings. Petroleum-based lubricants may damage rubber bushings.

Oil-soaked, affecting performance | A | Require replacement

NOTE: Further inspection required to determine source of oil.

Rubber separating from internal metal sleeve on bonded bushing | A | Require replacement

Seized | A | Require replacement

Shifted (out of position) | B | Require repair or replacement

Split | A | Require replacement

Surface cracking (weather-checked) | No service suggested or required
````

## Chunk 8641: Center Links

- Title: Center Links
- Source path: `pages\11131.html`
- Chunk ID: `chunk_05d93e47bc09`
- Images: none
- Duplicate sources: `pages\19904.html`

### Full Text

````text
# Center Links

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Bent, affecting performance | B | Require replacement

Binding | A | Further inspection required

NOTE: If greaseable, grease joint. If problem persists or joint is non-greaseable, require replacement.

Grease boot cracked | 2 | Require replacement of boot

NOTE: If boot is not available as a separate component, suggest replacement of center link (reason code 2). Cracked grease boot will allow contaminants to enter the joint and will accelerate wear.

Grease boot missing | C | Require replacement of boot

NOTE: If boot is not available as a separate component, suggest replacement of center link (reason code 2). Lack of grease boot will allow contaminants to enter the joint and will accelerate wear

Grease boot torn | A | Require replacement of boot

NOTE: If boot is not available as a separate component, suggest replacement of center link (reason code 2). Torn grease boot will allow contaminants to enter the joint and will accelerate wear .

Grease fitting broken | A | Require replacement of grease fitting

Grease fitting missing | C | Require replacement of grease fitting

Grease fitting won't seal | A | Require replacement of grease fitting

Grease seal missing | C | Require replacement

NOTE: If seal is not available as a separate component, suggest replacement of center link (reason code 2). Lack of grease seal will allow contaminants to enter the joint and will accelerate wear.

Grease seal torn | A | Require replacement

NOTE: If seal is not available as a separate component, suggest replacement of center link (reason code 2). Torn grease seal will allow contaminants to enter the joint and will accelerate wear.

Greaseable center link will not take grease | 2 | Suggest replacement of grease fitting

NOTE: If greaseable center link still will not take grease after replacing the grease fitting, suggest replacement of center link.

Looseness (perceptible horizontal movement) | 1 | Suggest replacement

NOTE: If manufacturer's procedures for inspection exist, use those procedures; otherwise, use an approved inspection method such as the dry park check. Do not use pliers or pry bar to check ball and socket movement. Use only moderate hand pressure.

Looseness that is excessive | B | Require replacement

NOTE: Excessive looseness is defined as being significant enough to affect vehicle handling or structural integrity. If manufacturer's procedures for inspection exist, use those procedures; otherwise, use an approved inspection method such as the dry park check.

CAUTION: Do not use pliers or pry bar to check ball and socket movement. Use only moderate hand pressure.

Seized | A | Require replacement

Stud bent | B | Require replacement

NOTE: Check for damaged taper hole.

Stud broken | A | Require replacement

NOTE: Check for damaged taper hole.

Stud loose in taper hole | A | Require repair or replacement

NOTE: Check for damaged taper hole.

Taper hole elongated | A | Require replacement

NOTE: Check for damaged stud.

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

NOTE: Check for damaged taper hole.

Wear exceeds manufacturer's specifications | B | Require replacement
````

## Chunk 8642: Steering And Suspension, Wheel Alignment, Wheels And Tires: Compressors

- Title: Steering And Suspension, Wheel Alignment, Wheels And Tires: Compressors
- Source path: `pages\11132.html`
- Chunk ID: `chunk_99e2210da905`
- Images: none
- Duplicate sources: `pages\19905.html`

### Full Text

````text
# Steering And Suspension, Wheel Alignment, Wheels And Tires: Compressors

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Connector bent | A | Require repair or replacement

Connector broken | A | Require replacement

Connector loose | A | Require repair or replacement

Does not build pressure | A | Require replacement

Excessive run time | B | Require replacement

Inoperative | A | Require replacement

NOTE: Inoperative includes intermittent operation.

Leaking | B | Require repair or replacement

Missing | C | Require replacement

Noisy (abnormal) | 2 | Suggest replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Wire lead burned | A | Require repair or replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8643: Control Arm Shafts

- Title: Control Arm Shafts
- Source path: `pages\11134.html`
- Chunk ID: `chunk_ff1d3505346a`
- Images: none
- Duplicate sources: `pages\19907.html`

### Full Text

````text
# Control Arm Shafts

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Bent, affecting performance | B | Require replacement

Shaft bushing surface undersized (worn) | B | Require replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement
````

## Chunk 8644: Control Arms

- Title: Control Arms
- Source path: `pages\11135.html`
- Chunk ID: `chunk_9e3e463d9de8`
- Images: none
- Duplicate sources: `pages\19908.html`

### Full Text

````text
# Control Arms

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware corroded, affecting structural integrity | A | Require replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Ball joint hole oversized (loose interference or press fit) | B | Further inspection required

NOTE: If oversized ball joint is available, require replacement orb all joint. If oversized ball joint is not available, require replacement of control arm.

Bent, affecting performance | B | Require replacement

Bushing hole oversized | B | Require replacement

Corroded, affecting structural integrity | A | Require replacement

Holes distorted | A | Require replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement
````

## Chunk 8645: Control Modules

- Title: Control Modules
- Source path: `pages\11136.html`
- Chunk ID: `chunk_bb263bffa76e`
- Images: none
- Duplicate sources: `pages\19909.html`

### Full Text

````text
# Control Modules

Condition | Code | Procedure

Application incorrect | B | Require replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Connector broken | A | Require repair or replacement

Connector melted | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector missing | C | Require repair

Contaminated | A | Require repair or replacement

NOTE: Determine source of contamination, such as engine coolant, fuel, metal particles, or water. Require repair or replacement.

Inoperative | A | Require repair or replacement

NOTE: Inoperative includes intermittent operation. Some components may be serviceable; check for accepted cleaning procedure.

Leaking | B | Require repair or replacement

Malfunctioning | A | Require replacement

NOTE: Includes inoperative, intermittent operation, failure to perform all functions, out of OEM specifications, or out of range.

Missing | C | Require replacement

Terminal broken | A | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead corroded | A | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8646: Distance Regulation Control Module

- Title: Distance Regulation Control Module
- Source path: `pages\11137.html`
- Chunk ID: `chunk_85f987b6e59c`
- Images: none
- Duplicate sources: `pages\19910.html`

### Full Text

````text
# Distance Regulation Control Module

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware corroded, affecting structural integrity | A | Require replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted | A | Require replacement

NOTE: Determine cause and correct prior to replacement of part.

Connector melted | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector missing | C | Require replacement

Contaminated | A | Require repair or replacement

NOTE: Determine source of contamination, such as engine coolant, fuel, metal particles, or water. Require repair or replacement.

Dust boot missing | C | Require replacement of boot

NOTE: If boot is not available separately, suggest replacement of sensor (reason code 2). This condition can lead to damage of the sliding magnet, which, in turn, causes premature sensor failure

Dust boot split | A | Require replacement of boot

NOTE: If boot is not available separately, suggest replacement of sensor (reason code 2). This condition can lead to damage of the sliding magnet, which, in turn, causes premature sensor failure.

Dust boot torn | A | Require replacement of boot

NOTE: If boot is not available separately, suggest replacement of sensor (reason code 2). This condition can lead to damage of the sliding magnet, which, in turn, causes premature sensor failure.

Housing cracked | B | Require replacement

Inoperative | A | Require repair or replacement

NOTE: Inoperative includes intermittent operation. Some components may be serviceable; check for accepted cleaning procedure.

Lead routing incorrect | B | Require rerouting according to vehicle manufacturer's specifications

Loose | B | Require adjustment to vehicle manufacturer's specifications

Malfunctioning | A | Require replacement

NOTE: includes inoperative, intermittent operation, failure to perform all functions, out of OEM specifications, or out of range.

Missing | C | Require replacement

Output signal incorrect | B | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Wire lead burned | A | Require repair or replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8647: Distance Regulation Sensor

- Title: Distance Regulation Sensor
- Source path: `pages\11138.html`
- Chunk ID: `chunk_8cd5a45ee180`
- Images: none
- Duplicate sources: `pages\19911.html`

### Full Text

````text
# Distance Regulation Sensor

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware corroded, affecting structural integrity | A | Require replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted | A | Require replacement

Connector missing | C | Require replacement

NOTE: Determine cause and correct prior to replacement of part.

Dust boot missing | C | Require replacement of boot

Dust boot split | A | Require replacement of boot

NOTE: If boot is not available separately, suggest replacement of sensor (reason code 2). This condition can lead to damage of the sliding magnet, which, in turn, causes premature sensor failure

Dust boot torn | A | Require replacement of boot

NOTE: If boot is not available separately, suggest replacement of sensor (reason code 2). This condition can lead to damage of the sliding magnet, which, in turn, causes premature sensor failure.

Housing cracked | B | Require replacement

NOTE: If boot is not available separately, suggest replacement of sensor (reason code 2). This condition can lead to damage of the sliding magnet, which, in turn, causes premature sensor failure.

Lead routing incorrect | B | Require rerouting according to vehicle manufacturer's specifications

Loose | B | Require adjustment to vehicle manufacturer's specifications

Missing | C | Require replacement

Output signal incorrect | B | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Wire lead burned | A | Require repair or replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8648: Drag Links

- Title: Drag Links
- Source path: `pages\11139.html`
- Chunk ID: `chunk_2f8ebdb30482`
- Images: none
- Duplicate sources: `pages\19912.html`

### Full Text

````text
# Drag Links

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Bent, affecting performance | B | Require replacement

Binding | A | Further inspection required

NOTE: If greaseable, grease joint. If problem persists or joint is non-greaseable, require replacement.

Grease boot cracked | 2 | Require replacement of boot

NOTE: If boot is not available as a separate component, suggest replacement of drag link (reason code 2). Cracked grease boot will allow contaminants to enter the joint and will accelerate wear.

Grease boot missing | C | Require replacement of boot

NOTE: If boot is not available as a separate component, suggest replacement of drag link (reason code 2). Lack of grease boot will allow contaminants to enter the joint and will accelerate wear.

Grease boot torn | A | Require replacement of boot

NOTE: If boot is not available as a separate component, suggest replacement of drag link (reason code 2). Torn grease boot will allow contaminants to enter the joint and will accelerate wear.

Grease fitting broken | A | Require replacement of grease fitting

Grease fitting missing | C | Require replacement of grease fitting

Grease fitting won't seal | A | Require replacement of grease fitting

Grease seal missing | C | Require replacement

NOTE: If seal is not available as a separate component, suggest replacement of drag link (reason code 2). Lack of grease seal will allow contaminants to enter the joint and will accelerate wear.

Grease seal torn | A | Require replacement

NOTE: If seal is not available as a separate component, suggest replacement of drag link (reason code 2). Torn grease seal will allow contaminants to enter the joint and will accelerate wear.

Greaseable drag link will not take grease | 2 | Suggest replacement of grease fitting

NOTE: If greaseable center link still will not take grease after replacing the grease fitting, suggest replacement of drag link.

Looseness (perceptible horizontal movement) | 1 | Suggest replacement

NOTE: If manufacturer's procedures for inspection exist, use those procedures; otherwise, use an approved inspection method such as the dry park check. Do not use pliers or pry bar to check ball and socket movement. Use only moderate hand pressure.

Looseness that is excessive | B | Require replacement

NOTE: Excessive looseness is defined as being significant enough to affect vehicle handling or structural integrity. If manufacturer's procedures for inspection exist, use those procedures; otherwise, use an approved inspection method such as the dry park check.

CAUTION: Do not use pliers or pry bar to check ball and socket movement. Use only moderate hand pressure.

Seized | A | Require replacement

Stud bent | B | Require replacement

NOTE: Check for damaged taper hole.

Stud broken | A | Require replacement

NOTE: Check for damaged taper hole.

Stud loose in taper hole | A | Require repair or replacement

NOTE: Check for damaged taper hole.

Taper hole elongated | A | Require replacement

NOTE: Check for damaged stud.

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

NOTE: Check for damaged taper hole.

Wear exceeds manufacturer's specifications | B | Require replacement
````

## Chunk 8649: Dynamic Stability Control

- Title: Dynamic Stability Control
- Source path: `pages\11140.html`
- Chunk ID: `chunk_cb5573a576e2`
- Images: none
- Duplicate sources: `pages\19913.html`

### Full Text

````text
# Dynamic Stability Control

Condition | Code | Procedure

NOTE: On slippery surfaces or during aggressive maneuvers, if the vehicle understeers severely, the computer will actuate the brakes on the inside rear wheel, just hard enough and just long enough to correct the steering behavior. When the vehicle oversteers severely, the system will brake the outside front wheel instead.

NOTE: When servicing this system, OEM may require steering angle sensor be calibrated to the vehicle thrustline.
````

## Chunk 8650: Electronic Ride Control Shocks And Struts

- Title: Electronic Ride Control Shocks And Struts
- Source path: `pages\11142.html`
- Chunk ID: `chunk_d2d65bd3723c`
- Images: none
- Duplicate sources: `pages\19915.html`

### Full Text

````text
# Electronic Ride Control Shocks And Struts

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Connector bent | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector loose | A | Require repair or replacement

Electronic valve control inoperative | A | Require replacement

NOTE: It is acceptable to replace with a non-electronically controlled unit, where available.

Terminal bent | A | Require repair or replacement

Terminal broken | A | Require repair or replacement

Terminal corroded | A | Require repair or replacement

Terminal loose | A | Require repair or replacement
````

## Chunk 8651: Flex Couplers

- Title: Flex Couplers
- Source path: `pages\11145.html`
- Chunk ID: `chunk_e4302ec95661`
- Images: none
- Duplicate sources: `pages\19918.html`

### Full Text

````text
# Flex Couplers

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Flex coupler binding | A | Require repair or replacement of coupler

Flex coupler loose | A | Require repair or replacement of coupler

Flex coupler missing parts | A | Require repair or replacement of coupler

Flex coupler soft/ spongy | A | Require replacement of coupler

Flex coupler tom | A | Require replacement of coupler

Steering coupler shield cracked | 2 | Suggest replacement

Steering coupler shield missing | C | Require replacement

Steering coupler shield torn | 2 | Suggest replacement

U-joint binding | A | Require repair or replacement of joint

U-joint loose | A | Require repair or replacement of joint
````

## Chunk 8652: Steering And Suspension, Wheel Alignment, Wheels And Tires: Gaskets

- Title: Steering And Suspension, Wheel Alignment, Wheels And Tires: Gaskets
- Source path: `pages\11146.html`
- Chunk ID: `chunk_d960946405e5`
- Images: none
- Duplicate sources: `pages\19919.html`

### Full Text

````text
# Steering And Suspension, Wheel Alignment, Wheels And Tires: Gaskets

Condition | Code | Procedure

Leaking | A | Require repair or replacement

NOTE: Require inspection of mating and sealing surface and repair or replace as necessary.
````

## Chunk 8653: Height Sensors

- Title: Height Sensors
- Source path: `pages\11147.html`
- Chunk ID: `chunk_9b46ae9be7b6`
- Images: none
- Duplicate sources: `pages\19920.html`

### Full Text

````text
# Height Sensors

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware corroded, affecting structural integrity | A | Require replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted | A | Require replacement

NOTE: Determine cause and correct prior to replacement of part.

Connector missing | C | Require replacement

Dust boot missing | C | Require replacement of boot

NOTE: If boot is not available separately, suggest replacement of sensor (reason code 2). This condition can lead to damage of the sliding magnet, which, in turn, causes premature sensor failure

Dust boot split | A | Require replacement of boot

NOTE: If boot is not available separately, suggest replacement of sensor (reason code 2). This condition can lead to damage of the sliding magnet, which, in turn, causes premature sensor failure.

Dust boot torn | A | Require replacement of boot

NOTE: If boot is not available separately, suggest replacement of sensor (reason code 2). This condition can lead to damage of the sliding magnet, which, in turn, causes premature sensor failure.

Housing cracked | B | Require replacement

Lead routing incorrect | B | Require rerouting according to vehicle manufacturer's specifications

Loose | B | Require adjustment to vehicle manufacturer's specifications

Missing | C | Require replacement

Output signal incorrect | B | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Wire lead burned | A | Require repair or replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8654: Hydraulic Power Steering Pumps

- Title: Hydraulic Power Steering Pumps
- Source path: `pages\11149.html`
- Chunk ID: `chunk_ad80b7588a21`
- Images: none
- Duplicate sources: `pages\19922.html`

### Full Text

````text
# Hydraulic Power Steering Pumps

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Binding | A | Require repair or replacement

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted | A | Require replacement

NOTE: Determine cause and correct prior to replacement of part.

Connector missing | C | Require replacement

Leaking | B | Require repair or replacement

Noisy | 2 | Suggest repair or replacement

Pulley bent | A | Require repair or replacement of pulley

Pulley missing | C | Require replacement of pulley

Pump output out of manufacturer's specifications | A | Require repair or replacement

Remote reservoir leaking | A | Require replacement of reservoir

Reservoir cap broken | A | Require replacement of cap

Reservoir cap missing | C | Require replacement of cap

Seized | A | Require replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

Wire lead burned | A | Require repair or replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8655: Hydraulic Suspension Hoses

- Title: Hydraulic Suspension Hoses
- Source path: `pages\11150.html`
- Chunk ID: `chunk_4e86b60be138`
- Images: none
- Duplicate sources: `pages\19923.html`

### Full Text

````text
# Hydraulic Suspension Hoses

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Blistered | B | Require replacement

Fitting threads damaged | A | Require repair or replacement

Fitting threads stripped (threads missing) | A | Require replacement

Inner fabric (webbing) cut | B | Require replacement

Leaking | A | Require replacement

Missing | C | Require replacement

Outer covering is cracked to the extent that inner fabric of hose is visible | B | Require replacement

Restricted | A | Require replacement

Routed incorrectly (where failure is likely to occur) | B | Require repair or replacement

Secured incorrectly | B | Require repair
````

## Chunk 8656: Hydraulic Suspension Pumps

- Title: Hydraulic Suspension Pumps
- Source path: `pages\11151.html`
- Chunk ID: `chunk_b00a836ae0d9`
- Images: none
- Duplicate sources: `pages\19924.html`

### Full Text

````text
# Hydraulic Suspension Pumps

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Binding | A | Require repair or replacement

Fluid at or beyond service interval | 3 | Suggest fluid change

Fluid contaminated | B | Require flushing and refilling of the system

NOTE: Determine and correct source of contamination. OEM specifications must be followed for fluid type.

Fluid contaminated | B | Require flushing and refilling of the system

NOTE: Determine and correct source of contamination. OEM specifications must be followed for fluid type.

Fluid level incorrect | B | Require adjustment of fluid level

Leaking | B | Require repair or replacement

Noisy | 2 | Suggest repair or replacement

Pulley bent | A | Require repair or replacement of pulley

Pulley missing | C | Require replacement of pulley

Pump output out of manufacturer's specifications | A | Require repair or replacement

Remote reservoir leaking | A | Require replacement of reservoir

Reservoir cap broken | A | Require replacement of cap

Reservoir cap missing | C | Require replacement of cap

Seized | A | Require replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement
````

## Chunk 8657: Idler Arms

- Title: Idler Arms
- Source path: `pages\11152.html`
- Chunk ID: `chunk_212e950f5bf1`
- Images: none
- Duplicate sources: `pages\19925.html`

### Full Text

````text
# Idler Arms

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Binding | A | Further inspection required

NOTE: If greaseable, grease joint. If problem persists or joint is non-greaseable, require replacement.

Grease boot cracked | B | Require replacement of boot

NOTE: If boot is not available as a separate component, suggest replacement of idler arm (reason code 2). Cracked grease boot will allow contaminants to enter joint and will accelerate wear.

Grease boot missing | C | Require replacement of boot

NOTE: If boot is not available as a separate component, suggest replacement of idler arm (reason code 2). Lack of grease boot will allow contaminants to enter joint and will accelerate wear.

Grease boot torn | A | Require replacement of boot

NOTE: If boot is not available as a separate component, suggest replacement of idler arm (reason code 2). Torn grease boot will allow contaminants to enter joint and will accelerate wear.

Grease fitting broken | A | Require replacement of grease fitting

Grease fitting missing | C | Require replacement of grease fitting

Grease fitting won't seal | A | Require replacement of grease fitting

Grease seal missing | C | Require replacement of seal

NOTE: If seal is not available as a separate component, suggest replacement of idler arm (reason code 2). Missing grease seal will allow contaminants to enter joint and will accelerate wear.

Grease seal torn | A | Require replacement of seal

NOTE: If seal is not available as a separate component, suggest replacement of idler arm (reason code 2). Torn grease seal will allow contaminants to enter joint and will accelerate wear.

Greaseable joint will not take grease | 2 | Suggest replacement of grease fitting

NOTE: If greaseable joint will not take grease after replacing the grease fitting, suggest replacement of idler arm.

Looseness at frame bracket end | B | Require repair or replacement

NOTE: If manufacturer's procedures and specifications exist, use those procedures and specifications; otherwise, use an approved inspection method such as the dry park check.

NOTE: Looseness is defined as movement that creates excessive toe change.

Looseness at link end (perceptible horizontal movement) | 1 | Suggest replacement

NOTE: If manufacturer's procedures for inspection exist, use those procedures; otherwise, use an approved inspection method such as the dry park check. Do not use pliers or pry bar to check ball and socket movement. Use only moderate hand pressure.

Looseness at link end that is excessive | B | Require replacement

NOTE: Excessive looseness is defined as significant enough to affect vehicle handling or structural integrity. If manufacturer's procedures for inspection exist, use those procedures; otherwise, use an approved inspection method such as the dry park check.

CAUTION: Do not use pliers or pry bar to check ball and socket movement. Use only moderate hand pressure.

Mounted out of position (center link not parallel) | B | Require repositioning

Nut on stud loose | A | Require repair or replacement

NOTE: Check for bent stud or damaged taper hole.

Seized | A | Require replacement

Stud bent | B | Require replacement

NOTE: Check for damaged taper hole.

Stud broken | A | Require replacement

NOTE: Check for damaged taper hole.

Taper hole elongated | A | Require replacement

NOTE: Check for damaged stud.

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

NOTE: Check for damaged taper hole.

Wear exceeds manufacturer's specifications | B | Require replacement
````

## Chunk 8658: Intermediate Shaft U-Joints

- Title: Intermediate Shaft U-Joints
- Source path: `pages\11153.html`
- Chunk ID: `chunk_c356116a7d92`
- Images: none
- Duplicate sources: `pages\19926.html`

### Full Text

````text
# Intermediate Shaft U-Joints

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Flex coupler binding | A | Require repair or replacement of coupler

Flex coupler loose | A | Require repair or replacement of coupler

Flex coupler missing parts | A | Require repair or replacement of coupler

Flex coupler soft/ spongy | A | Require replacement of coupler

Flex coupler tom | A | Require replacement of coupler

Steering coupler shield cracked | 2 | Suggest replacement

Steering coupler shield missing | C | Require replacement

Steering coupler shield torn | 2 | Suggest replacement

U-joint binding | A | Require repair or replacement of joint

U-joint loose | A | Require repair or replacement of joint
````

## Chunk 8659: King Pins

- Title: King Pins
- Source path: `pages\11154.html`
- Chunk ID: `chunk_d207dbb31ad2`
- Images: none
- Duplicate sources: `pages\19927.html`

### Full Text

````text
# King Pins

Condition | Code | Procedure

Bearing balls pitted | A | Require replacement

Bearing balls worn | A | Require replacement

Bearing races pitted | A | Require replacement

Bearing races worn | A | Require replacement

Bearing rollers pitted | A | Require replacement

Bearing rollers worn | A | Require replacement

Bearing seal bent | 2 | Suggest replacement of seal or bearing

Bearing seal missing | C | Require replacement of seal if available separately or bearing and seal together

Bearing seal torn | A | Require replacement of seal if available separately or bearing and seal together

Binding | A | Require repair or replacement of affected parts

End caps missing | C | Require replacement of missing part, if available; otherwise, replace king pin

End play exceeds specifications | B | Require repair

Grease fitting broken | A | Require replacement of grease fitting

Grease fitting missing | C | Require replacement of grease fitting

Grease fitting will not seal | A | Require replacement of grease fitting

Locating pins missing | C | Require replacement of missing part, if available; otherwise, replace king pin

Looseness exceeds manufacturer's specifications | B | Require replacement of worn parts

Seized | A | Require replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

Will not take grease | 2 | Suggest replacement of grease fitting

NOTE: If king pin will not take grease after replacement of grease fitting, suggest replacement of king pin.
````

## Chunk 8660: Steering And Suspension, Wheel Alignment, Wheels And Tires: Modules

- Title: Steering And Suspension, Wheel Alignment, Wheels And Tires: Modules
- Source path: `pages\11155.html`
- Chunk ID: `chunk_bee7f7b9b857`
- Images: none
- Duplicate sources: `pages\19928.html`

### Full Text

````text
# Steering And Suspension, Wheel Alignment, Wheels And Tires: Modules

Condition | Code | Procedure

Application incorrect | B | Require replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Connector broken | A | Require repair or replacement

Connector melted | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector missing | C | Require repair

Contaminated | A | Require repair or replacement

NOTE: Determine source of contamination, such as engine coolant, fuel, metal particles, or water. Require repair or replacement.

Inoperative | A | Require repair or replacement

NOTE: Inoperative includes intermittent operation. Some components may be serviceable; check for accepted cleaning procedure.

Leaking | B | Require repair or replacement

Malfunctioning | A | Require replacement

NOTE: Includes inoperative, intermittent operation, failure to perform all functions, out of OEM specifications, or out of range.

Missing | C | Require replacement

Terminal broken | A | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead corroded | A | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8661: Pitman Arms

- Title: Pitman Arms
- Source path: `pages\11156.html`
- Chunk ID: `chunk_fb4b6c169c90`
- Images: none
- Duplicate sources: `pages\19929.html`

### Full Text

````text
# Pitman Arms

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Bent, affecting performance | B | Require replacement

Binding | A | Further inspection required

NOTE: If greaseable, grease joint. If problem persists or joint is non-greaseable, require replacement.

Grease boot cracked | 2 | Require replacement of boot

NOTE: If boot is not available as a separate component, suggest replacement of pitman arm (reason code 2). Cracked grease boot will allow contaminants to enter joint and will accelerate wear.

Grease boot missing | C | Require replacement of boot

NOTE: If boot is not available as a separate component, suggest replacement of pitman arm (reason code 2). Lack of grease boot will allow contaminants to enter joint and will accelerate wear.

Grease boot torn | A | Require replacement of boot

NOTE: If boot is not available as a separate component, suggest replacement of pitman arm (reason code 2). Tom grease boot will allow contaminants to enter joint and will accelerate wear.

Grease fitting broken | A | Require replacement grease fitting

Grease fitting missing | C | Require replacement of grease fitting

Grease fitting won't seal | A | Require replacement of grease fitting

Grease seal missing | C | Require replacement of seal

NOTE: If seal is not available as a separate component, suggest replacement of pitman arm (reason code 2). Lack of grease seal will allow contaminants to enter joint and will accelerate wear.

Grease seal torn | A | Require replacement of seal

NOTE: If seal is not available as a separate component, suggest replacement of pitman arm (reason code 2). Tom grease seal will allow contaminants to enter joint and will accelerate wear.

Looseness (perceptible horizontal movement) | 1 | Suggest replacement

NOTE: If manufacturer's procedures for inspection exist, use those procedures; otherwise, use an approved inspection method such as the dry park check. Do not use pliers or pry bar to check ball and socket movement. Use only moderate hand pressure.

Looseness that is excessive | B | Require replacement

NOTE: Excessive looseness is defined as being significant enough to affect vehicle handling or structural integrity. If manufacturer's procedures for inspection exist, use those procedures; otherwise, use an approved inspection method such as the dry park check.

CAUTION: Do not use pliers or pry bar to check ball and socket movement. Use only moderate hand pressure.

Nut on stud loose | A | Require repair or replacement

NOTE: Check for bent stud or damaged taper hole.

Seized | A | Require replacement

Splines damaged | A | Require repair or replacement

Splines stripped (splines missing) | A | Require replacement

Stud bent | B | Require replacement

NOTE: Check for damaged taper hole.

Stud broken | A | Require replacement

NOTE: Check for damaged taper hole.

Stud loose in taper hole | A | Require repair or replacement

NOTE: Check for damaged taper hole.

Taper hole elongated | A | Require replacement

NOTE: Check for damaged stud.

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

NOTE: Check for damaged taper hole.
````

## Chunk 8662: Power Steering Coolers

- Title: Power Steering Coolers
- Source path: `pages\11158.html`
- Chunk ID: `chunk_9fae9f2c8698`
- Images: none
- Duplicate sources: `pages\19931.html`

### Full Text

````text
# Power Steering Coolers

Condition | Code | Procedure

Air flow obstruction | A | Require repair

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Connection leaking | A | Require repair or replacement

Contaminated | A | Require repair or replacement

Corroded | 1 | Suggest repair or replacement

Fins damaged, affecting performance | A | Require repair or replacement

Fins damaged, not affecting performance | No service suggested or required

Internal restrictions | B | Require repair or replacement

Leaking | B | Require repair or replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require repair or replacement

Tubes damaged, affecting performance | A | Require repair or replacement

Tubes damaged, not affecting performance | No service suggested or required
````

## Chunk 8663: Power Steering Lines (Steel)

- Title: Power Steering Lines (Steel)
- Source path: `pages\11161.html`
- Chunk ID: `chunk_b4a0065c9d32`
- Images: none
- Duplicate sources: `pages\19934.html`

### Full Text

````text
# Power Steering Lines (Steel)

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Corroded, affecting structural integrity | A | Require replacement

Fitting incorrect (for example, compression fitting) | B | Require replacement

Flare type incorrect | B | Require repair or replacement

Leaking | A | Require repair or replacement

Line material incorrect (copper, etc. ) | B | Require replacement

Restricted | A | Require replacement

Routed incorrectly (where failure is likely to occur) | B | Require repair or replacement

Rust-pitted, not affecting structural integrity | 1 | Suggest replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement
````

## Chunk 8664: Power Steering Pumps - Electric

- Title: Power Steering Pumps - Electric
- Source path: `pages\11162.html`
- Chunk ID: `chunk_5cd1ee03e7ab`
- Images: none
- Duplicate sources: `pages\19935.html`

### Full Text

````text
# Power Steering Pumps - Electric

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Binding | A | Require repair or replacement

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted | A | Require replacement

NOTE: Determine cause and correct prior to replacement of part.

Connector missing | C | Require replacement

Leaking | B | Require repair or replacement

Noisy | 2 | Suggest repair or replacement

Pulley bent | A | Require repair or replacement of pulley

Pulley missing | C | Require replacement of pulley

Pump output out of manufacturer's specifications | A | Require repair or replacement

Remote reservoir leaking | A | Require replacement of reservoir

Reservoir cap broken | A | Require replacement of cap

Reservoir cap missing | C | Require replacement of cap

Seized | A | Require replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

Wire lead burned | A | Require repair or replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8665: Power Steering Pumps

- Title: Power Steering Pumps
- Source path: `pages\11163.html`
- Chunk ID: `chunk_f72aa5720617`
- Images: none
- Duplicate sources: `pages\19936.html`

### Full Text

````text
# Power Steering Pumps

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Binding | A | Require repair or replacement

Binding | A | Require repair or replacement

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted | A | Require replacement

NOTE: Determine cause and correct prior to replacement of part.

Connector missing | C | Require replacement

Fluid at or beyond service interval | 3 | Suggest fluid change

Fluid contaminated | B | Require flushing and refilling of the system

Fluid level incorrect | B | Require adjustment of fluid level

Leaking | B | Require repair or replacement

Leaking | A | Require repair or replacement

Noisy | 2 | Suggest repair or replacement

Noisy | 2 | Suggest repair or replacement

Pulley bent | A | Require repair or replacement of pulley

Pulley bent | A | Require repair or replacement of pulley

Pulley missing | C | Require replacement of pulley

Pulley missing | C | Require replacement of pulley

Pump output out of manufacturer's specifications | A | Require repair or replacement

Pump output out of manufacturer's specifications | A | Require repair or replacement

Remote reservoir leaking | A | Require replacement of reservoir

Remote reservoir leaking | A | Require replacement of reservoir

Reservoir cap broken | A | Require replacement of cap

Reservoir cap broken | A | Require replacement of cap

Reservoir cap missing | C | Require replacement of cap

Reservoir cap missing | C | Require replacement of cap

Seized | A | Require replacement

Seized | A | Require replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Threads damaged | A | Require repair or replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

Wire lead burned | A | Require repair or replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8666: Radar Sensor

- Title: Radar Sensor
- Source path: `pages\11164.html`
- Chunk ID: `chunk_fe002a8792f3`
- Images: none
- Duplicate sources: `pages\19937.html`

### Full Text

````text
# Radar Sensor

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware corroded, affecting structural integrity | A | Require replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted | A | Require replacement

Connector missing | C | Require replacement

NOTE: Determine cause and correct prior to replacement of part.

Dust boot missing | C | Require replacement of boot

Dust boot split | A | Require replacement of boot

NOTE: If boot is not available separately, suggest replacement of sensor (reason code 2). This condition can lead to damage of the sliding magnet, which, in turn, causes premature sensor failure

Dust boot torn | A | Require replacement of boot

NOTE: If boot is not available separately, suggest replacement of sensor (reason code 2). This condition can lead to damage of the sliding magnet, which, in turn, causes premature sensor failure.

Housing cracked | B | Require replacement

NOTE: If boot is not available separately, suggest replacement of sensor (reason code 2). This condition can lead to damage of the sliding magnet, which, in turn, causes premature sensor failure.

Lead routing incorrect | B | Require rerouting according to vehicle manufacturer's specifications

Loose | B | Require adjustment to vehicle manufacturer's specifications

Missing | C | Require replacement

Output signal incorrect | B | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Wire lead burned | A | Require repair or replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8667: Radius Arms

- Title: Radius Arms
- Source path: `pages\11165.html`
- Chunk ID: `chunk_60953ec77d42`
- Images: none
- Duplicate sources: `pages\19938.html`

### Full Text

````text
# Radius Arms

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Bent, affecting performance | B | Require replacement

Corroded, affecting structural integrity | a | Require replacement

Holes distorted | A | Require replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement
````

## Chunk 8668: Relay Rods

- Title: Relay Rods
- Source path: `pages\11166.html`
- Chunk ID: `chunk_b853b3919886`
- Images: none
- Duplicate sources: `pages\19939.html`

### Full Text

````text
# Relay Rods

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Bent, affecting performance | B | Require replacement

Binding | A | Further inspection required

NOTE: If greaseable, grease joint. If problem persists or joint is non-greaseable, require replacement.

Grease boot cracked | B | Require replacement of boot

NOTE: If boot is not available as a separate component, suggest replacement of relay rod (reason code 2). Cracked grease boot will allow contaminants to enter the joint and will accelerate wear.

Grease boot missing | C | Require replacement of boot

NOTE: If boot is not available as a separate component, suggest replacement of relay rod (reason code 2). Lack of grease boot will allow contaminants to enter the joint and will accelerate wear.

Grease boot torn | A | Require replacement of boot

NOTE: If boot is not available as a separate component, suggest replacement of center link (reason code 2). Torn grease boot will allow contaminants to enter the joint and will accelerate wear.

Grease fitting broken | A | Require replacement of grease fitting

Grease fitting missing | C | Require replacement of grease fitting

Grease fitting won't seal | A | Require replacement of grease fitting

Grease seal missing | C | Require replacement of seal

NOTE: If seal is not available as a separate component, suggest replacement of relay rod (reason code 2). Lack of grease seal will allow contaminants to enter the joint and will accelerate wear.

Grease seal torn | A | Require replacement of seal

NOTE: If seal is not available as a separate component, suggest replacement of relay rod (reason code 2). Torn grease seal will allow contaminants to enter the joint and will accelerate wear.

Greaseable relay rod will not take grease | 2 | Suggest replacement of grease fitting

NOTE: If greaseable relay rod still will not take grease after replacing the grease fitting, suggest replacement of relay rod.

Looseness (perceptible horizontal movement) | 1 | Suggest replacement

NOTE: If manufacturer's procedures for inspection exist, use those procedures; otherwise, use an approved inspection method such as the dry park check. Do not use pliers or pry bar to check ball and socket movement. Use only moderate hand pressure.

Looseness that is excessive | B | Require replacement

NOTE: Excessive looseness is defined as being significant enough to affect vehicle handling or structural integrity. If manufacturer's procedures for inspection exist, use those procedures; otherwise, use an approved inspection method such as the dry park check.

CAUTION: Do not use pliers or pry bar to check ball and socket movement. Use only moderate hand pressure.

Seized | A | Require replacement

Stud bent | B | Require replacement

NOTE: Check for damaged taper hole.

Stud broken | A | Require replacement

NOTE: Check for damaged taper hole.

Stud loose in taper hole | A | Require repair or replacement

NOTE: Check for damaged taper hole.

Taper hole elongated | A | Require replacement

NOTE: Check for damaged stud.

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

NOTE: Check for damaged taper hole.

Wear exceeds manufacturer's specifications | B | Require replacement
````

## Chunk 8669: Steering And Suspension, Wheel Alignment, Wheels And Tires: Relays

- Title: Steering And Suspension, Wheel Alignment, Wheels And Tires: Relays
- Source path: `pages\11167.html`
- Chunk ID: `chunk_582aefffd4b1`
- Images: none
- Duplicate sources: `pages\19940.html`

### Full Text

````text
# Steering And Suspension, Wheel Alignment, Wheels And Tires: Relays

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Housing broken | A | Require replacement

Housing cracked | 2 | Suggest replacement

Inoperative | A | Require replacement

NOTE: Inoperative includes intermittent operation.

Missing | C | Require replacement

Terminal broken | A | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement
````

## Chunk 8670: Steering And Suspension, Wheel Alignment, Wheels And Tires: Sensors

- Title: Steering And Suspension, Wheel Alignment, Wheels And Tires: Sensors
- Source path: `pages\11168.html`
- Chunk ID: `chunk_c76f78542b62`
- Images: none
- Duplicate sources: `pages\19941.html`

### Full Text

````text
# Steering And Suspension, Wheel Alignment, Wheels And Tires: Sensors

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector missing | C | Require replacement

Inoperative | A | Require repair or replacement

NOTE: Inoperative includes intermittent operation or out of specification.

Leaking (vacuum/fluid/air) | A | Require replacement

Out of adjustment | B | Further inspection required

NOTE: Follow OEM recommended adjustment procedures. Repair or replace if out of specification.

Terminal broken | A | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

Wire lead burned | A | Require repair or replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8671: Steering And Suspension, Wheel Alignment, Wheels And Tires: Spindles

- Title: Steering And Suspension, Wheel Alignment, Wheels And Tires: Spindles
- Source path: `pages\11170.html`
- Chunk ID: `chunk_d565793bab8d`
- Images: none
- Duplicate sources: `pages\19943.html`

### Full Text

````text
# Steering And Suspension, Wheel Alignment, Wheels And Tires: Spindles

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Bent | B | Require replacement

Broken | A | Require replacement

Pinch bolt bent | B | Require replacement

Pinch bolt incorrect | B | Require replacement with bolt that meets OEM design

Pinch bolt loose | B | Require repair

Pinch bolt missing | C | Require replacement

Pinch bolt tabs deformed (gap closer together than allowed by OEM specification, typically minimum .032"" gap before clamping) | B | Require replacement

NOTE: Steering knuckle deformation can cause pinch bolt breakage.

Race seat area undersized | B | Require replacement

Scored | A | Require repair or replacement

Taper hole elongated | A | Require replacement

NOTE: Check for damaged stud.

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement
````

## Chunk 8672: Springs, Coil, Leaf And Torsion Bars

- Title: Springs, Coil, Leaf And Torsion Bars
- Source path: `pages\11171.html`
- Chunk ID: `chunk_89c5488985ff`
- Images: none
- Duplicate sources: `pages\19944.html`

### Full Text

````text
# Springs, Coil, Leaf And Torsion Bars

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware corroded, affecting structural integrity | A | Require replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Broken (all springs except secondary leave(s) on multi-leaf springs) | A | Require replacement

Coil clash | Further inspection required

NOTE: Require ride height check and inspection of strike out Jounce) bumper. If vehicle is within manufacturer's height specifications, no service is suggested or required.

Coil spring insulator deteriorated | 2 | Suggest replacement of insulator

Coil spring insulator missing | C | Require replacement of insulator

Coil spring insulator split | 2 | Suggest replacement of insulator

Coil spring plastic coating deteriorated - rust present | A | Refer to manufacturer's service requirements

NOTE: Some manufacturers require replacement under these conditions.

Composite spring damaged | Further inspection required

NOTE: Check vehicle ride height. If ride height is OK, no service is suggested or required.

Cracked (all springs except composite leaf and secondary leave(s) on multileaf springs) | A | Require replacement

Installed incorrectly | B | Require repair

Leaf spring insulators missing | C | Require replacement of insulators

Secondary leaf on multi-leaf spring broken | 1 | Suggest repair or replacement

Secondary leaf on multi-leaf spring cracked | 1 | Suggest repair or replacement

Torsion bar adjuster bent | A | Require repair or replacement of adjuster

NOTE: Only required if ride height needs to be adjusted.

Torsion bar adjuster seized | A | Require repair or replacement of adjuster

NOTE: Only required if ride height needs to be adjusted.

Torsion bar adjuster threads damaged | A | Require repair or replacement of part with damaged threads

NOTE: Only required if ride height needs to be adjusted.

Torsion bar adjuster threads stripped (threads missing) | A | Require replacement of part with stripped threads

Vehicle suspension height not within OEM specifications | A | Require adjustment or replacement
````

## Chunk 8673: Steering Angle Sensor

- Title: Steering Angle Sensor
- Source path: `pages\11174.html`
- Chunk ID: `chunk_07b58e4c6a52`
- Images: none
- Duplicate sources: `pages\19947.html`

### Full Text

````text
# Steering Angle Sensor

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware corroded, affecting structural integrity | A | Require replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted | A | Require replacement

Connector missing | C | Require replacement

NOTE: Determine cause and correct prior to replacement of part.

Dust boot missing | C | Require replacement of boot

Dust boot split | A | Require replacement of boot

NOTE: If boot is not available separately, suggest replacement of sensor (reason code 2). This condition can lead to damage of the sliding magnet, which, in turn, causes premature sensor failure

Dust boot torn | A | Require replacement of boot

NOTE: If boot is not available separately, suggest replacement of sensor (reason code 2). This condition can lead to damage of the sliding magnet, which, in turn, causes premature sensor failure.

Housing cracked | B | Require replacement

NOTE: If boot is not available separately, suggest replacement of sensor (reason code 2). This condition can lead to damage of the sliding magnet, which, in turn, causes premature sensor failure.

Lead routing incorrect | B | Require rerouting according to vehicle manufacturer's specifications

Loose | B | Require adjustment to vehicle manufacturer's specifications

Missing | C | Require replacement

Output signal incorrect | B | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Wire lead burned | A | Require repair or replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8674: Steering Arms

- Title: Steering Arms
- Source path: `pages\11175.html`
- Chunk ID: `chunk_eefe209a7b17`
- Images: none
- Duplicate sources: `pages\19948.html`

### Full Text

````text
# Steering Arms

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Bent | B | Require replacement

Broken | A | Require replacement

Pinch bolt bent | B | Require replacement

Pinch bolt incorrect | B | Require replacement with bolt that meets OEM design

Pinch bolt loose | B | Require repair

Pinch bolt missing | C | Require replacement

Pinch bolt tabs deformed (gap closer together than allowed by OEM specification, typically minimum .032"" gap before clamping) | B | Require replacement

NOTE: Steering knuckle deformation can cause pinch bolt breakage.

Race seat area undersized | B | Require replacement

Scored | A | Require repair or replacement

Taper hole elongated | A | Require replacement

NOTE: Check for damaged stud.

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement
````

## Chunk 8675: Steering Couplers

- Title: Steering Couplers
- Source path: `pages\11176.html`
- Chunk ID: `chunk_b0c5cf72b8d0`
- Images: none
- Duplicate sources: `pages\19949.html`

### Full Text

````text
# Steering Couplers

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Flex coupler binding | A | Require repair or replacement of coupler

Flex coupler loose | A | Require repair or replacement of coupler

Flex coupler missing parts | A | Require repair or replacement of coupler

Flex coupler soft/ spongy | A | Require replacement of coupler

Flex coupler tom | A | Require replacement of coupler

Steering coupler shield cracked | 2 | Suggest replacement

Steering coupler shield missing | C | Require replacement

Steering coupler shield torn | 2 | Suggest replacement

U-joint binding | A | Require repair or replacement of joint

U-joint loose | A | Require repair or replacement of joint
````

## Chunk 8676: Steering Dampers

- Title: Steering Dampers
- Source path: `pages\11177.html`
- Chunk ID: `chunk_1164f05fa6af`
- Images: none
- Duplicate sources: `pages\19950.html`

### Full Text

````text
# Steering Dampers

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware corroded, affecting structural integrity | A | Require replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Binding | A | Require replacement

Damper body dented | A | Further inspection required

NOTE: Require replacement of units where dents restrict damper piston rod movement. If dents don't restrict movement, no service is suggested or required. Especially critical on mono-tube dampers.

Damper body punctured | A | Require replacement

Damping (none) | A | Require replacement

Dust boot (bellows) missing | C | Require replacement of boot

NOTE: If boot is not available separately, suggest replacement of steering damper ( reason code 2). This condition can lead to damage of the piston rod, which, in turn, causes premature piston rod seal wear.

Dust boot (bellows) split | A | Require replacement of boot

NOTE: If boot is not available separately, suggest replacement of steering damper ( reason code 2). This condition can lead to damage of the piston rod, which, in turn, causes premature piston rod seal wear.

Dust shield broken | 2 | Suggest replacement

NOTE: This condition can lead to damage of the piston rod, which, in turn, causes premature piston rod seal wear.

Dust shield missing | 2 | Suggest replacement

NOTE: This condition can lead to damage of the piston rod, which, in turn, causes premature piston rod seal wear.

Leaking oil, enough for fluid to be running down the body | A | Require replacement

Loose | A | Require repair or replacement

Missing | C | Require replacement

Noise | 2 | Further inspection required

NOTE: If noise is isolated to damper, suggest replacement.

Piston rod bent | A | Require replacement

Piston rod broken | A | Require replacement

Piston rod has surface defect | 2 | Suggest replacement

Piston rod threads damaged | A | Require repair or replacement

Piston rod threads stripped (threads missing), affecting performance | A | Require replacement

NOTE: Only required if condition affects structural integrity or if unit needs to be serviced.

Seized | A | Require replacement
````

## Chunk 8677: Steering Gears (Except Rack And Pinion)

- Title: Steering Gears (Except Rack And Pinion)
- Source path: `pages\11178.html`
- Chunk ID: `chunk_2bf8d1ec5e2d`
- Images: none
- Duplicate sources: `pages\19951.html`

### Full Text

````text
# Steering Gears (Except Rack And Pinion)

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Binding | A | Require repair or replacement

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted | A | Require replacement

NOTE: Determine cause and correct prior to replacement of part.

Fluid contaminated | B | Require flushing and refilling of the system

NOTE: Determine and correct source of contamination. OEM specifications must be followed for fluid type.

Gasket leaking | A | Require repair or replacement of gasket

Housing leaking | A | Require replacement

Hydraulic fittings leaking | A | Require repair or replacement of fittings

Inadequate power assist | A | Further inspection required

NOTE: If steering gear is source of inadequate assist, require repair or replacement.

Lash exceeds manufacturer's specifications | B | Require repair or replacement

Malfunctioning | A | Require repair or replacement

NOTE: Includes inoperative, intermittent operation, failure to perform all functions, out of OEM specification, or out of range.

Seal leaking | A | Require repair or replacement of seal and / or mating part

Splines damaged | A | Require repair or replacement of splines

Splines stripped | A | Require replacement of splines

Steering coupler shield cracked | 2 | Suggest replacement

Steering coupler shield missing | C | Require replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Threads damaged | A | Require repair or replacement of part with damaged threads

Threads stripped (threads missing) | A | Require replacement of part with stripped threads

Unequal power assist | A | Require repair or replacement

Wire lead burned | A | Require repair or replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8678: Steering Gears, Rack And Pinion

- Title: Steering Gears, Rack And Pinion
- Source path: `pages\11179.html`
- Chunk ID: `chunk_ba2e5c509e5e`
- Images: none
- Duplicate sources: `pages\19952.html`

### Full Text

````text
# Steering Gears, Rack And Pinion

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Balance tube blocked | A | Require repair or replacement of balance tube

Balance tube missing | C | Require replacement of balance tube

Balance tube restricted | A | Require repair or replacement of balance tube

Bellows boot clamp missing | C | Require replacement of clamp

Bellows boot cracked (not through) | 2 | Suggest replacement of bellows boot

Bellows boot missing | C | Require replacement of bellows boot

Bellows boot not sealing | A | Require repair or replacement of bellows boot

Bellows boot torn | A | Require replacement of bellows boot

Bellows boot twisted (from toe adjustment) | B | Require repair

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted | A | Require replacement

NOTE: Determine cause and correct prior to replacement of part.

Connector missing | C | Require replacement

Fitting leaking | A | Require repair or replacement

Fitting missing | A | Require replacement of fitting

Fitting threads damaged | A | Require repair or replacement of part with damaged threads

Fitting threads stripped (threads missing) | A | Require replacement of part with stripped threads

Fluid contaminated | B | Require flushing and refilling of the system

NOTE: Determine and correct source of contamination. OEM specifications must be followed for fluid type.

Gasket leaking | A | Require repair or replacement

Housing cracked, affecting structural integrity | B | Require replacement

Housing leaking | A | Require replacement

Inadequate power assist | A | Further inspection required

NOTE: If steering gear is source of inadequate assist, require repair or replacement.

Lash exceeds manufacturer's specifications | B | Require repair or replacement

Malfunctioning | A | Require repair or replacement

NOTE: Includes inoperative, intermittent operation, failure to perform all functions, out of OEM specification, or out of range.

Seal leaking | A | Require repair or replacement

Splines damaged | A | Require repair or replacement

Splines stripped (splines missing) | A | Require replacement

Steel line blocked | A | Require repair or replacement of line

Steel line leaking | A | Require repair or replacement of line

Steel line missing | C | Require replacement of line

Steel line restricted | A | Require repair or replacement of line

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Threads damaged | A | Require repair or replacement of part with damaged threads

Threads stripped (threads missing) | A | Require replacement of part with stripped threads

Unequal power assist | A | Require repair or replacement

Wire lead burned | A | Require repair or replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8679: Steering Knuckles

- Title: Steering Knuckles
- Source path: `pages\11180.html`
- Chunk ID: `chunk_3fbd5c4878fc`
- Images: none
- Duplicate sources: `pages\19953.html`

### Full Text

````text
# Steering Knuckles

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Bent | B | Require replacement

Broken | A | Require replacement

Pinch bolt bent | B | Require replacement

Pinch bolt incorrect | B | Require replacement with bolt that meets OEM design

Pinch bolt loose | B | Require repair

Pinch bolt missing | C | Require replacement

Pinch bolt tabs deformed (gap closer together than allowed by OEM specification, typically minimum .032"" gap before clamping) | B | Require replacement

NOTE: Steering knuckle deformation can cause pinch bolt breakage.

Race seat area undersized | B | Require replacement

Scored | A | Require repair or replacement

Taper hole elongated | A | Require replacement

NOTE: Check for damaged stud.

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement
````

## Chunk 8680: Strike Out Bumpers

- Title: Strike Out Bumpers
- Source path: `pages\11181.html`
- Chunk ID: `chunk_003fe8189530`
- Images: none
- Duplicate sources: `pages\19954.html`

### Full Text

````text
# Strike Out Bumpers

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware corroded, affecting structural integrity | A | Require replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Missing | C | Require replacement

Split | A | Suggest replacement
````

## Chunk 8681: Strut Bearing Plate Assemblies

- Title: Strut Bearing Plate Assemblies
- Source path: `pages\11182.html`
- Chunk ID: `chunk_f5e6a2788b21`
- Images: none
- Duplicate sources: `pages\19955.html`

### Full Text

````text
# Strut Bearing Plate Assemblies

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Axial or radial movement exceeds vehicle manufacturer's specifications | B | Require replacement

Bearing binding | A | Require replacement of bearing

Bearing missing | C | Require replacement of bearing

Bearing seized | A | Require replacement of bearing

Bent, affecting performance | B | Require replacement

Corroded, affecting structural integrity | A | Require replacement

Holes distorted | A | Require replacement

Missing | C | Require replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement
````

## Chunk 8682: Suspension Pumps (Hydraulic)

- Title: Suspension Pumps (Hydraulic)
- Source path: `pages\11184.html`
- Chunk ID: `chunk_104f8ebb29ec`
- Images: none
- Duplicate sources: `pages\19957.html`

### Full Text

````text
# Suspension Pumps (Hydraulic)

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Binding | A | Require repair or replacement

Fluid at or beyond service interval | 3 | Suggest fluid change

Fluid contaminated | B | Require flushing and refilling of the system

NOTE: Determine and correct source of contamination. OEM specifications must be followed for fluid type.

Fluid level incorrect | B | Require adjustment of fluid level

Leaking | B | Require repair or replacement

Noisy | 2 | Suggest repair or replacement

Pulley bent | A | Require repair or replacement of pulley

Pulley missing | C | Require replacement of pulley

Pump output out of manufacturer's specifications | A | Require repair or replacement

Remote reservoir leaking | A | Require replacement of reservoir

Reservoir cap broken | A | Require replacement of cap

Reservoir cap missing | C | Require replacement of cap

Seized | A | Require replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement
````

## Chunk 8683: Sway Bar Links

- Title: Sway Bar Links
- Source path: `pages\11185.html`
- Chunk ID: `chunk_00a63d3e9a42`
- Images: none
- Duplicate sources: `pages\19958.html`

### Full Text

````text
# Sway Bar Links

Condition | Code | Procedure

Attaching (mating) hole distorted | A | Require repair or replacement of bracket or control arm

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Ball and socket has looseness (perceptible vertical movement) | 1 | Suggest replacement

NOTE: If manufacturer's procedures for inspection exist, use those procedures; otherwise, use an approved inspection method. Do not use pliers or pry bar to check ball and socket movement. Use only moderate hand pressure.

Ball and socket has looseness that is excessive | B | Require replacement

NOTE: Excessive looseness is defined as being significant enough to affect vehicle handling or structural integrity. If manufacturer's procedures for inspection exist, use those procedures; otherwise, use an approved inspection method.

CAUTION: Do not use pliers or pry bar to check ball and socket movement. Use only moderate hand pressure.

Bent | B | Require replacement

Broken | A | Require replacement

Bushing cracked | A | Require replacement

Bushing deteriorated, affecting performance | A | Require repair or replacement

NOTE: If condition is caused by oil-soaking, further inspection is required to determine source of oil.

Bushing distorted, affecting performance | A | Require repair or replacement

Bushing missing | C | Require replacement

Bushing oil-soaked, affecting performance | A | Require replacement

NOTE: Further inspection required to determine source of oil.

Bushing shows surface cracking (weather-checked) | No service suggested or required

Bushing split | A | Require replacement

Corroded, affecting structural integrity | A | Require replacement

Grease boot cracked | 2 | Suggest replacement

NOTE: Cracked grease boot will allow contaminants to enter the joint and will accelerate wear .

Grease boot missing | C | Require replacement of boot

NOTE: If boot is not available separately, suggest replacement of sway bar link (reason code 2). Lack of grease boot will allow contaminants to enter the joint and will accelerate wear.

Grease boot torn | A | Require replacement of boot

NOTE: If boot is not available separately, suggest replacement of sway bar link (reason code 2). Lack of grease boot will allow contaminants to enter the joint and will accelerate wear.

Mating (attaching) hole distorted | A | Require repair or replacement of bracket or control arm

Missing | C | Require replacement

Nut on stud loose | A | Require repair

NOTE: Check for bent stud or damaged mating hole.

Stud bent | B | Require replacement

NOTE: Check for damaged mating hole.

Stud broken | A | Require replacement

NOTE: Check for damaged mating hole.

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

NOTE: Check for damaged mating hole.
````

## Chunk 8684: Sway Bar Mounting Bushings

- Title: Sway Bar Mounting Bushings
- Source path: `pages\11186.html`
- Chunk ID: `chunk_33a534350d14`
- Images: none
- Duplicate sources: `pages\19959.html`

### Full Text

````text
# Sway Bar Mounting Bushings

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Binding | A | Require repair or replacement

Deteriorated, affecting performance | A | Require repair or replacement

NOTE: If condition is caused by oil-soaking, further inspection is required to determine source of oil.

Distorted, affecting performance | A | Require repair or replacement

Leaking (fluid-filled type) | A | Require replacement

Missing | C | Require replacement

Noisy | 2 | Further inspection required

NOTE: If noise isolated to bushing, suggest repair or replacement. Use only approved lubricant on rubber bushings. Petroleum-based lubricants may damage rubber bushings.

Oil-soaked, affecting performance | A | Require replacement

NOTE: Further inspection required to determine source of oil.

Rubber separating from internal metal sleeve on bonded bushing | A | Require replacement

Seized | A | Require replacement

Shifted (out of position) | B | Require repair or replacement

Split | A | Require replacement

Surface cracking (weather-checked) | No service suggested or required
````

## Chunk 8685: Sway Bars

- Title: Sway Bars
- Source path: `pages\11187.html`
- Chunk ID: `chunk_d198d5941cab`
- Images: none
- Duplicate sources: `pages\19960.html`

### Full Text

````text
# Sway Bars

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware corroded, affecting structural integrity | A | Require replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Bent | B | Require replacement

Broken | A | Require replacement

Sway bar corroded at point of attachment to frame bushing | A | Require repair or replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement
````

## Chunk 8686: Steering And Suspension, Wheel Alignment, Wheels And Tires: Switches

- Title: Steering And Suspension, Wheel Alignment, Wheels And Tires: Switches
- Source path: `pages\11188.html`
- Chunk ID: `chunk_901e9fb67e60`
- Images: none
- Duplicate sources: `pages\19961.html`

### Full Text

````text
# Steering And Suspension, Wheel Alignment, Wheels And Tires: Switches

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Binding, affecting performance | A | Require repair or replacement

Binding, not affecting performance | 2 | Suggest repair or replacement

Broken | A | Require repair or replacement

Burned, affecting performance | 2 | Suggest repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Burned, not affecting performance | 1 | Determine cause and correct prior to repair or replacement of part

Cracked, affecting performance | A | Require repair or replacement

Cracked, not affecting performance | 1 | Suggest repair or replacement

Leaking | B | Require repair or replacement

Malfunctioning | A | Require repair or replacement

NOTE: Includes inoperative, intermittent operation, or failure to perform all functions.

Melted, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Melted, not affecting performance | 2 | Determine cause and correct prior to repair or replacement of part

Missing | C | Require replacement

Out of adjustment | B | Require repair or replacement

Terminal broken | A | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Won't return | A | Require repair or replacement

Worn | 1 | Suggest replacement
````

## Chunk 8687: Tie Rod Ends (Inner And Outer)

- Title: Tie Rod Ends (Inner And Outer)
- Source path: `pages\11189.html`
- Chunk ID: `chunk_8ba1140e1004`
- Images: none
- Duplicate sources: `pages\19962.html`

### Full Text

````text
# Tie Rod Ends (Inner And Outer)

Condition | Code | Procedure

Adjusting sleeve bent | B | Require replacement of sleeve

Adjusting sleeve clamps out of position | B | Require repair

Adjusting sleeve corroded, affecting structural integrity | A | Require replacement of sleeve

Adjusting sleeve missing | C | Require replacement of sleeve

Adjusting sleeve seized | A | Require repair or replacement

NOTE: Only required if toe needs to be adjusted.

Adjusting sleeve threads damaged | A | Require repair or replacement of sleeve

Adjusting sleeve threads stripped (threads missing) | A | Require replacement of sleeve

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Bent | A | Require replacement

Binding | A | Further inspection required

NOTE: If greaseable, grease joint. If problem persists or joint is non-greaseable, require replacement.

Grease boot cracked | 2 | Suggest replacement of boot

NOTE: If boot is not available separately, suggest replacement of tie rod end (reason code 2). Cracked grease boot will allow contaminants to enter joint and will accelerate wear.

Grease boot missing | C | Require replacement of boot

NOTE: If boot is not available separately, suggest replacement of tie rod end (reason code 2). Lack of grease boot will allow contaminants to enter joint and will accelerate wear.

Grease boot torn | A | Require replacement of boot

NOTE: If boot is not available separately, suggest replacement of tie rod end (reason code 2). Torn grease boot will allow contaminants to enter joint and will accelerate wear.

Grease fitting broken | A | Require replacement of grease fitting

Grease fitting missing | C | Require replacement of grease fitting

Grease fitting won't seal | A | Require replacement of grease fitting

Grease seal missing | C | Require replacement of seal

NOTE: If seal is not available separately, suggest replacement of tie rod end ( reason code 2). Lack of grease seal will allow contaminants to enter joint and will accelerate wear.

Grease seal torn | A | Require replacement of seal

NOTE: If seal is not available separately, suggest replacement of tie rod end (reason code 2), wear. Torn grease seal will allow contaminants to enter joint and will accelerate wear.

Greaseable tie rod end won't take grease | 2 | Suggest replacement of grease fitting

NOTE: If greaseable tie rod end will not take grease after replacing the grease fitting, suggest replacement of tie rod end.

Looseness (perceptible horizontal movement) | 1 | Suggest replacement

NOTE: If manufacturer's procedures for inspection exist, use those procedures; otherwise, use an approved inspection method such as the dry park check. Do not use pliers or pry bar to check ball and socket movement. Use only moderate hand pressure.

Looseness exceeds manufacturer's specifications | B | Require replacement

Looseness that is excessive | B | Require replacement

NOTE: Excessive looseness is defined as being significant enough to affect vehicle handling or structural integrity. If manufacturer's procedures for inspection exist, use those procedures; otherwise, use an approved inspection method such as the dry park check.

CAUTION: Do not use pliers or pry bar to check ball and socket movement. Use only moderate hand pressure.

Noisy | 2 | Further inspection required

NOTE: If greaseable, grease joint. If problem persists or joint is non-greaseable, suggest replacement.

Nut on stud loose | A | Require repair or replacement

NOTE: Check for bent stud or damaged taper hole.

Seized | A | Require replacement

Stud bent | B | Require replacement

NOTE: Check for damaged taper hole.

Stud broken | A | Require replacement

NOTE: Check for damaged taper hole.

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

NOTE: Check for damaged taper hole.
````

## Chunk 8688: Torque Sensor

- Title: Torque Sensor
- Source path: `pages\11193.html`
- Chunk ID: `chunk_fe6b5073fe8c`
- Images: none
- Duplicate sources: `pages\19966.html`

### Full Text

````text
# Torque Sensor

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted | A | Require repair or replacement

Connector missing | C | Require replacement

Inoperative | A | Require repair or replacement

Leaking (vacuum/fluid/air) | A | Require replacement

Out of adjustment | B | Further inspection required

Terminal broken | A | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

Wire lead burned | A | Require repair or replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8689: Torsion Springs

- Title: Torsion Springs
- Source path: `pages\11194.html`
- Chunk ID: `chunk_8b7605e13106`
- Images: none
- Duplicate sources: `pages\19967.html`

### Full Text

````text
# Torsion Springs

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Broken | A | Require replacement

Missing | C | Require replacement
````

## Chunk 8690: Track Bar Bushings

- Title: Track Bar Bushings
- Source path: `pages\11195.html`
- Chunk ID: `chunk_e8f797841886`
- Images: none
- Duplicate sources: `pages\19968.html`

### Full Text

````text
# Track Bar Bushings

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Binding | A | Require repair or replacement

Deteriorated, affecting performance | A | Require repair or replacement

NOTE: If condition is caused by oil-soaking, further inspection is required to determine source of oil.

Distorted, affecting performance | A | Require repair or replacement

Leaking (fluid-filled type) | A | Require replacement

Missing | C | Require replacement

Noisy | 2 | Further inspection required

NOTE: If noise isolated to bushing, suggest repair or replacement. Use only approved lubricant on rubber bushings. Petroleum-based lubricants may damage rubber bushings.

Oil-soaked, affecting performance | A | Require replacement

NOTE: Further inspection required to determine source of oil.

Rubber separating from internal metal sleeve on bonded bushing | A | Require replacement

Seized | A | Require replacement

Shifted (out of position) | B | Require repair or replacement

Split | A | Require replacement

Surface cracking (weather-checked) | No service suggested or required
````

## Chunk 8691: Track Bars

- Title: Track Bars
- Source path: `pages\11196.html`
- Chunk ID: `chunk_be7c0aaf8406`
- Images: none
- Duplicate sources: `pages\19969.html`

### Full Text

````text
# Track Bars

Condition | Code | Procedure

Attaching (mating) hole distorted | A | Require repair or replacement of bracket or frame

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Bent, affecting performance | B | Require replacement

Corroded, affecting structural integrity | A | Require replacement

Grease boot cracked | 2 | Suggest replacement of boot

NOTE: If boot is not available separately, suggest replacement of tie rod end (reason code 2). Cracked grease boot will allow contaminants to enter joint and will accelerate wear .

Grease boot missing | C | Require replacement of boot

NOTE: If boot is not available separately, suggest replacement of track bar (reason code 2). Lack of grease boot will allow contaminants to enter joint and will accelerate wear.

Grease boot torn | A | Require replacement of boot

NOTE: If boot is not available separately, suggest replacement of track bar (reason code 2). Torn grease boot will allow contaminants to enter joint and will accelerate wear.

Holes distorted | A | Require replacement

Looseness (perceptible horizontal movement) | 1 | Suggest replacement

NOTE: If manufacturer's procedures for inspection exist, use those procedures; otherwise, use an approved inspection method such as the dry park check. Do not use pliers or pry bar to check ball and socket movement. Use only moderate hand pressure.

Looseness that is excessive | B | Require replacement

NOTE: Excessive looseness is defined as being significant enough to affect vehicle handling or structural integrity. If manufacturer's procedures 'for inspection exist, use those procedures; otherwise, use an approved inspection method such as the dry park check.

CAUTION: Do not use pliers or pry bar to check ball and socket movement. Use only moderate hand pressure.

Mating (attaching) hole distorted | A | Require repair or replacement of bracket or frame

Nut on stud loose | A | Require repair or replacement of nut

NOTE: Check for bent stud or damaged mating hole.

Seized | A | Require replacement

Stud bent | B | Require replacement

NOTE: Check for damaged mating hole.

Stud broken | A | Require replacement

NOTE: Check for damaged mating hole.

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement

NOTE: Check for damaged mating hole.

Wear exceeds manufacturer's specifications | B | Require replacement
````

## Chunk 8692: Trailing Arm Bushings

- Title: Trailing Arm Bushings
- Source path: `pages\11197.html`
- Chunk ID: `chunk_ddf650863900`
- Images: none
- Duplicate sources: `pages\19970.html`

### Full Text

````text
# Trailing Arm Bushings

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Binding | A | Require repair or replacement

Deteriorated, affecting performance | A | Require repair or replacement

NOTE: If condition is caused by oil-soaking, further inspection is required to determine source of oil.

Distorted, affecting performance | A | Require repair or replacement

Leaking (fluid-filled type) | A | Require replacement

Missing | C | Require replacement

Noisy | 2 | Further inspection required

NOTE: If noise isolated to bushing, suggest repair or replacement. Use only approved lubricant on rubber bushings. Petroleum-based lubricants may damage rubber bushings.

Oil-soaked, affecting performance | A | Require replacement

NOTE: Further inspection required to determine source of oil.

Rubber separating from internal metal sleeve on bonded bushing | A | Require replacement

Seized | A | Require replacement

Shifted (out of position) | B | Require repair or replacement

Split | A | Require replacement

Surface cracking (weather-checked) | No service suggested or required
````

## Chunk 8693: Trailing Arms

- Title: Trailing Arms
- Source path: `pages\11198.html`
- Chunk ID: `chunk_9cf13e5174f3`
- Images: none
- Duplicate sources: `pages\19971.html`

### Full Text

````text
# Trailing Arms

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware corroded, affecting structural integrity | A | Require replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Ball joint hole oversized (loose interference or press fit) | B | Further inspection required

NOTE: If oversized ball joint is available, require replacement of ball joint. If oversized ball joint is not available, require replacement of control arm.

Bent, affecting performance | B | Require replacement

Bushing hole oversized | B | Require replacement

Corroded, affecting structural integrity | A | Require replacement

Holes distorted | A | Require replacement

Threads damaged | A | Require repair or replacement

Threads stripped (threads missing) | A | Require replacement
````

## Chunk 8694: Vehicle Speed Sensor

- Title: Vehicle Speed Sensor
- Source path: `pages\11201.html`
- Chunk ID: `chunk_d10a4c82bcba`
- Images: none
- Duplicate sources: `pages\19974.html`

### Full Text

````text
# Vehicle Speed Sensor

Condition | Code | Procedure

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware corroded, affecting structural integrity | A | Require replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted | A | Require replacement

Connector missing | C | Require replacement

NOTE: Determine cause and correct prior to replacement of part.

Dust boot missing | C | Require replacement of boot

Dust boot split | A | Require replacement of boot

NOTE: If boot is not available separately, suggest replacement of sensor (reason code 2). This condition can lead to damage of the sliding magnet, which, in turn, causes premature sensor failure

Dust boot torn | A | Require replacement of boot

NOTE: If boot is not available separately, suggest replacement of sensor (reason code 2). This condition can lead to damage of the sliding magnet, which, in turn, causes premature sensor failure.

Housing cracked | B | Require replacement

NOTE: If boot is not available separately, suggest replacement of sensor (reason code 2). This condition can lead to damage of the sliding magnet, which, in turn, causes premature sensor failure.

Lead routing incorrect | B | Require rerouting according to vehicle manufacturer's specifications

Loose | B | Require adjustment to vehicle manufacturer's specifications

Missing | C | Require replacement

Output signal incorrect | B | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Wire lead burned | A | Require repair or replacement

Wire lead conductors exposed | B | Require repair or replacement

Wire lead open | A | Require repair or replacement

Wire lead shorted | A | Require repair or replacement
````

## Chunk 8695: Warning Lamps

- Title: Warning Lamps
- Source path: `pages\11204.html`
- Chunk ID: `chunk_f04fcb90d851`
- Images: none
- Duplicate sources: `pages\19977.html`

### Full Text

````text
# Warning Lamps

Condition | Code | Procedure

Bulb burned out | A | Require replacement

Warning light does not come on during bulb check | Further inspection required to determine cause

Warning light flashes | Further inspection required to determine cause

Warning light is intermittent | Further inspection required to determine cause

Warning light stays on after initial bulb check | Further inspection required to determine cause
````

## Chunk 8696: Wiring Harnesses And Connectors

- Title: Wiring Harnesses And Connectors
- Source path: `pages\11209.html`
- Chunk ID: `chunk_6e763fd7cc5c`
- Images: none
- Duplicate sources: `pages\19982.html`

### Full Text

````text
# Wiring Harnesses And Connectors

Condition | Code | Procedure

Application incorrect | B | Require repair or replacement

Attaching hardware broken | A | Require repair or replacement of hardware

Attaching hardware missing | C | Require replacement of hardware

Attaching hardware not functioning | A | Require repair or replacement of hardware

Attaching hardware threads damaged | A | Require repair or replacement of hardware

Attaching hardware threads stripped (threads missing) | A | Require replacement of hardware

Connector (Weatherpack type) leaking | A | Require repair or replacement

Connector broken | A | Require repair or replacement

Connector melted | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Connector missing | C | Require replacement

Insulation damaged, conductors exposed | A | Require repair or replacement

Insulation damaged, conductors not exposed | 1 | Suggest repair or replacement

Open | A | Require repair or replacement

Protective shield (conduit) melted | 2 | Suggest repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Protective shield (conduit) missing | C | Require repair or replacement

Resistance (voltage drop) out of specification | A | Require repair or replacement

Routed incorrectly | B | Require repair

Secured incorrectly | B | Require repair

Shorted | A | Require repair or replacement

Terminal broken | A | Require repair or replacement

Terminal burned, affecting performance | A | Require repair or replacement

NOTE: Determine cause and correct prior to repair or replacement of part.

Terminal burned, not affecting performance | 2 | Suggest repair or replacement

Terminal corroded, affecting performance | A | Require repair or replacement

Terminal corroded, not affecting performance | 2 | Suggest repair or replacement

Terminal loose, affecting performance | B | Require repair or replacement

Terminal loose, not affecting performance | 1 | Suggest repair or replacement

Voltage drop out of specification | A | Require repair or replacement
````

## Chunk 8697: Automotive Terminology & Definitions

- Title: Automotive Terminology & Definitions
- Source path: `pages\11211.html`
- Chunk ID: `chunk_7a15bec2b45a`
- Images: none
- Duplicate sources: `pages\19984.html`

### Full Text

````text
# Automotive Terminology & Definitions

active suspension systems move each wheel up and down to control body motion in response to road abnormalities. The system responds to inputs from the road and the driver. With an active suspension, a vehicle can simultaneously provide the smooth ride of a soft suspension along with the superior handling associated with a firm suspension.

active tilt control winds up the stabilizer bars in the front and rear suspension to resist body lean while cornering. Because active control is used only as needed, vehicle spring rates and stabilizer bar stiffness can be reduced, improving normal ride characteristics. In addition, this system has potential to increase low-speed, off-road traction on 4WD vehicles.

electronically provides variable steering ratios. A computer is linked with the vehicle stability control system to aid in directional stability of the vehicle. As the vehicle travels down the highway, road surfaces and wind gusts can affect the vehicle directional stability. The car may wander a little or dart to one side, as many who have met a tractor-trailer unit on a windy day have experienced. Sensors on the car detect this sudden unintentional movement and the computer will stabilize the car by moving the Active Steering electric motor and steering gear. The driver doesn't turn the steering wheel at all.

a suspension device made up of a flexible bladder containing compressed air. The air spring takes the place of a :onvent;onal coil or leaf spring. Air is supplied by an on-board ;ompressor, usually with auxiliary equipment to sense vehicle leight and modify the pressure in the air spring as needed.

instead of steel coil or leaf springs, some vehicles have a bellows-like unit at each corner that contains pressurized air. As a rule, air suspensions can produce a softer ride.

an adjustment to bring parts or components into a line or proper coordination.

the method of providing traction to any of the wheels of a vehicle, as conditions require. Depending on the system, it may be full-time or part-time.

see 'stabilizer bar'.

the relationship between the height of a tire from bead to tread, and the tread width, usually expressed as a percentage of the tread width.

automatic ride control adjusts vehicle shock absorber resistance (damping) in response to driver inputs such as steering and braking and for changes in road surface. During maneuvers such as hard braking or quick lane changes, the system increases suspension damping to improve dynamic stability. Damping is automatically decreased during steady driving, so that bumps and potholes are absorbed rather than being transmitted to the occupants. Some systems also allow the driver to select suspension settings: soft, normal or firm (sport).

a type of load placed on a bearing that is parallel to the axis of the rotating shaft.

movement of a component parallel to the axis of rotation.

round, on or along an axis; having the same direction or being parallel to the axis of rotation.

a real or imaginary straight line on which or around which an object rotates.

a condition of equal weight distribution within a component or among components; the act of equalizing the weight distribution, such as balancing a tire or an engine's reciprocating assembly.

a suspension component that provides a pivot point, allowing the steering knuckle to move up and down as well as turn. In response to steering input. The ball fits into a socket housing that is attached to the control arm and the stud on the other end of the ball is attached to the steering knuckle. A dust cover is installed over the ball and socket assembly to keep dirt out and lubricant in.

the steel reinforced inner edge of a tire, which fits inside and seals against the wheel rim.

protective rubber cover with accordion pleats used to contain lubricants and exclude contaminating dirt, water and grime, located at each end of the rack-and- pinion assembly and FWD CV-joints.

a steering problem in which a vehicle tends to the left or the right after a bump, without steering wheel input from the driver. This is usually caused by some steering misalignment or damage that permits change of toe when the suspension works up and down.

a liner, usually removable, for a bearing; an anti-friction liner used in place of a bearing; a type of bearing that is used to support rotating shafts.
````

## Chunk 8698: Automotive Terminology & Definitions

- Title: Automotive Terminology & Definitions
- Source path: `pages\11211.html`
- Chunk ID: `chunk_4cbae57070e5`
- Images: none
- Duplicate sources: `pages\19984.html`

### Full Text

````text
. A dust cover is installed over the ball and socket assembly to keep dirt out and lubricant in.

the steel reinforced inner edge of a tire, which fits inside and seals against the wheel rim.

protective rubber cover with accordion pleats used to contain lubricants and exclude contaminating dirt, water and grime, located at each end of the rack-and- pinion assembly and FWD CV-joints.

a steering problem in which a vehicle tends to the left or the right after a bump, without steering wheel input from the driver. This is usually caused by some steering misalignment or damage that permits change of toe when the suspension works up and down.

a liner, usually removable, for a bearing; an anti-friction liner used in place of a bearing; a type of bearing that is used to support rotating shafts.

the attitude of a wheel/tire assembly in which, when viewed from the front, the distance between the tops and bottoms of the tires are different. If the distance between the tops is greater than between the bottoms, positive camber is present. If the distance between the tops is less than between the bottoms, negative camber is present.

angle formed between the kingpin axis and a vertical axis as viewed from the side of the vehicle. Caster is considered positive when the top of the kingpin axis is behind the vertical axis, that is, tilted toward the rear of the vehicle.

a steering linkage component which attaches the Pitman arm to the idler arm, tie-rod or crosslink.

spring steel rod wound into a coil that supports the vehicle's weight while allowing suspension movement.

a steering column that is designed to collapse, to prevent the column from heavily impacting the driver during an accident.

a flexible coupling between two shafts that allows each shaft to maintain the same speed regardless of operating angle.

a suspension component that connects the vehicle frame to the steering knuckle or axle housing and allows the up and down movement of the wheels.

a safety component made from soft steel, used to keep a nut from loosening on a bolt or stud. The cotter pin is inserted through a hole in the bolt or stud and through slots in the nut (see 'castellated nut'), then the ends of the cotter pin are spread to lock it in position.

part of the vehicle frame structure, arranged transversely and attached to the frame rails at each side of the vehicle. Can be removable or welded in place.

to slow or reduce oscillations or movement.

a load-supporting axle that does not transmit power; an axle that does not rotate, but merely forms a base on which to attach the wheels.

the ability of a car to travel in a straight line on a flat surface with a minimum of driver control.

tire with a tread pattern that is designed to give maximum traction by removing water from under the tread in such a way as to minimize the risk of aquaplaning. Directional tires must be installed to turn in a specific direction.

negative aerodynamic lift.

drag divided by the product of dynamic pressure and projected area. A factor representing the drag acting on a body (as an automobile or airfoil).

a steering linkage component that connects the pitman arm and the steering arm.

horizontal aerodynamic retarding force on a vehicle parallel to the relative wind direction.

balancing a part while it is in motion.

electrically powered steering uses an electric motor to drive either the power steering hydraulic pump or the steering linkage directly. The power steering function is therefore independent of engine speed, resulting in significant energy savings.

electronic air suspension provides the comfort of riding on air with adjustable spring rates and capability to change ride height and load-carrying ability. Under normal driving conditions, an electronic air suspension vehicle rides at the same height as a traditionally sprung vehicle. With a heavy load, ride height is increased automatically. On current vehicles, the suspension lowers the ride height by 20 mm at highway speeds for improved aerodynamics, with about 2 percent better fuel economy. Lower ride height also can improve on-center feel of steering due to the change in suspension geometry and increased caster angle.

a suspension system that uses air springs to maintain vehicle ride height. Height sensors are used to signal a control unit when the vehicle is riding low or high. In response to this signal, compressed air is either sent to or vented from the air springs.
````

## Chunk 8699: Automotive Terminology & Definitions

- Title: Automotive Terminology & Definitions
- Source path: `pages\11211.html`
- Chunk ID: `chunk_48f11b4bd576`
- Images: none
- Duplicate sources: `pages\19984.html`

### Full Text

````text
es and capability to change ride height and load-carrying ability. Under normal driving conditions, an electronic air suspension vehicle rides at the same height as a traditionally sprung vehicle. With a heavy load, ride height is increased automatically. On current vehicles, the suspension lowers the ride height by 20 mm at highway speeds for improved aerodynamics, with about 2 percent better fuel economy. Lower ride height also can improve on-center feel of steering due to the change in suspension geometry and increased caster angle.

a suspension system that uses air springs to maintain vehicle ride height. Height sensors are used to signal a control unit when the vehicle is riding low or high. In response to this signal, compressed air is either sent to or vented from the air springs.

transfers power from the transaxle to the front wheels on a front-wheel drive vehicle. Also used on some vehicles with rear-wheel drive and independent rear suspension to transfer power from the differential to the rear wheels. Consists of a stub shaft that is splined into the differential side gear, another stub shaft that is splined into the wheel hub, an interconnecting shaft, and two CV-joints, which connect the interconnecting shaft to the stub shafts.

periodic motion or vibration along a straight line. The severity depends on the frequency or amplitude.

a component used in an air suspension system to signal a control unit when the vehicle is riding low or high. In response to this signal, compressed air is either sent to or vented from the air springs.

mounting point for the wheelan an axle or spindle; the part of the synchronizer assembly that is splined to the transmission shaft; the center part of a wheel, gear, etc., that rides on a shaft.

a conventional steering system component consisting of an arm that swivels in a bushing on a shaft, which is attached to the frame. The idler arm is mounted on the right side of the vehicle and is the same length and set at the same angle as the Pitman arm. Its function is to hold the right end of the center link level with the left end, which is moved by the pitman arm, and transfer the steering motion to the right side tie-rod.

the sum of the angle of camber and steering axis inclination; the sum of two intersecting angles.

a suspension in which each wheel can travel up and down without directly affecting the position of the opposite wheel.

a power steering system in which the power cylinder and control valve are contained in one housing.

the Intelligent Vehicle Highway System (IVHS) provides a variety of information to the vehicle and driver through cooperation of automotive electronics, communications, controls and systems engineering technologies. IVHS has two areas of interest to car and truck makers: (1)telematics and (2)active safety warning and control systems. Several features are: Telematics: Navigation systems Traffic messaging Emergency messaging and security tracking (e.g. RESCU - Remote Emergency Satellite Cellular Unit) Short range communications/ automatic toll collection Active Safety Warning and Control Systems Collision warning/avoidance - Backup and parking aids - Side vision aid - Vision enhancement - (all weather/night vision) - Adaptive cruise control - Lane departure control

interactive Vehicle Dynamics is designed to minimize loss of vehicle control due to loss of traction. The IVD system could be activated when a vehicle is taking a turn too quickly or when encountering an icy patch.

a locknut.

the pivot shaft for the steering knuckle on most early axles and some modern heavy-duty axles.

the suspension component that connects the upper and lower control arms or the strut and lower control arm. On rear wheel drive vehicles, it usually incorporates the front wheel spindle and on front wheel drive vehicles it has an opening where the halfshaft passes through. A steering arm is attached to the knuckle, where the tie-rod end is connected. Also called a steering knuckle.

Issues a warning when the vehicle edges off course and reaches the highway lane markers. Introduced on the 2005 Infiniti FX and available on the 2006 Infiniti M45, the system developed by Iteris can detect lane dividers even in rainy weather. It delivers a noticeable sound when the vehicle starts to move into an adjacent lane, whether due to inattention, drowsiness or distraction.

side-to-side movement or wobble in a wheel or tire.
````

## Chunk 8700: Automotive Terminology & Definitions

- Title: Automotive Terminology & Definitions
- Source path: `pages\11211.html`
- Chunk ID: `chunk_2009735f7d5d`
- Images: none
- Duplicate sources: `pages\19984.html`

### Full Text

````text
t that connects the upper and lower control arms or the strut and lower control arm. On rear wheel drive vehicles, it usually incorporates the front wheel spindle and on front wheel drive vehicles it has an opening where the halfshaft passes through. A steering arm is attached to the knuckle, where the tie-rod end is connected. Also called a steering knuckle.

Issues a warning when the vehicle edges off course and reaches the highway lane markers. Introduced on the 2005 Infiniti FX and available on the 2006 Infiniti M45, the system developed by Iteris can detect lane dividers even in rainy weather. It delivers a noticeable sound when the vehicle starts to move into an adjacent lane, whether due to inattention, drowsiness or distraction.

side-to-side movement or wobble in a wheel or tire.

a suspension spring consisting of a single flat plate made of steel or composite material or several steel plates bundled together.

a low tire pressure warning system alerts the driver if the air pressure in a tire becomes too low. Typically, a light on the instrument panel will be illuminated to warn of the low-pressure condition.

the principal device in the suspension of the same name, in which the spring, shock absorber and sometimes the steering knuckle are combined in a single unit.

a steering condition where the steering wheel and wheels want to return to a position other than center. This can be caused by tightening rubber bonded socket tie-rod ends when the steering wheel is not centered, binding in the upper strut mounts, or binding in a steering component or ball joint.

the practice of spinning a wheel on the car to balance the wheel and all other rotational components together.

a type of conventional steering linkage consisting of a pitman arm, center link, idler arm and tierod assemblies to connect to the steering knuckles. The pitman arm, center link and idler arm form three sides of a parallelogram.

a steering system component mounted on the steering box shaft and transfers the gearbox motion to the steering linkage.

the inboard CV-joint on a halfshaft, so called because the joint moves in and out in response to the suspension's up and down movement, which causes the distance between the transaxle and the wheel to change. The movement takes place within the joint, with the tripod rollers or double offset ball bearings moving in and out on elongated grooves in the yoke or outer race.

when a part is slightly larger than a hole it must be forced together with a press.

a steering condition where the vehicle driver has to maintain constant pressure on the steering wheel to keep the vehicle moving straight.

a type of steering mechanism that replaces the pitman arm, center link and idler arm on gearbox steering. The steering column ends in a pinion gear that moves the driven rack to the left and right. The rack ends contain ball studs connected to the outer tie-rod ends and steering knuckles.

load applied at 90 degrees to an axis of rotation.

the out-of-roundness ot a wheel or tire.

branching out in all directions from a common center; perpendicular to the shaft or bearing bore.

a suspension component that is connected to a twin I-beam or solid axle at one end and to the vehicle frame through bushings at the other. The radius arm braces the I-beam or axle and keeps it at a right angle to the vehicle frame.

a system used on a some vehicles to change the toe of the rear wheels to either steepen a sharp turn or enhance cornering on a shallower, faster one.

the dimension between a fixed point on the vehicle and the pavement. The fixed point varies according to vehicle and manufacturer. Also called vehicle height.

retarding force, parallel to the direction of travel, caused by tire resistance along the ground.

wobble or deflection beyond a rotating part's normal plane of movement.

see 'steering axis inclination',

the distance between the point at which the tire's vertical centerpoint intersects the road, and the steering axis inclination (SAI) intersects the road.

the attachment to the frame for one end of a leaf spring. The shackle allows the spring to change in length as the vehicle encounters uneven road surfaces.

thin sheets of material, usually metal, used as spacers to control the distance between parts.

a device used to dampen the oscillation of the suspension caused by irregularities in the road surface.
````

## Chunk 8701: Automotive Terminology & Definitions

- Title: Automotive Terminology & Definitions
- Source path: `pages\11211.html`
- Chunk ID: `chunk_9a17534413ad`
- Images: none
- Duplicate sources: `pages\19984.html`

### Full Text

````text
point varies according to vehicle and manufacturer. Also called vehicle height.

retarding force, parallel to the direction of travel, caused by tire resistance along the ground.

wobble or deflection beyond a rotating part's normal plane of movement.

see 'steering axis inclination',

the distance between the point at which the tire's vertical centerpoint intersects the road, and the steering axis inclination (SAI) intersects the road.

the attachment to the frame for one end of a leaf spring. The shackle allows the spring to change in length as the vehicle encounters uneven road surfaces.

thin sheets of material, usually metal, used as spacers to control the distance between parts.

a device used to dampen the oscillation of the suspension caused by irregularities in the road surface.

a suspension system in which the upper control arm is shorter than the lower control arm, allowing the wheel to deflect in a vertical direction with minimal change in camber.

a shaft used to attach the wheel assembly on non-drive axles.

a suspension system component that supports the vehicle and absorbs shock caused by uneven road surfaces; a device that returns to its original form after being forced out of shape.

a toothed wheel used to engage a chain or ribbed belt.

the weight of all the vehicle components that are supported by the springs; see 'unsprung weight'.

a torsion-bar spring connecting the suspension on either side of the vehicle. When a vehicle rolls to the side in a turn, the suspension at the outside wheel compresses and the suspension at the inside wheel extends. The stabilizer bar that connects them twists to apply a counteracting force to hold the vehicle closer to level. Also called an anti-roll bar or sway bar.

balance at rest; still balance; the equal distribution of weight of the wheel and tire around the axis of rotation such that the wheel assembly has no tendency to rotate by itself regardless of its position.

the steering system component that links the steering knuckle to the tie-rod assembly.

the angle between true vertical and an imaginary line running through the rotational center of the ball joint(s).

the housing, steering shaft, bearings and related components between the steering wheel and the steering gear.

the assembly located at the end of the steering column, which contains the gears and other components that multiply the driver turning force.

the suspension component that connects the upper and lower control arms or the strut and lower control arm. On rear wheel drive vehicles, it usually incorporates the front wheel spindle and on front wheel drive vehicles it has an opening where the halfshaft passes through. A steering arm is attached to the steering knuckle, where the tie-rod end is connected.

all of the components that connect the steering gear to the front wheels.

on vehicles where the lower control arm is attached to the frame at one pivot point, a strut rod is used to brace the control arm against the vehicle frame.

a fastener that has screw threads at both ends.

see 'stabilizer bar',

the difference between the thrust line and the geometric centerline of the vehicle.

aligning the front wheels to the thrust line during a wheel alignment, when rear wheel toe cannot be adjusted to specification.

an imaginary line that divides the total toe angle of the rear wheels.

load placed on a part that is parallel to the center of the axis.

a ball and socket joint that connects the tie-rod to the steering knuckle arm and to the center link or steering rack.

steering linkage member which connects the steering knuckle arm with the centerlink or the steering rack.

the practice of moving a set of tires to different positions on the vehicle to equalize wear and extend the life of the tires.

see 'wheel slip'.

the direction in which a wheel tends to roll, a major factor in tire wear.

a condition that exists if the tire's line of forward direction intersects the extended centerline of the vehicle.

the designed angle of the steering arm on the steering knuckle, which causes the inside front wheel to turn at a sharper angle than the outside front wheel during a turn. The specification is checked using the turntables on wheel alignment machine. Toe-out on turns is not an adjustable angle, and if it is incorrect it is most likely due to a bent steering arm.

a condition that exists if the tire's line of forward direction and the vehicle centerline are angled apart.
````

## Chunk 8702: Automotive Terminology & Definitions

- Title: Automotive Terminology & Definitions
- Source path: `pages\11211.html`
- Chunk ID: `chunk_f6370cdc254e`
- Images: none
- Duplicate sources: `pages\19984.html`

### Full Text

````text
of moving a set of tires to different positions on the vehicle to equalize wear and extend the life of the tires.

see 'wheel slip'.

the direction in which a wheel tends to roll, a major factor in tire wear.

a condition that exists if the tire's line of forward direction intersects the extended centerline of the vehicle.

the designed angle of the steering arm on the steering knuckle, which causes the inside front wheel to turn at a sharper angle than the outside front wheel during a turn. The specification is checked using the turntables on wheel alignment machine. Toe-out on turns is not an adjustable angle, and if it is incorrect it is most likely due to a bent steering arm.

a condition that exists if the tire's line of forward direction and the vehicle centerline are angled apart.

the distance between the centers of the treads of parallel wheels.

travel of the rear wheels in a parallel path with the front wheels.

a type of independent front suspension and used on light trucks and vans. It consists of two I-beams supported by coil springs, and the steering knuckles/spindles, which are connected by king pins or ball joints. The inner end of the axle connects to the vehicle frame through a rubber bushing. A radius arm also connects to the frame through rubber bushings to control wheelbase and caster.

the components of a vehicle that rest directly on the road surface without being supported by the suspension springs.

a power steering system that uses valves and speed sensors to vary the amount of steering assist according to engine or road speed. At slow speeds more steering assist is delivered and steering the wheels is easier; necessary for parking, etc.. At higher speeds, steering assist is reduced and more steering effort is required to steer the car, giving the driver greater feel of the road. Also known as Speed-sensitive power steering.

see 'ride height'.

the adjustment of suspension and steering components to optimize steering control and minimize tire wear.

the condition in which a wheel/tire assembly has equal weight around its center, preventing vibration at high speeds. Wheel balance can be static, such as on a bubble balancer, or dynamic, such as with a spin balancer.

the dimensional difference between a wheel's centerline and the plane of the axle flange mounting surface.

a measurement (in percentage) of the friction between the tire and road surface; at zero slip the tire rotates freely, while at 100% slip the tire is locked up and is pushed along the road surface by the moving vehicle. Also called tire slip.

a permanent magnetic sensor that sends information to the computer in an ABS system regarding wheel speed.

small weights, usually made of lead, attached either mechanically or by adhesive to a wheel/tire assembly to correct its balance.

a gear into which teeth are cut, resembling the threads of a screw.
````

## Chunk 8703: Pre-Alignment Instructions: Notes

- Title: Pre-Alignment Instructions: Notes
- Source path: `pages\11213.html`
- Chunk ID: `chunk_789c77d1223f`
- Images: none
- Duplicate sources: `pages\19860.html`

### Full Text

````text
# Pre-Alignment Instructions: Notes
````

## Chunk 8704: General Alignment Checks

- Title: General Alignment Checks
- Source path: `pages\11214.html`
- Chunk ID: `chunk_b267d2213435`
- Images: `images\G26694.gif`, `images\G26695.gif`
- Duplicate sources: `pages\19861.html`

### Full Text

````text
# General Alignment Checks

Before adjusting wheel alignment, check the following:

- Each axle uses tires of same construction and tread style, equal in tread wear and overall diameter. Verify that radial and axial runout is not excessive. Inflation should be at manufacturer's specifications.

- Steering linkage and suspension must not have excessive play. Check for wear in tie rod ends and ball joints. Springs must not be sagging. Control arm and strut rod bushings must not have excessive play. See Fig 1 . Fig 1: Checking Steering Linkage

- Vehicle must be on level floor with full fuel tank, no passenger load, spare tire in place and no load in trunk. Bounce front and rear end of vehicle several times. Confirm vehicle is at normal riding height.

- Steering wheel must be centered with wheels in straight ahead position. If required, shorten one tie rod adjusting sleeve and lengthen opposite sleeve (equal amount of turns). See Fig 2 .

- Wheel bearings should have the correct preload and lug nuts must be tightened to manufacturer's specifications. Adjust camber, caster and toe-in using this sequence. Follow instructions of the alignment equipment manufacturer.
````

## Chunk 8705: Wheel Alignment Theory & Operation - General Information: Adjustments: Notes

- Title: Wheel Alignment Theory & Operation - General Information: Adjustments: Notes
- Source path: `pages\11215.html`
- Chunk ID: `chunk_231a5201cb26`
- Images: none
- Duplicate sources: `pages\19862.html`

### Full Text

````text
# Wheel Alignment Theory & Operation - General Information: Adjustments: Notes
````

## Chunk 8706: Wheel Alignment Theory & Operation - General Information: Adjustments: Camber

- Title: Wheel Alignment Theory & Operation - General Information: Adjustments: Camber
- Source path: `pages\11216.html`
- Chunk ID: `chunk_2d32c46f25f4`
- Images: `images\G26696.gif`
- Duplicate sources: `pages\19863.html`

### Full Text

````text
# Wheel Alignment Theory & Operation - General Information: Adjustments: Camber

- Camber is the tilting of the wheel, outward at either top or bottom, as viewed from front of vehicle. See Fig 1 .

- When wheels tilts outward at the top (from centerline of vehicle), camber is positive. When wheels tilt inward at top, camber is negative. Amount of tilt is measured in degrees from vertical.
````

## Chunk 8707: Wheel Alignment Theory & Operation - General Information: Adjustments: Caster

- Title: Wheel Alignment Theory & Operation - General Information: Adjustments: Caster
- Source path: `pages\11217.html`
- Chunk ID: `chunk_1a19bd75587d`
- Images: `images\G26697.gif`
- Duplicate sources: `pages\19864.html`

### Full Text

````text
# Wheel Alignment Theory & Operation - General Information: Adjustments: Caster

- Caster is tilting of front steering axis either forward or backward from vertical, as viewed from side of vehicle. See Fig 1 .

- When axis is tilted backward from vertical, caster is positive. This creates a trailing action on front wheels. When axis is tilted forward, caster is negative, causing a leading action on front wheels.
````

## Chunk 8708: Toe-In Adjustment

- Title: Toe-In Adjustment
- Source path: `pages\11218.html`
- Chunk ID: `chunk_abcdc55ecfb2`
- Images: `images\G26698.gif`
- Duplicate sources: `pages\19865.html`

### Full Text

````text
# Toe-In Adjustment

Toe-in is the width measured at the rear of the tires subtracted by the width measured at the front of the tires at about spindle height. A positive figure would indicate toe-in and a negative figure would indicate toe-out. If the distance between the front and rear of the tires is the same, toe measurement would be zero. To adjust:

1) Measure toe-in with front wheels in straight ahead position and steering wheel centered. To adjust toe-in, loosen clamps and turn adjusting sleeve or adjustable end on right and left tie rods. See Figure and Fig 1 .

2) Turn equally and in opposite directions to maintain steering wheel in centered position. Face of tie rod end must be parallel with machined surface of steering rod end to prevent binding.

3) When tightening clamps, make certain that clamp bolts are positioned so there will be no interference with other parts throughout the entire travel of linkage.
````

## Chunk 8709: Toe-Out On Turns

- Title: Toe-Out On Turns
- Source path: `pages\11219.html`
- Chunk ID: `chunk_01951284ec98`
- Images: none
- Duplicate sources: `pages\19866.html`

### Full Text

````text
# Toe-Out On Turns

- Toe-out on turns (turning radius) is a check for bent or damaged parts, and not a service adjustment. With caster, camber, and toe-in properly adjusted, check toe-out with weight of vehicle on wheels.

- Use a full floating turntable under each wheel, repeating test with each wheel positioned for right and left turns. Incorrect toe-out generally indicates a bent steering arm. Replace arm, if necessary, and recheck wheel alignment.
````

## Chunk 8710: Steering Axis Inclination

- Title: Steering Axis Inclination
- Source path: `pages\11220.html`
- Chunk ID: `chunk_b19c32a78013`
- Images: `images\G90J06025.gif`
- Duplicate sources: `pages\19867.html`

### Full Text

````text
# Steering Axis Inclination

- Steering axis inclination is a check for bent or damaged parts, and not a service adjustment. Vehicle must be level and camber should be properly adjusted. See Fig 1 .

- If camber cannot be brought within limits and steering axis inclination is correct, steering knuckle is bent. If camber and steering axis inclination are both incorrect by approximately the same amount, the upper and lower control arms are bent.
````

## Chunk 8711: Traction Control Disable

- Title: Traction Control Disable
- Source path: `pages\11290.html`
- Chunk ID: `chunk_6fe6c6c62f98`
- Images: none
- Duplicate sources: `pages\19858.html`

### Full Text

````text
# Traction Control Disable

Application | FWD | RWD | Part Time 4WD | Full Time 4WD | AWD | TCS | Do Not Test

Accord

2001-07 | X | ... | ... | ... | ... | X (1) | ...

2008-25 | X | ... | ... | ... | ... | X (2) | ...

Accord Crosstour

2010-11 (FWD) | X | ... | ... | ... | ... | X (2) | ...

2010-11 (4WD) | X | ... | ... | X (4) | ... | ... | X

Civic

2007 | X | ... | ... | ... | ... | X (1) | ...

2008-25 | X | ... | ... | ... | ... | X (2) | ...

Civic Wagon

1987-91 | ... | ... | X (3) | ... | ... | ... | ...

Clarity

2017-21 | X | ... | ... | ... | ... | X (2) | ...

CR-V

2005-06 (FWD) | X | ... | ... | ... | ... | X (1) | ...

1997-25 (AWD) | ... | ... | ... | ... | X | ... | X

2007-25 (FWD) | X | ... | ... | ... | ... | X (2) | ...

CR-Z

2012-16 | X | ... | ... | ... | ... | X (2) | ...

Crosstour

2012-15 (FWD) | X | ... | ... | ... | ... | X (2) | ...

2012-15 (4WD) | ... | ... | ... | X (4) | ... | ... | X

Element

2003-11 (AWD) | ... | ... | ... | ... | X | ... | X

2007-08 (FWD) | X | ... | ... | ... | ... | X (1) | ...

2009-10 (FWD) | X | ... | ... | ... | ... | X (2) | ...

Fit

2007-20 | X | ... | ... | ... | ... | X (2) | ...

HR-V

2016-25 (FWD) | X | ... | ... | ... | ... | X (2) | ...

2016-25 (AWD) | ... | ... | ... | ... | X | ... | X

Insight

2010-14 | X | ... | ... | ... | ... | X (2) | ...

Odyssey

1999-09 | X | ... | ... | ... | ... | X (1) | ...

2010-25 | X | ... | ... | ... | ... | X (2) | ...

Passport

1994-97 (4WD) | ... | ... | X (5) | ... | ... | ... | ...

1998-02 (4WD) | ... | ... | X (6) | ... | ... | ... | ...

2019-25 (4WD) | ... | ... | X | ... | ... | X (2) | ...

Pilot

2005-08 (FWD) | X | ... | ... | ... | ... | X (1) | ...

2009-25 (FWD) | X | ... | ... | ... | ... | X (2) | ...

2005-25 (AWD) | ... | ... | ... | ... | X | ... | X

Prologue

2024-25 (FWD) | ... | ... | ... | ... | X | X (7) | ...

2024-25 (AWD) | X | ... | ... | ... | ... | X (7) | ...

Ridgeline

2006-13 | ... | ... | ... | X (4) | ... | X (2) | X

2014-25 (AWD) | ... | ... | ... | ... | X | ... | X

2014-25 (FWD) | X | ... | ... | ... | ... | X (2) | ...

(1) Press TCS (or VSA) switch near left side vent. TCS indicator light will illuminate when system is disabled. (2) Press VSA switch to the left of the steering wheel until a beep is heard. VSA indicator light will illuminate when system is disabled. (3) On A/T models, locate disengagement plate on rear of transaxle case behind the right front wheel. Loosen lock bolt on plate. Turn middle bolt on plate. Turn middle bolt counterclockwise until plate rotates about 150 degrees and is stopped by lock bolt. Tighten lock bolt. On M/T models, locate Orange disengagement lever at rear of engine. Loosen lock bolt at slotted lever. Turn middle bolt on lever counterclockwise and tighten lock bolt. (4) Cannot be shifted to 2WD. (5) Shift transfer case lever into 2WD position. Ensure 4WD indicator light is off. (6) Shift transfer case lever into HIGH position. The 4WD button is located on left side of dash. Ensure 4WD indicator light is off. (7) Roll the right selector wheel to scroll to select Reduce traction control , then press the right selector wheel to check or uncheck it. | (1) | Press TCS (or VSA) switch near left side vent. TCS indicator light will illuminate when system is disabled. | (2) | Press VSA switch to the left of the steering wheel until a beep is heard. VSA indicator light will illuminate when system is disabled. | (3) | On A/T models, locate disengagement plate on rear of transaxle case behind the right front wheel. Loosen lock bolt on plate. Turn middle bolt on plate. Turn middle bolt counterclockwise until plate rotates about 150 degrees and is stopped by lock bolt. Tighten lock bolt. On M/T models, locate Orange disengagement lever at rear of engine. Loosen lock bolt at slotted lever. Turn middle bolt on lever counterclockwise and tighten lock bolt. | (4) | Cannot be shifted to 2WD. | (5) | Shift transfer case lever into 2WD position. Ensure 4WD indicator light is off. | (6) | Shift transfer case lever into HIGH position. The 4WD button is located on left side of dash. Ensure 4WD indicator light is off. | (7) | Roll the right selector wheel to scroll to select Reduce traction control , then press the right selector wheel to check or uncheck it.

(1) | Press TCS (or VSA) switch near left side vent. TCS indicator light will illuminate when system is disabled.
````

## Chunk 8712: Traction Control Disable

- Title: Traction Control Disable
- Source path: `pages\11290.html`
- Chunk ID: `chunk_1eb3c4b4eea9`
- Images: none
- Duplicate sources: `pages\19858.html`

### Full Text

````text
ddle bolt counterclockwise until plate rotates about 150 degrees and is stopped by lock bolt. Tighten lock bolt. On M/T models, locate Orange disengagement lever at rear of engine. Loosen lock bolt at slotted lever. Turn middle bolt on lever counterclockwise and tighten lock bolt. | (4) | Cannot be shifted to 2WD. | (5) | Shift transfer case lever into 2WD position. Ensure 4WD indicator light is off. | (6) | Shift transfer case lever into HIGH position. The 4WD button is located on left side of dash. Ensure 4WD indicator light is off. | (7) | Roll the right selector wheel to scroll to select Reduce traction control , then press the right selector wheel to check or uncheck it.

(1) | Press TCS (or VSA) switch near left side vent. TCS indicator light will illuminate when system is disabled.

(2) | Press VSA switch to the left of the steering wheel until a beep is heard. VSA indicator light will illuminate when system is disabled.

(3) | On A/T models, locate disengagement plate on rear of transaxle case behind the right front wheel. Loosen lock bolt on plate. Turn middle bolt on plate. Turn middle bolt counterclockwise until plate rotates about 150 degrees and is stopped by lock bolt. Tighten lock bolt. On M/T models, locate Orange disengagement lever at rear of engine. Loosen lock bolt at slotted lever. Turn middle bolt on lever counterclockwise and tighten lock bolt.

(4) | Cannot be shifted to 2WD.

(5) | Shift transfer case lever into 2WD position. Ensure 4WD indicator light is off.

(6) | Shift transfer case lever into HIGH position. The 4WD button is located on left side of dash. Ensure 4WD indicator light is off.

(7) | Roll the right selector wheel to scroll to select Reduce traction control , then press the right selector wheel to check or uncheck it.
````

## Chunk 8713: Trouble Shooting - Manual Transmission - General Information: Introduction

- Title: Trouble Shooting - Manual Transmission - General Information: Introduction
- Source path: `pages\11292.html`
- Chunk ID: `chunk_68673c3313be`
- Images: none
- Duplicate sources: `pages\19857.html`

### Full Text

````text
# Trouble Shooting - Manual Transmission - General Information: Introduction

There are many times when the transmission is incorrectly blamed for shifting problems or noises that are actually caused by other reasons. Shift difficulties are frequently caused by conditions outside of the transmission or transaxle. Typical conditions include: shift linkage, shift cables, alignment of engine to transmission, worn engine mounts or clutch problems. Drive train noises may come from many sources such as tires, road surfaces, wheel bearings, differentials, engine or exhaust system. Repairing or overhauling transmission will not cure these problems.

No manufacturer makes a perfectly quiet transmission. Gear rollover noise is present in most constant mesh transmissions and will tend to disappear when the clutch is disengaged or transmission is placed in gear. If clutch is properly adjusted, clutch release bearing noise will disappear when release bearing is moved enough to slide release bearing away from pressure plate.

Trouble shooting can be helped by driving vehicle on a smooth level road to help eliminate tire and body noise. Note whether noise occurs on acceleration, coasting, deceleration or steady driving conditions. Some problems may only occur when transmission is either hot or cold. Gear lubricant that is too thick can cause hard shifting on cold mornings before engine is warm and vehicle has been driven.

Condition | Possible Cause

Noisy In Forward Gears | Low Gear Oil Level, Loose Bellhousing Bolts, Worn Bearings Or Gears

Clunk On Deceleration (FWD Only) | Loose Engine Mounts, Worn Inboard CV Joints, Worn Differential Pinion Shaft, Oversized Side Gear Hub Counterbore in Case

Gear Clash When Shifting Forward Gears | Clutch Out Of Alignment, Shift Linkage Damaged Or Out Of Adjustment, Gears Or Synchronizers Damaged, Low Gear Oil Level

Transmission Noisy When Moving (RWD Only); Quiet In Neutral With Clutch Engaged | Worn Rear Output Shaft Bearing

Gear Rattle | Worn Bearings, Worn Gear Oil, Low Gear Oil, Worn Gears

Steady Ticking At Idle (Increases With RPM) | Broken Tooth On A Gear

Gear Clash When Shifting Forward Gears | Worn Or Broken Synchronizers, Faulty Clutch

Loud Whine In Reverse | Normal Condition (1)

Noise When Stepping On Clutch | Faulty Release Bearing, Worn Pilot Bearing

Ticking Or Screeching As Clutch Is Engaged | Faulty Release Bearing, Uneven Pressure Plate Fingers

Click Or Snap When Clutch Is Engaged | Worn Clutch Fork, Worn Pivot Ball, Worn Or Broken Front Bearing Retainer

Transmission Shifts Hard | Clutch Not Releasing, Incorrect Gear Oil, Shift Mechanism Binding, Clutch Installed Backward

Will Not Shift Into One Gear, Shifts Into All Others | Bent Shift Fork, Worn Detent Balls

Locked Into Gear, Cannot Shift | Clutch Adjustment, Worn Detent Balls

Transmission Jumps Out Of Gear | Pilot Bearing Worn, Bent Shift Fork, Worn Gear Teeth Or Face, Excessive Gear Train End Play, Worn Synchronizers, Missing Detent Ball Spring, Shift Mechanism Worn Or Out Of Adjustment, Engine Or Transmission Mount Bolts Loose, Transmission Not Aligned

Shift Lever Rattle | Worn Detents Or Shift Lever, Worn Shift Fork, Worn Synchronizer Sleeves

Shift Lever Hops Under Acceleration | Worn Engine Or Transmission Mounts

(1) Most units use spur cut gears in Reverse and are naturally noisy. | (1) | Most units use spur cut gears in Reverse and are naturally noisy.

(1) | Most units use spur cut gears in Reverse and are naturally noisy.
````

## Chunk 8714: Air Conditioning

- Title: Air Conditioning
- Source path: `pages\11303.html`
- Chunk ID: `chunk_682bb924a1d4`
- Images: none
- Duplicate sources: `pages\19845.html`

### Full Text

````text
# Air Conditioning

Item | Measurement | Qualification | Standard or New | Service Limit

Refrigerant | Type (KA/KC) | HFO-1234yf (R-1234yf)

Type (KX) | HFC-134a (R-134a)

Capacity of system (KA/KC) | 375-425 g (13.23-14.99 oz) | -

Capacity of system (KX) | 405-455 g (14.29-16.05 oz) | -

Refrigerant oil | Type (KA/KC) | RL85HM (POE oil: P/N 38899-RLV-A01)

Type (KX) | DENSO ND-OIL 8 (PAG oil: P/N 38897-PR7-A01AH)

Capacity of components | Condenser (including dryer desiccant) | 50 mL (1 2/3 fl oz)

Evaporator | 40 mL (1 1/3 fl oz)

Each line and hose | 10 mL (1/3 fl oz)

Dryer desiccant | 10 mL (1/3 fl oz)

Compressor | 77-103 mL (2 3/5-3 1/2 fl oz)

Compressor | Field coil resistance | At 68 deg.F (20 deg.C) | 3.35-3.61 '

Variable capacity control solenoid resistance | At 68 deg.F (20 deg.C) | 9.6-11.6 '

Pulley-to-armature plate clearance (1.5 L) | 0.35-0.65 mm (0.014-0.025 in) | -

Pulley-to-armature plate clearance (2.0 L) | 0.30-0.70 mm (0.012-0.027 in) | -
````

## Chunk 8715: Climate Control System DTC Troubleshooting Index

- Title: Climate Control System DTC Troubleshooting Index
- Source path: `pages\11304.html`
- Chunk ID: `chunk_4405e20efc2e`
- Images: none
- Duplicate sources: `pages\13066.html`

### Full Text

````text
# Climate Control System DTC Troubleshooting Index

DTC | Detection Item or Symptom | ECU | DTC Type

B120A | Climate control unit LIN communication bus line error | Climate control unit | Loss of communication

B121A | An open in the mode control motor circuit | Climate control unit | Signal error

B121B | A short in the mode control motor circuit | Climate control unit | Signal error

B1220 | A short in the recirculation control motor circuit | Climate control unit | Signal error

B1225 | An open in the in-car temperature sensor circuit | Climate control unit | Signal error

B1226 | A short in the in-car temperature sensor circuit | Climate control unit | Signal error

B1227 | An open in the outside air temperature sensor circuit | Climate control unit | Signal error

B1228 | A short in the outside air temperature sensor circuit | Climate control unit | Signal error

B1231*1 | An open in the evaporator temperature sensor circuit | Climate control unit | Signal error

B1232*1 | A short in the evaporator temperature sensor circuit | Climate control unit | Signal error

B1233 | An open in the air mix control motor circuit (driver's) | Climate control unit | Signal error

B1234 | A short in the air mix control motor circuit (driver's) | Climate control unit | Signal error

B1235 | A problem in the air mix control motor circuit, linkage, door, or motor (driver's) | Climate control unit | Signal error

B1236*2 | An open in the passenger's air mix control motor circuit | Climate control unit | Signal error

B1237*2 | A short in the passenger's air mix control motor circuit | Climate control unit | Signal error

B1238*2 | A problem in the passenger's air mix control motor circuit, linkage, door, or motor | Climate control unit | Signal error

B123F | Automatic lighting control unit/sunlight sensor error | Climate control unit | Signal error

B1240 | A problem in the mode control motor circuit, linkage, door, or motor | Climate control unit | Signal error

B1241 | A problem in the blower motor circuit | Climate control unit | Signal error

B2964 | Climate control unit lost communication with front panel (climate control panel) | Climate control unit | Loss of communication

B2983 | A problem in the recirculation control motor circuit, linkage, door, or motor | Climate control unit | Signal error

B2986 | An open in the recirculation control motor circuit | Climate control unit | Signal error

B2988*1 | A problem in the A/C compressor variable capacity control solenoid circuit | Climate control unit | Signal error

U1280 | Communication bus line error (BUS-OFF) | Climate control unit | Loss of communication

U1281 | Climate control unit lost communication with MICU (body control module) | Climate control unit | Loss of communication

U128D | Climate control unit lost communication with gauge control module | Climate control unit | Loss of communication

U1290*3 | Climate control unit lost communication with seat heater control unit (front) | Climate control unit | Loss of communication

*1: With A/C

*2: With dual zone climate control

*3: With seat heater
````

## Chunk 8716: How to Check for DTCs with the HDS

- Title: How to Check for DTCs with the HDS
- Source path: `pages\11305.html`
- Chunk ID: `chunk_41b4d59a44dd`
- Images: `images\GHH409243.jpeg`
- Duplicate sources: `pages\11314.html`, `pages\16184.html`, `pages\16193.html`

### Full Text

````text
# How to Check for DTCs with the HDS

NOTE:

- There are three methods used to check for DTCs. The recommended method is to use the Honda Diagnostic System (HDS) with the appropriate software, plugged into the data link connector (DLC).

- The second method is to run the self-diagnostic function built into the climate control unit.

- The third method is to use B-CAN system diagnosis test mode A .

1. Make sure the vehicle ignition is in the OFF (LOCK) mode.

2. Connect the HDS to the DLC (A) located under the driver's side of the dashboard.

Courtesy of HONDA, U.S.A., INC.

3. Turn the vehicle to the ON mode.

4. Make sure the HDS communicates with the vehicle and the climate control unit. If it does not, go to the DLC circuit troubleshooting

5. Select BODY ELECTRICAL in the System Selection Menu.

6. Select HVAC/Climate control in the Body Electrical System Select.

7. Select DTCs in the HVAC/Climate Control Mode Menu. Check for DTCs. If any DTCs are indicated, write down the DTCs, then go to the indicated DTC troubleshooting. If no DTCs are indicated, do all system scan, then refer to symptom troubleshooting.

NOTE:

- After troubleshooting, clear the DTCs with the HDS.

- For specific operations, refer to the user's manual that came with the HDS.
````

## Chunk 8717: How to Use the Self-Diagnostic Function with the HDS

- Title: How to Use the Self-Diagnostic Function with the HDS
- Source path: `pages\11306.html`
- Chunk ID: `chunk_68266b15a376`
- Images: none
- Duplicate sources: `pages\11315.html`, `pages\16185.html`, `pages\16194.html`

### Full Text

````text
# How to Use the Self-Diagnostic Function with the HDS

NOTE: This method is only available if the HDS can communicate with the climate control unit.

1. Make sure the vehicle ignition is in the OFF (LOCK) mode.

2. Connect the HDS to the DLC.

3. Turn the vehicle to the ON mode.

4. Make sure the HDS communicates with the vehicle and the climate control unit. If it does not, go to the DLC circuit troubleshooting

5. Select BODY ELECTRICAL in the System Selection Menu.

6. Select HVAC/Climate Control in the Body Electrical System Select.

7. Select Inspection in the HVAC/Climate Control Mode Menu.

8. Select Climate Control Unit Self Test in the Inspection Menu. Check for DTCs. If any DTCs are indicated, write down the DTCs, then go to the indicated DTC troubleshooting.

NOTE:

- After troubleshooting, clear the DTCs with the HDS.

- For specific operations, refer to the user's manual that came with the HDS.
````

## Chunk 8718: How to Use the Self-Diagnostic Function without the HDS

- Title: How to Use the Self-Diagnostic Function without the HDS
- Source path: `pages\11307.html`
- Chunk ID: `chunk_57035b1cf502`
- Images: `images\GHH409244.jpeg`, `images\GHH409245.jpeg`, `images\GHH409246.jpeg`, `images\GHH409247.jpeg`, `images\GHH409248.jpeg`
- Duplicate sources: `pages\16186.html`

### Full Text

````text
# How to Use the Self-Diagnostic Function without the HDS

Button

Button | Button Name

Courtesy of HONDA, U.S.A., INC. | AUTO button

Courtesy of HONDA, U.S.A., INC. | ON/OFF button

Courtesy of HONDA, U.S.A., INC. | REAR WINDOW DEFOGGER/MIRROR DEFOGGER * button

Courtesy of HONDA, U.S.A., INC. | RECIRCULATION button

Courtesy of HONDA, U.S.A., INC. | WINDSHIELD DEFROST button

*: With mirror defogger

The climate control unit has a self-diagnostic function. To run the self-diagnostic function, do the following:

1. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

2. Press the ON/OFF button to turn on the climate control system if it is off.

3. Press and hold the ON/OFF button, then within 10 seconds press and release the REAR WINDOW DEFOGGER/MIRROR DEFOGGER * button five times. Release the ON/OFF button.*: With mirror defogger ALL LCD segments come on for 2 seconds, then the self-diagnostic function begins.

NOTE:

- The blower motor will run at various speeds regardless of what the panel is displaying.

- If there is any problem in the system, the temperature indicator flashes 88. Refer to checking for DTCs.

- If there is more than one DTC, they are displayed one at a time in sequence followed by a pause (all the display indicator segments illuminate) between the DTCs.

- If no DTCs are present, the temperature indicator will flash "no".

Canceling the Self-Diagnostic Function

5. Turn the vehicle to the OFF (LOCK) mode to cancel the self-diagnostic function. After completing any repairs, run the self-diagnostic function again to make sure that there are no other DTCs.
````

## Chunk 8719: Checking for DTCs

- Title: Checking for DTCs
- Source path: `pages\11308.html`
- Chunk ID: `chunk_fa10a39ce522`
- Images: none
- Duplicate sources: `pages\16187.html`

### Full Text

````text
# Checking for DTCs

The temperature indicator display indicates single or multiple DTCs. If no DTCs are present, the temperature indicator will flash "no".

DTC (Temperature Indicator Segments) | DTC | Detection Item

01 | B1225 | An open in the in-car temperature sensor circuit

02 | B1226 | A short in the in-car temperature sensor circuit

05 | B1227 | An open in the outside air temperature sensor circuit

06 | B1228 | A short in the outside air temperature sensor circuit

09 * | B1231 | An open in the evaporator temperature sensor circuit

0A * | B1232 | A short in the evaporator temperature sensor circuit

17 | B123F | Automatic lighting control unit/sunlight sensor error

40 | B1233 | An open in the air mix control motor circuit

41 | B1234 | A short in the air mix control motor circuit

42 | B1235 | A problem in the air mix control motor circuit, linkage, door, or motor

49 | B121A | An open in the mode control motor circuit

4A | B121B | A short in the mode control motor circuit

4b | B1240 | A problem in the mode control motor circuit, linkage, door, or motor

55 | B2986 | An open in the recirculation control motor circuit

56 | B1220 | A short in the recirculation control motor circuit

57 | B2983 | A problem in the recirculation control motor circuit, linkage, door, or motor

59 | B1241 | A problem in the blower motor circuit

61 * | B2988 | A problem in the A/C compressor variable capacity control solenoid circuit

80 | U1280 | Communication bus line error (BUS-OFF)

83 | U128D | Climate control unit lost communication with gauge control module (VSP message)

8A | B120A | Climate control unit LIN communication bus line error

91 | U1281 | Climate control unit lost communication with MICU (body control module)

93 | B2964 | Climate control unit lost communication with front panel (climate control panel)

C0 | --- | Climate control unit internal error

Cd | --- | Unknown sunlight sensor type

*: With A/C
````

## Chunk 8720: How to Check for History DTCs

- Title: How to Check for History DTCs
- Source path: `pages\11309.html`
- Chunk ID: `chunk_db1b120a68b4`
- Images: none
- Duplicate sources: `pages\16188.html`

### Full Text

````text
# How to Check for History DTCs

The climate control unit can record history DTCs. To read the history DTCs, do the following:

1. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

2. While pressing the WINDSHIELD DEFROST button, press and hold the ON/OFF button for 10 seconds or more.While pressing and holding both the WINDSHIELD DEFROST and ON/OFF buttons, the history DTCs will be indicated.

NOTE:

- If there is any problem in the system, the temperature indicator flashes 88. Refer to checking for DTCs.

- If there is more than one DTC, they are displayed one at a time in sequence followed by a pause (all the display indicator segments illuminate) between the DTCs.

- If no DTCs are present, the temperature indicator will flash "no".

Canceling the Read History DTCs

4. Turn the vehicle to the OFF (LOCK) mode to cancel the history DTCs. After completing the repair work, clear the DTCs.
````

## Chunk 8721: How to Clear the History DTCs

- Title: How to Clear the History DTCs
- Source path: `pages\11310.html`
- Chunk ID: `chunk_91df221afb5b`
- Images: none
- Duplicate sources: `pages\16189.html`

### Full Text

````text
# How to Clear the History DTCs

1. Turn the vehicle to the OFF (LOCK) mode.

2. Press and hold both the AUTO and WINDSHIELD DEFROST buttons, then turn the vehicle to the ON mode.

3. After about 5 seconds the windshield defrost indicator starts to blink, release the buttons.

4. Do the How to Check for History DTCs to verify DTCs have been cleared.
````

## Chunk 8722: Displaying Sensor Inputs at the Climate Control Unit

- Title: Displaying Sensor Inputs at the Climate Control Unit
- Source path: `pages\11311.html`
- Chunk ID: `chunk_d19cff083493`
- Images: none
- Duplicate sources: `pages\11320.html`, `pages\16190.html`, `pages\16199.html`

### Full Text

````text
# Displaying Sensor Inputs at the Climate Control Unit

The climate control unit has a mode that displays the sensor inputs it receives. This mode shows you what the climate control unit is receiving from each of the sensors, one at a time, and it can help you determine if a sensor is faulty.
````

## Chunk 8723: Checks Before Using the Sensor Input Display Mode

- Title: Checks Before Using the Sensor Input Display Mode
- Source path: `pages\11312.html`
- Chunk ID: `chunk_6780ce81fee4`
- Images: none
- Duplicate sources: `pages\16191.html`

### Full Text

````text
# Checks Before Using the Sensor Input Display Mode

1. Turn the vehicle to the ON mode, and check the recirculation door function; press the RECIRCULATION button to switch from FRESH to RECIRCULATE. The air volume and sound should change slightly. Set the TEMPERATURE CONTROL dial to the desired test temperature:

- "Lo" temperature setting will default to MAX COOL, VENT, and RECIRCULATE (A/C on) or FRESH (A/C off).

- "Hi" temperature setting will default to MAX HOT, HEAT, HEAT/DEF and FRESH.

3. Turn the vehicle to the OFF (LOCK) mode.
````

## Chunk 8724: Run the Sensor Input Display Mode

- Title: Run the Sensor Input Display Mode
- Source path: `pages\11313.html`
- Chunk ID: `chunk_80ee9b8d0a3a`
- Images: `images\GHH409249.jpeg`, `images\GHH409250.jpeg`, `images\GHH409251.jpeg`, `images\GHH409252.jpeg`, `images\GHH409253.jpeg`
- Duplicate sources: `pages\16192.html`

### Full Text

````text
# Run the Sensor Input Display Mode

1. Press and hold both the AUTO and RECIRCULATION buttons, then start the engine.

2. Release both buttons. The temperature indicator will flash the sensor number and then the value for that sensor. Record the value displayed.

3. To advance to the next sensor, press the REAR WINDOW DEFOGGER/MIRROR DEFOGGER * button.*: With mirror defogger To cancel the sensor input display mode, press the AUTO button or turn the vehicle to the OFF (LOCK) mode.

NOTE:

- The sensor values will be displayed in degrees Celsius (deg.C) or an alphanumeric code. Use the chart to convert the value to degrees Fahrenheit (deg.F).

- If the sensor value displays "Er", this indicates there is an open or short in the circuit or sensor. Check for DTCs using the HDS, or use the climate control self-diagnostic function.

- If necessary, compare the sensor input display to a known-good vehicle under the same test conditions.

- If the sensor displayed value is out of the normal range, refer to the sensor test or substitute a known-good sensor, and recheck.

- Unsupported items shall be skipped.

Sensor | Item | Displayed Value

0 | In-car temperature sensor | deg.C

1 | Outside air temperature sensor | deg.C

2 | Sunlight sensor | 10 W/m 2.h

3 | Engine coolant temperature | deg.C

4 | Evaporator temperature sensor | deg.C

8 | Air mix opening (low value indicates cooler air distribution, higher value indicates warmer air distribution) | % of opening

9 | Passenger's air mix opening (low value indicates cooler air distribution, higher value indicates warmer air distribution) | % of opening

b | Mode positioning | 0.1 V

d | Recirculation control opening | % of opening

F | Vehicle speed (vehicle must be driven to display speed) | 10 km/h

H | A/C compressor oil circulation | Finished: 1 Unfinished: 0

- Finished: 1

- Unfinished: 0

L | Sunlight sensor type | Hard Wire: 00 BCAN: 99 Unknown: --

- Hard Wire: 00

- BCAN: 99

- Unknown: --

o | Not used | ---

Celsius to Fahrenheit Conversion Table

deg.C | deg.F | deg.C | deg.F | deg.C | deg.F | deg.C | deg.F | deg.C | deg.F

0 | 32 | 10 | 50 | 20 | 68 | 30 | 86 | 40 | 104

1 | 34 | 11 | 52 | 21 | 70 | 31 | 88 | 41 | 106

2 | 36 | 12 | 54 | 22 | 72 | 32 | 90 | 42 | 108

3 | 37 | 13 | 55 | 23 | 73 | 33 | 91 | 43 | 109

4 | 39 | 14 | 57 | 24 | 75 | 34 | 93 | 44 | 111

5 | 41 | 15 | 59 | 25 | 77 | 35 | 95 | 45 | 113

6 | 43 | 16 | 61 | 26 | 79 | 36 | 97 | 46 | 115

7 | 45 | 17 | 63 | 27 | 81 | 37 | 99 | 47 | 117

8 | 46 | 18 | 64 | 28 | 82 | 38 | 100 | 48 | 118

9 | 48 | 19 | 66 | 29 | 84 | 39 | 102 | 49 | 120

deg.C | deg.F | deg.C | deg.F | deg.C | deg.F | deg.C | deg.F | deg.C | deg.F

50 | 122 | 60 | 140 | 70 | 158 | 80 | 176 | 90 | 194

deg.C | deg.F | deg.C | deg.F | deg.C | deg.F | deg.C | deg.F | deg.C | deg.F

51 | 124 | 61 | 142 | 71 | 160 | 81 | 178 | 91 | 196

52 | 126 | 62 | 144 | 72 | 162 | 82 | 180 | 92 | 198

53 | 127 | 63 | 145 | 73 | 163 | 83 | 181 | 93 | 199

54 | 129 | 64 | 147 | 74 | 165 | 84 | 183 | 94 | 201

55 | 131 | 65 | 149 | 75 | 167 | 85 | 185 | 95 | 203

56 | 133 | 66 | 151 | 76 | 169 | 86 | 187 | 96 | 205

57 | 135 | 67 | 153 | 77 | 171 | 87 | 189 | 97 | 207

58 | 136 | 68 | 154 | 78 | 172 | 88 | 190 | 98 | 208

59 | 138 | 69 | 156 | 79 | 174 | 89 | 192 | 99 | 210

Alphanumeric Conversion Table

Display Reading (Alphanumeric) | deg.C | deg.F | %

0 thru 99 | 0 thru 99 | 32 thru 210 | 0 thru 99

A1 thru A9 | -1 thru -9 | 30 thru 16 | -1 thru -10

B0 thru B9 | -10 thru -19 | 14 thru -2 | -10 thru -19

C0 thru C9 | -20 thru -29 | -4 thru -20 | -20 thru -29

D0 thru D9 | -30 thru -39 | -22 thru -38 | -30 thru -39

E0 thru E9 | -40 thru -49 | -40 thru -56 | -40 thru -49

F0 thru F8 | 100 thru 108 | 212 thru 226 | 100 thru 108

F9 | 109 thru 200 | 228 thru 392 | 109 thru 200

Alphanumeric Conversion Table (Mode Positioning)

Display Reading (Volt) | Mode Position

0.5 | Courtesy of HONDA, U.S.A., INC.

1.3 or 1.9 | Courtesy of HONDA, U.S.A., INC.

2.6 | Courtesy of HONDA, U.S.A., INC.

3.2 or 3.7 | Courtesy of HONDA, U.S.A., INC.

4.5 | Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8725: How to Use the Self-Diagnostic Function without the HDS

- Title: How to Use the Self-Diagnostic Function without the HDS
- Source path: `pages\11316.html`
- Chunk ID: `chunk_29cf2b5f3ce8`
- Images: `images\GHH409255.jpeg`, `images\GHH409256.jpeg`, `images\GHH409257.jpeg`, `images\GHH409258.jpeg`, `images\GHH409259.jpeg`, `images\GHH409260.jpeg`
- Duplicate sources: `pages\16195.html`

### Full Text

````text
# How to Use the Self-Diagnostic Function without the HDS

BUTTON

Button | Button Name

Courtesy of HONDA, U.S.A., INC. | AUTO button

Courtesy of HONDA, U.S.A., INC. | ON/OFF button

Courtesy of HONDA, U.S.A., INC. | REAR WINDOW DEFOGGER/MIRROR DEFOGGER * button

Courtesy of HONDA, U.S.A., INC. | RECIRCULATION button

Courtesy of HONDA, U.S.A., INC. | WINDSHIELD DEFROST button

*: With mirror defogger

The climate control unit has a self-diagnostic function. To run the self-diagnostic function, do the following:

1. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

2. Press the ON/OFF button to turn on the climate control system if it is off. Press and hold the ON/OFF button, then within 10 seconds press and release the REAR WINDOW DEFOGGER/MIRROR DEFOGGER * button five times. Release the ON/OFF button, then the self-diagnostic function begins.*: With mirror defogger

NOTE:

- The blower motor should run at various speeds when in the self-diagnostic mode.

- If there are any problems in the system, the A/C Error Display screen will indicate them. Select the previous/next icon to confirm the DTCs. To determine the meaning of the indication, refer to the table that follows.

- If there are no problems detected, the error status shows Normal, and The number of Errors indicates "0".

Courtesy of HONDA, U.S.A., INC.

Canceling the Self-Diagnostic Function

4. Turn the vehicle to the OFF (LOCK) mode to cancel the self-diagnostic function. After completing any repairs, run the self-diagnostic function again to make sure that there are no other DTCs.
````

## Sources Used

- `pages\10611.html`
- `pages\10612.html`
- `pages\10613.html`
- `pages\10614.html`
- `pages\10615.html`
- `pages\10616.html`
- `pages\10617.html`
- `pages\10618.html`
- `pages\10619.html`
- `pages\10620.html`
- `pages\10621.html`
- `pages\10622.html`
- `pages\10623.html`
- `pages\10624.html`
- `pages\10625.html`
- `pages\10626.html`
- `pages\10627.html`
- `pages\10628.html`
- `pages\10629.html`
- `pages\10630.html`
- `pages\10631.html`
- `pages\10632.html`
- `pages\10633.html`
- `pages\10634.html`
- `pages\10635.html`
- `pages\10636.html`
- `pages\10637.html`
- `pages\10638.html`
- `pages\10639.html`
- `pages\10640.html`
- `pages\10641.html`
- `pages\10642.html`
- `pages\10643.html`
- `pages\10644.html`
- `pages\10645.html`
- `pages\10646.html`
- `pages\10647.html`
- `pages\10648.html`
- `pages\10649.html`
- `pages\10653.html`
- `pages\10655.html`
- `pages\10656.html`
- `pages\10657.html`
- `pages\10658.html`
- `pages\10659.html`
- `pages\10660.html`
- `pages\10661.html`
- `pages\10662.html`
- `pages\10664.html`
- `pages\10668.html`
- `pages\10669.html`
- `pages\10670.html`
- `pages\10671.html`
- `pages\10672.html`
- `pages\10673.html`
- `pages\10674.html`
- `pages\10675.html`
- `pages\10676.html`
- `pages\10677.html`
- `pages\10678.html`
- `pages\10679.html`
- `pages\10680.html`
- `pages\10681.html`
- `pages\10682.html`
- `pages\10684.html`
- `pages\10685.html`
- `pages\10686.html`
- `pages\10687.html`
- `pages\10688.html`
- `pages\10689.html`
- `pages\10690.html`
- `pages\10691.html`
- `pages\10692.html`
- `pages\10693.html`
- `pages\10694.html`
- `pages\10695.html`
- `pages\10696.html`
- `pages\10697.html`
- `pages\10698.html`
- `pages\10701.html`
- `pages\10702.html`
- `pages\10703.html`
- `pages\10704.html`
- `pages\10705.html`
- `pages\10706.html`
- `pages\10707.html`
- `pages\10708.html`
- `pages\10709.html`
- `pages\10710.html`
- `pages\10711.html`
- `pages\10712.html`
- `pages\10713.html`
- `pages\10715.html`
- `pages\10716.html`
- `pages\10717.html`
- `pages\10718.html`
- `pages\10719.html`
- `pages\10720.html`
- `pages\10721.html`
- `pages\10722.html`
- `pages\10723.html`
- `pages\10724.html`
- `pages\10725.html`
- `pages\10726.html`
- `pages\10727.html`
- `pages\10728.html`
- `pages\10729.html`
- `pages\10730.html`
- `pages\10731.html`
- `pages\10732.html`
- `pages\10733.html`
- `pages\10734.html`
- `pages\10735.html`
- `pages\10736.html`
- `pages\10737.html`
- `pages\10739.html`
- `pages\10740.html`
- `pages\10741.html`
- `pages\10742.html`
- `pages\10743.html`
- `pages\10746.html`
- `pages\10747.html`
- `pages\10748.html`
- `pages\10749.html`
- `pages\10750.html`
- `pages\10751.html`
- `pages\10752.html`
- `pages\10753.html`
- `pages\10754.html`
- `pages\10755.html`
- `pages\10756.html`
- `pages\10757.html`
- `pages\10758.html`
- `pages\10759.html`
- `pages\10761.html`
- `pages\10762.html`
- `pages\10763.html`
- `pages\10764.html`
- `pages\10765.html`
- `pages\10766.html`
- `pages\10767.html`
- `pages\10768.html`
- `pages\10769.html`
- `pages\10770.html`
- `pages\10771.html`
- `pages\10772.html`
- `pages\10773.html`
- `pages\10774.html`
- `pages\10775.html`
- `pages\10776.html`
- `pages\10777.html`
- `pages\10778.html`
- `pages\10779.html`
- `pages\10780.html`
- `pages\10781.html`
- `pages\10782.html`
- `pages\10783.html`
- `pages\10784.html`
- `pages\10785.html`
- `pages\10786.html`
- `pages\10787.html`
- `pages\10788.html`
- `pages\10789.html`
- `pages\10790.html`
- `pages\10792.html`
- `pages\10794.html`
- `pages\10795.html`
- `pages\10796.html`
- `pages\10797.html`
- `pages\10798.html`
- `pages\10799.html`
- `pages\10800.html`
- `pages\10801.html`
- `pages\10802.html`
- `pages\10803.html`
- `pages\10804.html`
- `pages\10805.html`
- `pages\10806.html`
- `pages\10807.html`
- `pages\10808.html`
- `pages\10809.html`
- `pages\10810.html`
- `pages\10811.html`
- `pages\10812.html`
- `pages\10813.html`
- `pages\10814.html`
- `pages\10815.html`
- `pages\10817.html`
- `pages\10818.html`
- `pages\10819.html`
- `pages\10820.html`
- `pages\10821.html`
- `pages\10822.html`
- `pages\10823.html`
- `pages\10824.html`
- `pages\10825.html`
- `pages\10826.html`
- `pages\10827.html`
- `pages\10829.html`
- `pages\10830.html`
- `pages\10831.html`
- `pages\10833.html`
- `pages\10834.html`
- `pages\10835.html`
- `pages\10837.html`
- `pages\10838.html`
- `pages\10839.html`
- `pages\10840.html`
- `pages\10841.html`
- `pages\10842.html`
- `pages\10843.html`
- `pages\10844.html`
- `pages\10845.html`
- `pages\10846.html`
- `pages\10847.html`
- `pages\10918.html`
- `pages\10919.html`
- `pages\10920.html`
- `pages\10921.html`
- `pages\10922.html`
- `pages\10923.html`
- `pages\10924.html`
- `pages\10929.html`
- `pages\10930.html`
- `pages\10931.html`
- `pages\11014.html`
- `pages\11015.html`
- `pages\11016.html`
- `pages\11017.html`
- `pages\11020.html`
- `pages\11021.html`
- `pages\11022.html`
- `pages\11023.html`
- `pages\11024.html`
- `pages\11025.html`
- `pages\11026.html`
- `pages\11027.html`
- `pages\11028.html`
- `pages\11029.html`
- `pages\11030.html`
- `pages\11031.html`
- `pages\11032.html`
- `pages\11033.html`
- `pages\11034.html`
- `pages\11035.html`
- `pages\11036.html`
- `pages\11037.html`
- `pages\11038.html`
- `pages\11039.html`
- `pages\11040.html`
- `pages\11041.html`
- `pages\11042.html`
- `pages\11043.html`
- `pages\11044.html`
- `pages\11045.html`
- `pages\11046.html`
- `pages\11047.html`
- `pages\11048.html`
- `pages\11049.html`
- `pages\11050.html`
- `pages\11051.html`
- `pages\11052.html`
- `pages\11053.html`
- `pages\11054.html`
- `pages\11055.html`
- `pages\11056.html`
- `pages\11057.html`
- `pages\11058.html`
- `pages\11059.html`
- `pages\11060.html`
- `pages\11061.html`
- `pages\11062.html`
- `pages\11063.html`
- `pages\11064.html`
- `pages\11065.html`
- `pages\11066.html`
- `pages\11067.html`
- `pages\11068.html`
- `pages\11069.html`
- `pages\11070.html`
- `pages\11071.html`
- `pages\11072.html`
- `pages\11073.html`
- `pages\11074.html`
- `pages\11075.html`
- `pages\11076.html`
- `pages\11077.html`
- `pages\11078.html`
- `pages\11079.html`
- `pages\11080.html`
- `pages\11081.html`
- `pages\11082.html`
- `pages\11083.html`
- `pages\11084.html`
- `pages\11085.html`
- `pages\11086.html`
- `pages\11087.html`
- `pages\11088.html`
- `pages\11089.html`
- `pages\11090.html`
- `pages\11091.html`
- `pages\11093.html`
- `pages\11095.html`
- `pages\11099.html`
- `pages\11100.html`
- `pages\11112.html`
- `pages\11113.html`
- `pages\11117.html`
- `pages\11118.html`
- `pages\11119.html`
- `pages\11121.html`
- `pages\11122.html`
- `pages\11123.html`
- `pages\11124.html`
- `pages\11125.html`
- `pages\11126.html`
- `pages\11127.html`
- `pages\11128.html`
- `pages\11129.html`
- `pages\11130.html`
- `pages\11131.html`
- `pages\11132.html`
- `pages\11134.html`
- `pages\11135.html`
- `pages\11136.html`
- `pages\11137.html`
- `pages\11138.html`
- `pages\11139.html`
- `pages\11140.html`
- `pages\11142.html`
- `pages\11145.html`
- `pages\11146.html`
- `pages\11147.html`
- `pages\11149.html`
- `pages\11150.html`
- `pages\11151.html`
- `pages\11152.html`
- `pages\11153.html`
- `pages\11154.html`
- `pages\11155.html`
- `pages\11156.html`
- `pages\11158.html`
- `pages\11161.html`
- `pages\11162.html`
- `pages\11163.html`
- `pages\11164.html`
- `pages\11165.html`
- `pages\11166.html`
- `pages\11167.html`
- `pages\11168.html`
- `pages\11170.html`
- `pages\11171.html`
- `pages\11174.html`
- `pages\11175.html`
- `pages\11176.html`
- `pages\11177.html`
- `pages\11178.html`
- `pages\11179.html`
- `pages\11180.html`
- `pages\11181.html`
- `pages\11182.html`
- `pages\11184.html`
- `pages\11185.html`
- `pages\11186.html`
- `pages\11187.html`
- `pages\11188.html`
- `pages\11189.html`
- `pages\11193.html`
- `pages\11194.html`
- `pages\11195.html`
- `pages\11196.html`
- `pages\11197.html`
- `pages\11198.html`
- `pages\11201.html`
- `pages\11204.html`
- `pages\11209.html`
- `pages\11211.html`
- `pages\11213.html`
- `pages\11214.html`
- `pages\11215.html`
- `pages\11216.html`
- `pages\11217.html`
- `pages\11218.html`
- `pages\11219.html`
- `pages\11220.html`
- `pages\11290.html`
- `pages\11292.html`
- `pages\11303.html`
- `pages\11304.html`
- `pages\11305.html`
- `pages\11306.html`
- `pages\11307.html`
- `pages\11308.html`
- `pages\11309.html`
- `pages\11310.html`
- `pages\11311.html`
- `pages\11312.html`
- `pages\11313.html`
- `pages\11316.html`
