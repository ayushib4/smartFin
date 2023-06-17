import 'package:flutter/material.dart';
import 'package:smart_fin_flutter/screens/home.dart';

void main() {
  runApp(const SmartFin());
}

class SmartFin extends StatelessWidget {
  const SmartFin({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'SmartFin',
      theme: ThemeData(
        colorScheme: const ColorScheme.dark(),
        useMaterial3: true,
      ),
      home: const Home(),
    );
  }
}
