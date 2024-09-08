# currency_converter
Currency Converter with GUI
A GUI-based Currency Converter is a simple program that instantly converts one form of currency into another. It uses the most recent foreign exchange rates, and therefore, this process can be smooth as it will get, hence very easy for people to handle financial transactions or plan trips.

Features:
Intuitive Interface:

The interface of the currency converter was designed to be the most intuitive and simplest possible so that end-users of any level of technical skill could work with it.
Key elements include the following: amount input field to be converted, source currency, and target currency; buttons such as convert, clear input field, and swap currencies.
Realtime Conversion:

For currency conversion, the application uses a very reliable API that fetches current and real exchange rates. This will ensure that users get the most current and accurate conversion rates available.
Multiple Currencies Supported:

Converter has supported all kinds of currencies from almost all parts of the world. They have the option to select source and target currencies via dropdowns. These reduce the chances of mistakes and accelerate the process.
Error Handling:

The application includes handling various error cases, like invalid input and network failure. In case of invalid input by a user or conversion failure due to network failure, it informs the user about an appropriate message.
Clear and Swap Functions:

A 'Clear' button immediately cleans up all the input fields such that one can start a new conversion with virtually no time wasted.
A 'Swap' button instantly reverses the source and target currency-a feature very useful for frequent travelers and businesspeople who work with more than one form of currency.
Technical Implementation:
The currency converter is coded in Python, utilizing its tkinter library for the GUI components and the currency_converter library to fetch exchange rates. A high-level overview of the implementation of the same is given below:

Initializations:

Application starts up by creating the main window through tkinter.Tk().

It sets up the window with a title and sizes it.

GUI Components: These include: creation of Labels, Entry widgets, and Buttons, which are placed within the window using grid or pack layout managers to ensure the display looks neat and clear. Selection of currency uses ttk.Combobox for richer user experience. Functionality: The conversion logic is created inside a function called convert_currency(). It takes in the input values, does the conversions using the library currency_converter, and then updates the result label. The function clear_fields() clears the input fields along with the result label. Automatically swap the values in the source and target currency fields through the function swap_currencies().
