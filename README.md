# GymManager 🏋️

A simple gym management app built with Python.

## What is it?

GymManager is a gym app that helps manage members, fitness classes, and gym capacity. Track who's at the gym, manage class bookings, and keep everything organized.

## Features

✅ **Members** - Register members, track their gym entries and subscriptions  
✅ **Classes** - Schedule classes like Yoga, Pilates, CrossFit with instructor and capacity  
✅ **Check-ins** - Track who's currently at the gym  
✅ **Capacity Management** - Monitor gym and class occupancy  
✅ **Save & Load** - Export and import gym data

## Quick Start

### Create a member

```python
member = Member(1, "João Silva", 5, True)  # ID, name, entries, subscription
```

### Create a class

```python
yoga_class = Class("Yoga Matinal", "Ana Silva", 15)  # name, instructor, capacity
```

### Set up your gym

```python
gym = Gym("LCD Fit", "Lisboa", 150)  # name, location, capacity
gym.new_member(member)
gym.create_class(yoga_class)
```

## Sample Data Included

The app comes with 10 sample members and 10 sample classes so you can try it out immediately!

## Requirements

- Python 3.x

---

**Project by:** Aline Fontoura (No. 139552)  
**Course:** LCD 2025/2026 - CDA2
