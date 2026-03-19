<!DOCTYPE html>
<html lang="kn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Eco Spice | Online Shopping for Sustainable Spices</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        body { font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background-color: #f1f3f6; }
        .amazon-blue { background-color: #232f3e; }
        .flipkart-blue { background-color: #2874f0; }
        .search-shadow { box-shadow: 0 2px 4px 0 rgba(0,0,0,.23); }
    </style>
</head>
<body>

    <nav class="flipkart-blue p-3 sticky top-0 z-50">
        <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
            <div class="text-white text-2xl font-bold italic">
                Eco<span class="text-yellow-400">Spice</span>
            </div>

            <div class="flex-grow max-w-2xl relative">
                <input type="text" placeholder="Search for eco-friendly spices, pods, and more" 
                       class="w-full py-2 px-4 rounded-sm outline-none search-shadow">
                <button class="absolute right-0 top-0 h-full px-4 text-blue-600">
                    <i class="fas fa-search"></i>
                </button>
            </div>

            <div class="flex items-center gap-8 text-white font-semibold">
                <button class="bg-white text-blue-600 px-8 py-1 rounded-sm">Login</button>
                <a href="#" class="hidden md:block">Become a Seller</a>
                <a href="#" class="flex items-center gap-2">
                    <i class="fas fa-shopping-cart"></i> Cart
                </a>
            </div>
        </div>
    </nav>

    <div class="bg-white shadow-sm py-3 mb-4 hidden md:block">
        <div class="max-w-7xl mx-auto flex justify-around text-sm font-medium text-gray-700">
            <a href="#" class="hover:text-blue-600">Spices Pods</a>
            <a href="#" class="hover:text-blue-600">Combo Kits</a>
            <a href="#" class="hover:text-blue-600">Sustainable Packaging</a>
            <a href="#" class="hover:text-blue-600">Recipes</a>
            <a href="#" class="hover:text-blue-600">Eco-Tracker</a>
            <a href="#" class="hover:text-blue-600">Gift Boxes</a>
        </div>
    </div>

    <div class="max-w-full mx-auto mb-6">
        <div class="relative h-[450px] bg-gray-200 overflow-hidden">
            <img src="URL_OF_YOUR_FIRST_IMAGE" class="w-full h-full object-cover" alt="Eco Spice Banner">
            <div class="absolute inset-0 bg-gradient-to-r from-black/50 to-transparent flex items-center p-12">
                <div class="text-white">
                    <h2 class="text-5xl font-bold mb-4">Simplifying Flavors, <br> Sustainably</h2>
                    <p class="text-xl mb-6">First-of-its-kind edible spice pods for your kitchen.</p>
                    <button class="bg-yellow-400 text-black px-10 py-3 rounded-md font-bold text-lg hover:bg-yellow-500">Shop Now</button>
                </div>
            </div>
        </div>
    </div>

    <div class="max-w-7xl mx-auto px-4 mb-10">
        <div class="flex justify-between items-end mb-4">
            <h3 class="text-2xl font-bold text-gray-800">New Arrivals in Eco Spices</h3>
            <a href="#" class="bg-blue-600 text-white px-4 py-2 text-sm rounded-sm">VIEW ALL</a>
        </div>
        
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4">
            
            <div class="bg-white p-4 hover:shadow-xl transition group">
                <div class="h-56 overflow-hidden mb-4">
                    <img src="URL_OF_YOUR_POD_IMAGE" class="w-full h-full object-contain group-hover:scale-105 transition" alt="Spice Pods">
                </div>
                <h4 class="text-gray-800 font-medium truncate">Eco Spice Pro - Combo Kit (40 Pods)</h4>
                <div class="flex items-center gap-2 my-2">
                    <span class="bg-green-600 text-white text-[10px] px-1 rounded-sm">4.5 ★</span>
                    <span class="text-gray-400 text-xs font-semibold">(2,345)</span>
                </div>
                <div class
