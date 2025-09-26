+++
title = "System Code"
description = "Follow the white rabbit.\n\nNOTE: Bruteforce is permitted for this challenge instance if you feel it is necessary.\n\nPress the Start button on the top-right to begin this challenge. "
authors = ["mango", "cstef", "Tyr"]
date = 2024-09-30

[taxonomies]
categories = ["misc"]
+++

## Description

Follow the white rabbit.

NOTE: Bruteforce is permitted for this challenge instance if you feel it is necessary.

Press the Start button on the top-right to begin this challenge. 

----

What we tried:

- Enum on `/` and `/enter=` with `gobuster` and custom + `rockyou.txt` wordlists
- Bruteforce on `/enter=` with `ffuf` and custom + `rockyou.txt`
- Recon using `finalrecon`
        - Header inspection
        - DNS records
        - WHOIS
        - URLs inside js/sitemap
        - Images 
- Looking through library assets, they all match the original


## Matrix library diffing with original source

```diff
diff -bur ../../matrix-code-github/js/config.js ./config.js
--- ../../matrix-code-github/js/config.js	2024-10-08 14:28:11.071705089 +0200
+++ ./config.js	2024-10-08 19:00:47.525132778 +0200
@@ -124,6 +124,7 @@
 	useHalfFloat: false,
 	renderer: "regl", // The preferred web graphics API
 	suppressWarnings: false, // Whether to show warnings to visitors on load
+  backupGlyphsTwr: ["a", "b", "c", "d", "e", "f"], // The characters to fallback to if glyphs fail to load
 	isometric: false,
 	useHoloplay: false,
 	loops: false,
@@ -132,138 +133,7 @@
 };
 
 const versions = {
-	classic: {},
-	megacity: {
-		font: "megacity",
-		animationSpeed: 0.5,
-		numColumns: 40,
-	},
-	neomatrixology: {
-		font: "neomatrixology",
-		animationSpeed: 0.8,
-		numColumns: 40,
-		palette: [
-			{ color: hsl(0.15, 0.9, 0.0), at: 0.0 },
-			{ color: hsl(0.15, 0.9, 0.2), at: 0.2 },
-			{ color: hsl(0.15, 0.9, 0.7), at: 0.7 },
-			{ color: hsl(0.15, 0.9, 0.8), at: 0.8 },
-		],
-		cursorColor: hsl(0.167, 1, 0.75),
-		cursorIntensity: 2,
-	},
-	operator: {
-		cursorColor: hsl(0.375, 1, 0.66),
-		cursorIntensity: 3,
-		bloomSize: 0.6,
-		bloomStrength: 0.75,
-		highPassThreshold: 0.0,
-		cycleSpeed: 0.01,
-		cycleFrameSkip: 8,
-		brightnessOverride: 0.22,
-		brightnessThreshold: 0,
-		fallSpeed: 0.6,
-		glyphEdgeCrop: 0.15,
-		glyphHeightToWidth: 1.35,
-		rippleTypeName: "box",
-		numColumns: 108,
-		palette: [
-			{ color: hsl(0.4, 0.8, 0.0), at: 0.0 },
-			{ color: hsl(0.4, 0.8, 0.5), at: 0.5 },
-			{ color: hsl(0.4, 0.8, 1.0), at: 1.0 },
-		],
-		raindropLength: 1.5,
-	},
-	nightmare: {
-		font: "gothic",
-		isolateCursor: false,
-		highPassThreshold: 0.7,
-		baseBrightness: -0.8,
-		brightnessDecay: 0.75,
-		fallSpeed: 1.2,
-		hasThunder: true,
-		numColumns: 60,
-		cycleSpeed: 0.35,
-		palette: [
-			{ color: hsl(0.0, 1.0, 0.0), at: 0.0 },
-			{ color: hsl(0.0, 1.0, 0.2), at: 0.2 },
-			{ color: hsl(0.0, 1.0, 0.4), at: 0.4 },
-			{ color: hsl(0.1, 1.0, 0.7), at: 0.7 },
-			{ color: hsl(0.2, 1.0, 1.0), at: 1.0 },
-		],
-		raindropLength: 0.5,
-		slant: (22.5 * Math.PI) / 180,
-	},
-	paradise: {
-		font: "coptic",
-		isolateCursor: false,
-		bloomStrength: 1,
-		highPassThreshold: 0,
-		cycleSpeed: 0.005,
-		baseBrightness: -1.3,
-		baseContrast: 2,
-		brightnessDecay: 0.05,
-		fallSpeed: 0.02,
-		isPolar: true,
-		rippleTypeName: "circle",
-		rippleSpeed: 0.1,
-		numColumns: 40,
-		palette: [
-			{ color: hsl(0.0, 0.0, 0.0), at: 0.0 },
-			{ color: hsl(0.0, 0.8, 0.3), at: 0.3 },
-			{ color: hsl(0.1, 0.8, 0.5), at: 0.5 },
-			{ color: hsl(0.1, 1.0, 0.6), at: 0.6 },
-			{ color: hsl(0.1, 1.0, 0.9), at: 0.9 },
-		],
-		raindropLength: 0.4,
-	},
-	resurrections: {
-		font: "resurrections",
-		glyphEdgeCrop: 0.1,
-		cursorColor: hsl(0.292, 1, 0.8),
-		cursorIntensity: 2,
-		baseBrightness: -0.7,
-		baseContrast: 1.17,
-		highPassThreshold: 0,
-		numColumns: 70,
-		cycleSpeed: 0.03,
-		bloomStrength: 0.7,
-		fallSpeed: 0.3,
-		palette: [
-			{ color: hsl(0.375, 0.9, 0.0), at: 0.0 },
-			{ color: hsl(0.375, 1.0, 0.6), at: 0.92 },
-			{ color: hsl(0.375, 1.0, 1.0), at: 1.0 },
-		],
-	},
-	trinity: {
-		font: "resurrections",
-		glintTexture: "metal",
-		baseTexture: "pixels",
-		glyphEdgeCrop: 0.1,
-		cursorColor: hsl(0.292, 1, 0.8),
-		cursorIntensity: 2,
-		isolateGlint: true,
-		glintColor: hsl(0.131, 1, 0.6),
-		glintIntensity: 3,
-		glintBrightness: -0.5,
-		glintContrast: 1.5,
-		baseBrightness: -0.4,
-		baseContrast: 1.5,
-		highPassThreshold: 0,
-		numColumns: 60,
-		cycleSpeed: 0.03,
-		bloomStrength: 0.7,
-		fallSpeed: 0.3,
-		palette: [
-			{ color: hsl(0.37, 0.6, 0.0), at: 0.0 },
-			{ color: hsl(0.37, 0.6, 0.5), at: 1.0 },
-		],
-		cycleSpeed: 0.01,
-		volumetric: true,
-		forwardSpeed: 0.2,
-		raindropLength: 0.3,
-		density: 0.75,
-	},
-	morpheus: {
+  classic: {
 		font: "resurrections",
 		glintTexture: "mesh",
 		baseTexture: "metal",
@@ -283,8 +153,8 @@
 		bloomStrength: 0.7,
 		fallSpeed: 0.3,
 		palette: [
-			{ color: hsl(0.97, 0.6, 0.0), at: 0.0 },
-			{ color: hsl(0.97, 0.6, 0.5), at: 1.0 },
+      { color: hsl(0.51, 0.74, 0.0), at: 0.0 },
+      { color: hsl(0.51, 0.74, 0.5), at: 1.0 },
 		],
 		cycleSpeed: 0.015,
 		volumetric: true,
@@ -292,109 +162,6 @@
 		raindropLength: 0.4,
 		density: 0.75,
 	},
-	bugs: {
-		font: "resurrections",
-		glintTexture: "sand",
-		baseTexture: "metal",
-		glyphEdgeCrop: 0.1,
-		cursorColor: hsl(0.619, 1, 0.65),
-		cursorIntensity: 2,
-		isolateGlint: true,
-		glintColor: hsl(0.625, 1, 0.6),
-		glintIntensity: 3,
-		glintBrightness: -1,
-		glintContrast: 3,
-		baseBrightness: -0.3,
-		baseContrast: 1.5,
-		highPassThreshold: 0,
-		numColumns: 60,
-		cycleSpeed: 0.03,
-		bloomStrength: 0.7,
-		fallSpeed: 0.3,
-		palette: [
-			{ color: hsl(0.12, 0.6, 0.0), at: 0.0 },
-			{ color: hsl(0.14, 0.6, 0.5), at: 1.0 },
-		],
-		cycleSpeed: 0.01,
-		volumetric: true,
-		forwardSpeed: 0.4,
-		raindropLength: 0.3,
-		density: 0.75,
-	},
-	palimpsest: {
-		font: "huberfishA",
-		isolateCursor: false,
-		bloomStrength: 0.2,
-		numColumns: 40,
-		raindropLength: 1.2,
-		cycleFrameSkip: 3,
-		fallSpeed: 0.5,
-		slant: Math.PI * -0.0625,
-		palette: [
-			{ color: hsl(0.15, 0.25, 0.9), at: 0.0 },
-			{ color: hsl(0.6, 0.8, 0.1), at: 0.4 },
-		],
-	},
-	twilight: {
-		font: "huberfishD",
-		cursorColor: hsl(0.167, 1, 0.8),
-		cursorIntensity: 1.5,
-		bloomStrength: 0.1,
-		numColumns: 50,
-		raindropLength: 0.9,
-		fallSpeed: 0.1,
-		highPassThreshold: 0.0,
-		palette: [
-			{ color: hsl(0.6, 1.0, 0.05), at: 0.0 },
-			{ color: hsl(0.6, 0.8, 0.1), at: 0.1 },
-			{ color: hsl(0.88, 0.8, 0.5), at: 0.5 },
-			{ color: hsl(0.15, 1.0, 0.6), at: 0.8 },
-			// { color: hsl(0.1, 1.0, 0.9), at: 1.0 },
-		],
-	},
-
-	holoplay: {
-		font: "resurrections",
-		glintTexture: "metal",
-		glyphEdgeCrop: 0.1,
-		cursorColor: hsl(0.292, 1, 0.8),
-		cursorIntensity: 2,
-		isolateGlint: true,
-		glintColor: hsl(0.131, 1, 0.6),
-		glintIntensity: 3,
-		glintBrightness: -0.5,
-		glintContrast: 1.5,
-		baseBrightness: -0.4,
-		baseContrast: 1.5,
-		highPassThreshold: 0,
-		cycleSpeed: 0.03,
-		bloomStrength: 0.7,
-		fallSpeed: 0.3,
-		palette: [
-			{ color: hsl(0.37, 0.6, 0.0), at: 0.0 },
-			{ color: hsl(0.37, 0.6, 0.5), at: 1.0 },
-		],
-		cycleSpeed: 0.01,
-		raindropLength: 0.3,
-
-		renderer: "regl",
-		numColumns: 20,
-		ditherMagnitude: 0,
-		bloomStrength: 0,
-		volumetric: true,
-		forwardSpeed: 0,
-		density: 3,
-		useHoloplay: true,
-	},
-
-	["3d"]: {
-		volumetric: true,
-		fallSpeed: 0.5,
-		cycleSpeed: 0.03,
-		baseBrightness: -0.9,
-		baseContrast: 1.5,
-		raindropLength: 0.3,
-	},
 };
 versions.throwback = versions.operator;
 versions.updated = versions.resurrections;
@@ -402,171 +169,34 @@
 versions["2003"] = versions.classic;
 versions["2021"] = versions.resurrections;
 
-const range = (f, min = -Infinity, max = Infinity) => Math.max(min, Math.min(max, f));
+const range = (f, min = -Infinity, max = Infinity) =>
+  Math.max(min, Math.min(max, f));
 const nullNaN = (f) => (isNaN(f) ? null : f);
-const isTrue = (s) => s.toLowerCase().includes("true");
-
-const parseColor = (isHSL) => (s) => ({
-	space: isHSL ? "hsl" : "rgb",
-	values: s.split(",").map(parseFloat),
-});
-
-const parseColors = (isHSL) => (s) => {
-	const values = s.split(",").map(parseFloat);
-	const space = isHSL ? "hsl" : "rgb";
-	return Array(Math.floor(values.length / 3))
-		.fill()
-		.map((_, index) => ({
-			space,
-			values: values.slice(index * 3, (index + 1) * 3),
-		}));
-};
-
-const parsePalette = (isHSL) => (s) => {
-	const values = s.split(",").map(parseFloat);
-	const space = isHSL ? "hsl" : "rgb";
-	return Array(Math.floor(values.length / 4))
-		.fill()
-		.map((_, index) => {
-			const colorValues = values.slice(index * 4, (index + 1) * 4);
-			return {
-				color: {
-					space,
-					values: colorValues.slice(0, 3),
-				},
-				at: colorValues[3],
-			};
-		});
-};
-
-const paramMapping = {
-	testFix: { key: "testFix", parser: (s) => s },
-	version: { key: "version", parser: (s) => s },
-	font: { key: "font", parser: (s) => s },
-	effect: { key: "effect", parser: (s) => s },
-	camera: { key: "useCamera", parser: isTrue },
-	numColumns: { key: "numColumns", parser: (s) => nullNaN(parseInt(s)) },
-	density: { key: "density", parser: (s) => nullNaN(range(parseFloat(s), 0)) },
-	resolution: { key: "resolution", parser: (s) => nullNaN(parseFloat(s)) },
-	animationSpeed: {
-		key: "animationSpeed",
-		parser: (s) => nullNaN(parseFloat(s)),
-	},
-	forwardSpeed: {
-		key: "forwardSpeed",
-		parser: (s) => nullNaN(parseFloat(s)),
-	},
-	cycleSpeed: { key: "cycleSpeed", parser: (s) => nullNaN(parseFloat(s)) },
-	fallSpeed: { key: "fallSpeed", parser: (s) => nullNaN(parseFloat(s)) },
-	raindropLength: {
-		key: "raindropLength",
-		parser: (s) => nullNaN(parseFloat(s)),
-	},
-	slant: {
-		key: "slant",
-		parser: (s) => nullNaN((parseFloat(s) * Math.PI) / 180),
-	},
-	bloomSize: {
-		key: "bloomSize",
-		parser: (s) => nullNaN(range(parseFloat(s), 0, 1)),
-	},
-	bloomStrength: {
-		key: "bloomStrength",
-		parser: (s) => nullNaN(range(parseFloat(s), 0, 1)),
-	},
-	ditherMagnitude: {
-		key: "ditherMagnitude",
-		parser: (s) => nullNaN(range(parseFloat(s), 0, 1)),
-	},
-	url: { key: "bgURL", parser: (s) => s },
-	palette: { key: "palette", parser: parsePalette(false) },
-	stripeColors: { key: "stripeColors", parser: parseColors(false) },
-	backgroundColor: { key: "backgroundColor", parser: parseColor(false) },
-	cursorColor: { key: "cursorColor", parser: parseColor(false) },
-	glintColor: { key: "glintColor", parser: parseColor(false) },
-
-	paletteHSL: { key: "palette", parser: parsePalette(true) },
-	stripeHSL: { key: "stripeColors", parser: parseColors(true) },
-	backgroundHSL: { key: "backgroundColor", parser: parseColor(true) },
-	cursorHSL: { key: "cursorColor", parser: parseColor(true) },
-	glintHSL: { key: "glintColor", parser: parseColor(true) },
-
-	cursorIntensity: {
-		key: "cursorIntensity",
-		parser: (s) => nullNaN(range(parseFloat(s), 0, Infinity)),
-	},
-
-	glyphIntensity: {
-		key: "glyphIntensity",
-		parser: (s) => nullNaN(range(parseFloat(s), 0, Infinity)),
-	},
-
-	volumetric: { key: "volumetric", parser: isTrue },
-	glyphFlip: { key: "glyphFlip", parser: isTrue },
-	glyphRotation: {
-		key: "glyphRotation",
-		parser: (s) => nullNaN(range(parseFloat(s), 0, Infinity)),
-	},
-	loops: { key: "loops", parser: isTrue },
-	fps: { key: "fps", parser: (s) => nullNaN(range(parseFloat(s), 0, 60)) },
-	skipIntro: { key: "skipIntro", parser: isTrue },
-	renderer: { key: "renderer", parser: (s) => s },
-	suppressWarnings: { key: "suppressWarnings", parser: isTrue },
-	once: { key: "once", parser: isTrue },
-	isometric: { key: "isometric", parser: isTrue },
-};
-
-paramMapping.paletteRGB = paramMapping.palette;
-paramMapping.stripeRGB = paramMapping.stripeColors;
-paramMapping.backgroundRGB = paramMapping.backgroundColor;
-paramMapping.cursorRGB = paramMapping.cursorColor;
-paramMapping.glintRGB = paramMapping.glintColor;
-
-paramMapping.width = paramMapping.numColumns;
-paramMapping.dropLength = paramMapping.raindropLength;
-paramMapping.angle = paramMapping.slant;
-paramMapping.colors = paramMapping.stripeColors;
-
-export default (urlParams) => {
-	const validParams = Object.fromEntries(
-		Object.entries(urlParams)
-			.filter(([key]) => key in paramMapping)
-			.map(([key, value]) => [paramMapping[key].key, paramMapping[key].parser(value)])
-			.filter(([_, value]) => value != null),
-	);
-
-	if (validParams.effect != null) {
-		if (validParams.cursorColor == null) {
-			validParams.cursorColor = hsl(0, 0, 1);
-		}
-
-		if (validParams.cursorIntensity == null) {
-			validParams.cursorIntensity = 2;
-		}
-
-		if (validParams.glintColor == null) {
-			validParams.glintColor = hsl(0, 0, 1);
-		}
-
-		if (validParams.glyphIntensity == null) {
-			validParams.glyphIntensity = 1;
-		}
-	}
 
-	const version = validParams.version in versions ? versions[validParams.version] : versions.classic;
-	const fontName = [validParams.font, version.font, defaults.font].find((name) => name in fonts);
+export default () => {
+  const version = versions.classic;
+  const fontName = [version.font, defaults.font].find((name) => name in fonts);
 	const font = fonts[fontName];
 
-	const baseTextureURL = textureURLs[[version.baseTexture, defaults.baseTexture].find((name) => name in textureURLs)];
+  const baseTextureURL =
+    textureURLs[
+      [version.baseTexture, defaults.baseTexture].find(
+        (name) => name in textureURLs
+      )
+    ];
 	const hasBaseTexture = baseTextureURL != null;
-	const glintTextureURL = textureURLs[[version.glintTexture, defaults.glintTexture].find((name) => name in textureURLs)];
+  const glintTextureURL =
+    textureURLs[
+      [version.glintTexture, defaults.glintTexture].find(
+        (name) => name in textureURLs
+      )
+    ];
 	const hasGlintTexture = glintTextureURL != null;
 
 	const config = {
 		...defaults,
 		...version,
 		...font,
-		...validParams,
 		baseTextureURL,
 		glintTextureURL,
 		hasBaseTexture,
Only in .: lib
Only in ../../matrix-code-github/js/: webgpu
```