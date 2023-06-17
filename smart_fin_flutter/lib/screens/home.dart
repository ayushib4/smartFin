import 'package:flutter/material.dart';

class Home extends StatefulWidget {
  const Home({super.key});

  @override
  State<Home> createState() => _HomeState();
}

class _HomeState extends State<Home> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              const Padding(
                padding: EdgeInsets.all(16.0),
                child: Text(
                  'SmartFin',
                  style: TextStyle(fontSize: 36, fontWeight: FontWeight.bold),
                ),
              ),
              Padding(
                padding: const EdgeInsets.fromLTRB(16.0, 0, 16.0, 16.0),
                child: ElevatedButton(
                  onPressed: () => {print("hi")},
                  child: const Text('Sign in with Plaid'),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
