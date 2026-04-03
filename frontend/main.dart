// Basic Flutter App Placeholder

import 'package:flutter/material.dart';

void main() {
  runApp(MindMeshApp());
}

class MindMeshApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'MindMesh',
      home: Scaffold(
        appBar: AppBar(title: Text('MindMesh')),
        body: Center(
          child: Text('Mental Health Monitoring App'),
        ),
      ),
    );
  }
}
