# Hercules 3d printer temperature reporting fix

> UPDATE! This may be fix in config.txt on internal flash of 3d printer
> 
> `temperature_control.hotend.designator T0`
> 
> `temperature_control.hotend2.designator T1`



Fixes the temperature reporting from the printer described in [this OctoPrint forum topic](https://community.octoprint.org/t/extruder-temperature-is-not-shown-on-the-graph/36328/9).

```
EX1:23.1 /0.0 @0 EX2:23.1 /0.0 @0 B:22.6 /0.0 @0
```

This plugin turns the input into the correct format, like this;
```
T0:23.1 /0.0 @0 T1:23.1 /0.0 @0 B:22.6 /0.0 @0
```


**This fix is confirmed to work for the following printers:**

Hercules Strong Duo 2018 and 2019
And may be working with other 3d printers by Imprinta company.


