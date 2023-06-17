import 'package:flutter/material.dart';

class Home extends StatelessWidget {
  const Home({super.key});

  @override
  Widget build(BuildContext context) {
    return const Column(
      children: [
        Text(
          'SmartFin',
          style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
        ),
        Text('Sign in with Plaid'),
      ],
    );
  }
}
