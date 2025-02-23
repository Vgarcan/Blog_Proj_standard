# **CSS Documentation for Programming Cookbook**

---

## **Table of Contents**
1. [Global Configuration](#1-global-configuration)
2. [Base Typography](#2-base-typography)
3. [Navbar](#3-navbar)
4. [Table of Contents](#4-table-of-contents)
5. [Code Blocks](#5-code-blocks)
6. [Notification Boxes](#6-notification-boxes)
7. [Tables](#7-tables)
8. [Pagination](#8-pagination)
9. [Footer](#9-footer)
10. [Search Bar](#10-search-bar)
11. [Badges](#11-badges)
12. [Progress Bars](#12-progress-bars)
13. [Modals](#13-modals)
14. [Tabs](#14-tabs)
15. [Tooltips](#15-tooltips)
16. [Toggles](#16-toggles)
17. [Accordions](#17-accordions)
18. [Carousels](#18-carousels)
19. [Timeline](#19-timeline)
20. [Avatars](#20-avatars)
21. [Cards](#21-cards)
22. [Tags](#22-tags)
23. [Pricing Tables](#23-pricing-tables)
24. [Floating Action Button](#24-floating-action-button)
25. [Light/Dark Mode](#25-lightdark-mode)
26. [Breadcrumbs](#26-breadcrumbs)
27. [Scroll to Top](27-#scroll-to-top)
28. [Custom Select Box](#28-custom-select-box)
29. [Custom Checkboxes and Radio Buttons](#29-custom-checkboxes-and-radio-buttons)
30. [Transitions and Animations](#30-transitions-and-animations)
31. [Loading Spinner](#31-loading-spinner)
32. [Custom Progress Bar](#32-custom-progress-bar)

---

## **1. Global Configuration**
All variables are declared in `custom-root.css`. They follow Bootstrap-like variable names.

- **Font Families**:
  - `--bs-font-sans-serif`: Default sans-serif font.
  - `--bs-font-monospace`: For code blocks.

- **Colors**:
  - `--bs-primary`: Primary color
  - `--bs-secondary`: Secondary color
  - `--bs-success`: Success color
  - `--bs-danger`: Danger color
  - `--bs-warning`: Warning color
  - `--bs-light`: Light background
  - `--bs-dark`: Dark background

- **Shadows**:
  - `--bs-box-shadow-sm`: Small shadow
  - `--bs-box-shadow-lg`: Large shadow

Example Usage:
```css
background-color: var(--bs-primary);
box-shadow: var(--bs-box-shadow-lg);
```

---

## **2. Base Typography**
Styles for text elements like headings, paragraphs, and blockquotes.

| **Element**     | **Description**                             |
|-----------------|---------------------------------------------|
| `h1, h2, h3...` | Bold headings with margins and sizes.       |
| `p, li`         | Paragraphs and lists with spacing.          |
| `blockquote`    | Italicized quote with a left border.        |

**Usage Example:**
```html
<h1>Main Title</h1>
<p>This is a paragraph.</p>
<blockquote>This is a highlighted quote.</blockquote>
```

---

## **3. Navbar**
A responsive sticky navigation bar.

- **Classes**:
  - `.navbar`: Main navbar container.
  - `.navbar a`: Links inside navbar.
  - `.navbar a:hover`: Hover effect.

**Usage Example:**
```html
<nav class="navbar">
  <a href="#">Home</a>
  <a href="#">About</a>
</nav>
```

---

## **4. Table of Contents**
Used for creating a table of contents with links.

- **Classes**:
  - `.table-of-contents`: Wrapper for TOC.
  - `.table-of-contents a`: Links to sections.

**Usage Example:**
```html
<div class="table-of-contents">
  <h3>Contents</h3>
  <a href="#section1">Section 1</a>
  <a href="#section2">Section 2</a>
</div>
```

---

## **5. Code Blocks**
Styling for code snippets and preformatted text.

- **Classes**:
  - `pre`: Code container with padding.
  - `code`: Inline code.

**Usage Example:**
```html
<pre><code>console.log('Hello, World!');</code></pre>
```

---

## **6. Notification Boxes**
Colored boxes for notes, warnings, and examples.

| **Class**      | **Description**                   |
|----------------|-----------------------------------|
| `.note`        | Blue box for informational notes. |
| `.warning`     | Yellow box for warnings.          |
| `.example`     | Green box for examples.           |

**Usage Example:**
```html
<div class="note">This is a note.</div>
<div class="warning">This is a warning.</div>
<div class="example">This is an example.</div>
```

---

## **7. Tables**
Custom tables with alternating row colors and hover effects.

- **Classes**:
  - `.table`: Main table container.
  - `th, td`: Table cells.
  - `tbody tr:hover`: Hover effect for rows.

**Usage Example:**
```html
<table class="table">
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Row 1</td>
      <td>Content</td>
    </tr>
  </tbody>
</table>
```

---

## **8. Pagination**
Custom pagination elements with hover effects.

- **Classes**:
  - `.pagination`: Wrapper for pagination.
  - `.pagination a`: Links for pages.
  - `.pagination a.active`: Active page.

**Usage Example:**
```html
<div class="pagination">
  <a href="#">1</a>
  <a href="#" class="active">2</a>
  <a href="#">3</a>
</div>
```

---

## **9. Footer**
Custom footer styling.

- **Classes**:
  - `.footer`: Footer container.
  - `.footer a`: Links in the footer.

**Usage Example:**
```html
<footer class="footer">
  <p>&copy; 2024 Programming Cookbook</p>
</footer>
```

---

## **10. Search Bar**
Search input field with button.

- **Classes**:
  - `.search-bar`: Wrapper for search.
  - `.search-bar input`: Input field.
  - `.search-bar button`: Submit button.

**Usage Example:**
```html
<div class="search-bar">
  <input type="text" placeholder="Search...">
  <button>Search</button>
</div>
```

---

## **11. Badges**
Custom badges for highlighting.

| **Class**        | **Description**              |
|------------------|------------------------------|
| `.badge`         | Default badge styling.       |
| `.badge-primary` | Primary colored badge.       |
| `.badge-success` | Success colored badge.       |

**Usage Example:**
```html
<span class="badge badge-primary">New</span>
<span class="badge badge-success">Success</span>
```

---

## **12. Progress Bars**
Custom progress bars with transitions.

- **Classes**:
  - `.progress`: Main progress bar container.
  - `.progress-bar`: Inner progress bar.

**Usage Example:**
```html
<div class="progress">
  <div class="progress-bar" style="width: 70%">70%</div>
</div>
```

---

## **13. Modals**
Custom modal window with overlay.

- **Classes**:
  - `.modal`: Modal background.
  - `.modal-dialog`: Modal content container.

**Usage Example:**
```html
<div class="modal active">
  <div class="modal-dialog">
    <div class="modal-header">Modal Title</div>
    <div class="modal-body">Content here</div>
  </div>
</div>
```

---

## **14. Tabs**
Custom tab system to switch between content.

- **Classes**:
  - `.tabs`: Wrapper for the tab headers.
  - `.tab`: Individual tab button.
  - `.tab.active`: Active tab.
  
**Usage Example:**
```html
<div class="tabs">
  <div class="tab active">Tab 1</div>
  <div class="tab">Tab 2</div>
</div>
<div class="tab-content">
  <p>Content for Tab 1</p>
</div>
<div class="tab-content" style="display: none;">
  <p>Content for Tab 2</p>
</div>

---

## **15. Tooltips**
Lightweight tooltips for hovering over elements.

- **Classes**:
  - `.tooltip`: Wrapper for the tooltip.
  - `.tooltip-text`: Content of the tooltip.

**Usage Example:**
```html
<div class="tooltip">
  Hover me
  <span class="tooltip-text">Tooltip content</span>
</div>
```

---

## **16. Toggles**
Custom toggle switches styled as checkboxes.

- **Classes**:
  - `.toggle`: Wrapper for the toggle.
  - `.slider`: Styled switch.
  - `input[type="checkbox"]`: Actual checkbox (hidden).

**Usage Example:**
```html
<label class="toggle">
  <input type="checkbox">
  <span class="slider"></span>
</label>
```

---

## **17. Accordions**
Expandable/collapsible sections for content.

- **Classes**:
  - `.accordion`: Main container for accordions.
  - `.accordion-item`: Individual accordion section.
  - `.accordion-header`: Clickable accordion header.
  - `.accordion-body`: Expandable content.

**Usage Example:**
```html
<div class="accordion">
  <div class="accordion-item active">
    <div class="accordion-header">Header 1</div>
    <div class="accordion-body">Content 1</div>
  </div>
  <div class="accordion-item">
    <div class="accordion-header">Header 2</div>
    <div class="accordion-body">Content 2</div>
  </div>
</div>
```

---

## **18. Carousels**
Rotating sliders for images or content.

- **Classes**:
  - `.carousel`: Main carousel container.
  - `.carousel-slides`: Wrapper for slides.
  - `.carousel-controls`: Navigation controls.

**Usage Example:**
```html
<div class="carousel">
  <div class="carousel-slides">
    <div class="carousel-slide">Slide 1</div>
    <div class="carousel-slide">Slide 2</div>
  </div>
  <div class="carousel-controls">
    <button>Prev</button>
    <button>Next</button>
  </div>
</div>
```

---

## **19. Timeline**
Vertical timeline for events or steps.

- **Classes**:
  - `.timeline`: Main timeline container.
  - `.timeline-item`: Individual timeline event.
  - `.timeline-content`: Event content.

**Usage Example:**
```html
<div class="timeline">
  <div class="timeline-item">
    <div class="timeline-content">
      <h3 class="timeline-title">Step 1</h3>
      <p>Details of step 1.</p>
    </div>
  </div>
</div>
```

---

## **20. Avatars**
Circular images for user profiles.

- **Classes**:
  - `.avatar`: Wrapper for avatar images.
  - `.avatar-status`: Status indicator (online/offline).

**Usage Example:**
```html
<div class="avatar">
  <img src="user.jpg" alt="User">
  <div class="avatar-status"></div>
</div>
```

---

## **21. Cards**
Reusable card components for content.

- **Types**:
  - `.card-header`: Card header section.
  - `.card-body`: Card content.
  - `.card-icon`: Card with icons/images.

**Usage Example:**
```html
<div class="card">
  <div class="card-header">Card Title</div>
  <div class="card-body">Card content.</div>
</div>
```

---

## **22. Tags**
Label-style elements for categorization.

- **Classes**:
  - `.tag`: Basic tag.
  - `.tag-primary`: Primary styled tag.

**Usage Example:**
```html
<span class="tag tag-primary">Tag 1</span>
<span class="tag">Tag 2</span>
```

---

## **23. Pricing Tables**
Tables for pricing plans.

- **Classes**:
  - `.pricing-table`: Wrapper for pricing.
  - `.pricing-plan`: Individual plan container.

**Usage Example:**
```html
<div class="pricing-table">
  <div class="pricing-plan">
    <h3>Basic Plan</h3>
    <p>$10/month</p>
  </div>
</div>
```

---

## **24. Floating Action Button**
Button fixed at the bottom-right.

- **Classes**:
  - `.fab`: Main button style.
  - `.fab-icon`: Icon inside the button.

**Usage Example:**
```html
<button class="fab">
  <span class="fab-icon">+</span>
</button>
```

---

## **25. Light/Dark Mode**
Class-based switch for themes.

- **Classes**:
  - `body.dark-mode`: Activates dark mode styles.

**Usage Example:**
```html
<body class="dark-mode">
  <!-- Dark Mode Enabled -->
</body>
```

---

## **26. Breadcrumbs**
Navigational breadcrumbs for pages.

- **Classes**:
  - `.breadcrumb`: Main breadcrumb container.
  - `.breadcrumb a`: Breadcrumb links.

**Usage Example:**
```html
<div class="breadcrumb">
  <a href="#">Home</a>
  <span>/</span>
  <a href="#">Section</a>
</div>
```

---

## **27. Scroll to Top**
Button to quickly scroll to the top.

- **Classes**:
  - `.scroll-to-top`: Main button style.

**Usage Example:**
```html
<div class="scroll-to-top">↑</div>
```

---

## **28. Custom Select Box**
Styled dropdown select input.

- **Classes**:
  - `.custom-select`: Styled select input.

**Usage Example:**
```html
<select class="custom-select">
  <option>Option 1</option>
  <option>Option 2</option>
</select>
```

---

## **29. Custom Checkboxes and Radio Buttons**
Stylized inputs for forms.

- **Classes**:
  - `.custom-checkbox`: Checkbox style.
  - `.custom-radio`: Radio button style.

**Usage Example:**
```html
<label class="custom-checkbox">
  <input type="checkbox"> Check Me
</label>
<label class="custom-radio">
  <input type="radio" name="radio"> Select Me
</label>
```

---

## **30. Transitions and Animations**
Smooth transitions for various components.

- **Classes**:
  - `.custom-transition`: General transition style.
  - `.slide-down`: Slide-down animation.

**Usage Example:**
```html
<div class="custom-transition slide-down">
  Sliding content.
</div>
```

---

## **31. Loading Spinner**
Animated spinner for loading states.

- **Classes**:
  - `.spinner`: Main spinner.

**Usage Example:**
```html
<div class="spinner"></div>
```

---

## **32. Custom Progress Bar**
Enhanced progress bars.

- **Classes**:
  - `.progress-bar`: Progress bar indicator.

**Usage Example:**
```html
<div class="progress">
  <div class="progress-bar" style="width: 50%;">50%</div>
</div>
```